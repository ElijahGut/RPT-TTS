import os
import re
import sys

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


def write_sequence(seq_name):
    f = open('./sequence.txt', 'w')
    f.write('*{}\n'.format(seq_name))
    f.write('login\n\nconsent consent_form\nsurvey presurvey\ntext_page remote_experiment_notice\nmedia_test audio test_loud\ntext_page error_marker_instructions\nprominence test_1_slt test_1 1 3 error_marker_reminder_test_1 pmos_question bindPlayKeyID=space\nprominence test_3_oph_loud test_2 1 3 error_marker_reminder_test_2 pmos_question bindPlayKeyID=space\n\
prominence test_2_slt test_3 1 3 error_marker_reminder_test_3 pmos_question bindPlayKeyID=space\ntext_page error_marker_instructions_2\n\n<randomize>\n')
    stimuli = os.listdir('./txt')
    stimuli = [s for s in stimuli if 'test' not in s]
    sorted_stimuli = sort_stimuli(stimuli)
    for i in range(len(sorted_stimuli)):
        st_name = sorted_stimuli[i]
        st_name = st_name.strip('.txt')
        if i >= 0 and i < 10:
            f.write('prominence {} {} 1 3 error_marker_reminder pmos_question bindPlayKeyID=space\n'.format(st_name+'_slt', st_name))
        elif i >= 10 and i < 20:
            f.write('prominence {} {} 1 3 error_marker_reminder pmos_question bindPlayKeyID=space\n'.format(st_name+'_oph', st_name))
        elif i >= 20 and i < 30:
            f.write('prominence {} {} 1 3 error_marker_reminder pmos_question bindPlayKeyID=space\n'.format(st_name+'_tac', st_name))
    f.write('</randomize>\n\nsurvey postsurvey\n\nend\n')
    f.close()

# TODO: make groups

# ABC CAB BCA, 30 stimuli each, 3 systems: slt, oph, tac

def main(st_name, seq_name):
    split_stimuli(st_name)
    write_sequence(seq_name)

st_name = sys.argv[1]
seq_name = sys.argv[2]

main(st_name, seq_name)

# example run command: python3.7 gen_sequence.py libri_isolated PILOT_experiment



