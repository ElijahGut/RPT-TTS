# NOTE: how to run this script: python3 create_experiment.py rpt_demo RPT_DEMO_experiment libri_isolated mp3 slt oph tac

from subprocess import run
from collections import deque
import shutil
import sys
import os

exp_name = sys.argv[1]
exp_alias = sys.argv[2]
stimulus_base = sys.argv[3]
aud_ext = sys.argv[4]
systems = deque(sys.argv[5:])
system_perms = []

# check that stimuli can be divided evenly into groups
try:
    f = open(f'./master_stimuli/{stimulus_base}.txt', 'r')
    N_stims = len(f.readlines())
    rem = int(N_stims % len(systems))
    if rem != 0:
        f.close()
        print('Can\'t divide stimuli into even groups. Please make sure the number of stimuli is evenly divisible by the number of systems')
        exit(1)
    f.close()
except FileNotFoundError:
    print('Stimulus file not found! The name of the txt file in master_stimuli should match the stimulus base name provided')
    exit(1)

# get system_perms
for i in range(len(systems)):
  system_perms.append(list(systems))
  systems.rotate(1)

# util
def custom_copytree(src, dst, ftc=None, symlinks=False, ignore=None):
    for item in os.listdir(src):
        if (ftc and os.path.splitext(item)[0] in ftc) or ftc == 'other':
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if 'README' not in s:
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks, ignore)
                else:
                    shutil.copy2(s, d)

def get_files_to_copy(e):
    raw_seq = open(os.path.join('tests', e, 'sequence.txt'))
    seq = raw_seq.readlines()
    seq = seq[8:11] + seq[14:14+N_stims]
    fs = [f.split()[1] for f in seq]
    return fs

# this method only copies the necessary media for the current experiment to save as much space as possible
def copy_media(e):
    files_to_copy = get_files_to_copy(e)
    shutil.copyfile('./master_audio_and_video/test_loud.mp3', os.path.join('tests', e, 'audio_and_video', 'test_loud.mp3'))
    custom_copytree('./master_audio_and_video', os.path.join('tests', e, 'audio_and_video'), ftc=files_to_copy)
    custom_copytree('./master_tests', os.path.join('tests', e, 'txt'), ftc='other')

def run_gen_sequence(e, i):
    gen_seq_path = os.path.join('tests', e)
    os.chdir(gen_seq_path)
    perm = system_perms[i]
    run_args = ['python3', './gen_sequence.py', stimulus_base, f'{exp_alias}_{i+1}'] + perm
    run(run_args)
    os.rename('./output/DEMO_experiment', f'./output/{exp_alias}_{i+1}')
    os.rename('./individual_sequences/DEMO_experiment', f'./individual_sequences/{exp_alias}_{i+1}')
    os.chdir('../../')

def create_groups():
    # run create_group based on the number of systems: naming convention is ${EXP_NAME}_{GroupNo}
    for i in range(len(systems)):
        e = f'{exp_name}_{i+1}'
        run(['./lmeds/user_scripts/create_group.sh', e, aud_ext])
        # copy stimulus file before generating sequence file
        custom_copytree('./master_stimuli', os.path.join('tests', e, 'stimuli'), ftc='other')
        run_gen_sequence(e, i)
        copy_media(e)
        run(['python3', './lmeds/user_scripts/sequence_check.py', e, 'sequence.txt', 'english.txt', 'true', f'.{aud_ext}'])

def main():
    print(f'System permutations are: {system_perms}')
    create_groups()
    print('created all groups!')

main()