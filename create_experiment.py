# NOTE: how to run this script: python3 create_experiment.py rpt_demo libri_isolated RPT_DEMO_experiment slt oph tac

from subprocess import run
from itertools import combinations
from collections import deque
import shutil
import sys
import os

exp_name = sys.argv[1]
stimulus_base = sys.argv[2]
exp_alias = sys.argv[3]
systems = deque(sys.argv[4:])
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
def custom_copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def copy_media(e):
    audio_path = './master_audio_and_video'
    stim_path = './master_stimuli'
    # for now copy all, refactor to make this more optimal later
    custom_copytree(audio_path, os.path.join('tests', e, 'audio_and_video'))
    custom_copytree(stim_path, os.path.join('tests', e, 'stimuli'))

def run_gen_sequence(e, i):
    gen_seq_path = os.path.join('tests', e)
    os.chdir(gen_seq_path)
    perm = system_perms[i]
    run_args = ['python3', './gen_sequence.py', stimulus_base, exp_alias] + perm
    run(run_args)
    os.chdir('../../')

def create_groups():
    # run create_group based on the number of systems: naming convention is ${EXP_NAME}_{GroupNo}
    for i in range(len(systems)):
        e = f'{exp_name}_{i+1}'
        run(['./lmeds/user_scripts/create_group.sh', e])
        copy_media(e)
        run_gen_sequence(e, i)

def main():
    print(f'System permutations are: {system_perms}')
    create_groups()
    print('created all groups!')

main()