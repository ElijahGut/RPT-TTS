# example run command: python3 gen_sequence.py libri_isolated DEMO_experiment slt oph tac (system order matters here!)
# for Latin square: run this script 3 times for 3 groups, changing the order of the systems each time

import os
import re
import sys

st_name = sys.argv[1]
seq_name = sys.argv[2]
system_names = sys.argv[3:]

def split_stimuli(st_name):
    f = open('./stimuli/{}.txt'.format(st_name), 'r')
    stimuli = f.readlines()
    for i in range(len(stimuli)):
        s = stimuli[i]
        s = s.replace('--', '-- ')
        g = open('./txt/{}_{}.txt'.format(st_name, (i+1)), 'w')
        for j in range(len(s.split())):
            word = s.split()[j]
            if j % 10 == 0 and j > 0:
                g.write('{}\n'.format(word))
            else:
                g.write(word+' ')
        g.close()
    f.close()

def sort_stimuli(stimuli):
    result = [''] * len(stimuli)
    for st in stimuli:
        m = re.search(r"\d+", st)
        if m is not None:
            n = int(m.group())
            result[n-1] = st
    final_sorted = [i for i in result if i != '']
    return final_sorted

def write_sequence(seq_name, system_names):
    f = open('./sequence.txt', 'w')
    f.write('*{}\n'.format(seq_name))
    f.write('login\n\nconsent consent_form\nsurvey presurvey\ntext_page remote_experiment_notice\nmedia_test audio test_loud\ntext_page error_marker_instructions\nerror_mark test_1_slt test_1 1 3 error_marker_reminder_test_1 pmos_question bindPlayKeyID=space\nerror_mark test_3_oph_loud test_2 1 3 error_marker_reminder_test_2 pmos_question bindPlayKeyID=space\n\
error_mark test_2_slt test_3 1 3 error_marker_reminder_test_3 pmos_question bindPlayKeyID=space\ntext_page error_marker_instructions_2\n\n<randomize>\n')
    stimuli = os.listdir('./txt')
    stimuli = [s for s in stimuli if 'test' not in s]
    sorted_stimuli = sort_stimuli(stimuli)
    size_of_groups = int(len(sorted_stimuli)/len(system_names))
    for i in range(len(system_names)):
        sn = system_names[i]
        idx = i*size_of_groups
        group_stims = sorted_stimuli[idx:idx+size_of_groups]
        final_group = [g.strip('.txt') for g in group_stims]
        for st_name in final_group:
            f.write('error_mark {} {} 1 3 error_marker_reminder pmos_question bindPlayKeyID=space\n'.format(st_name+'_{}'.format(sn), st_name))
    f.write('</randomize>\n\nsurvey postsurvey\n\nend\n')
    f.close()

def main(st_name, seq_name):
    split_stimuli(st_name)
    write_sequence(seq_name, system_names)


main(st_name, seq_name)