# NOTE: this script processes results across ALL listener groups. Make sure all the data has been collected,
# otherwise this script won't work!

import os
import re
import sys
import ast
import subprocess
import numpy as np

exp_name = sys.argv[1]

# how to call this script: python stitch.py [EXPERIMENT_NAME]
# example call: python stitch.py rpt_tts_demo

def get_totals(final_dict):
    totals = []
    moss = []
    ticks = [0,0,0,0]
    for v in final_dict:
        ur = v[2]
        mos = v[3]
        ticks = np.add(ticks, v[4]).tolist()
        totals.append(sum(ur))
        moss.append(mos)
    print('Totals: {}, Grand mean: {}\nMOSs: {}, Grand mean: {}, Grand std: {}'.format(totals, round(np.mean(totals), 2), moss, round(np.mean(moss), 2), round(np.std(moss), 3)))
    print('Ticks: {}\n'.format(ticks))
    return totals

def sort_stimuli(stimuli):
    sorted_stimuli = []
    result = [''] * len(stimuli)
    for st in stimuli:
        val = stimuli[st]
        m = re.search(r"\d+", st)
        if m is not None:
            n = int(m.group())
            result[n-1] = st
    final_sorted = [i for i in result if i != '']
    for i in final_sorted:
        sorted_stimuli.append(stimuli[i])
    return sorted_stimuli

def stitch():
    test_path = os.environ["TESTS"]
    raw_groups = os.listdir(test_path)
    groups = [d for d in raw_groups if re.match(r"{}*".format(exp_name), d)]
    for g in groups:
        subprocess.call(['python', 'custom_post_process.py', g, 'sequence.txt'])
    final_dicts = {}
    fds = os.listdir('./final_dicts/')
    for fd in fds:
        f = open('./final_dicts/{}'.format(fd), 'r')
        final_dict_str = f.read()
        final_dict = ast.literal_eval(final_dict_str)
        final_dicts.update(final_dict)
        f.close()

    # dictionary of all outputs for each system

    slt_dict = sort_stimuli({k: v for k,v in final_dicts.items() if 'slt' in k and 'libri' in k})
    oph_dict = sort_stimuli({k: v for k,v in final_dicts.items() if 'oph' in k and 'libri' in k})
    tac_dict = sort_stimuli({k: v for k,v in final_dicts.items() if 'tac' in k and 'libri' in k})

    print('slt totals:\n')
    get_totals(slt_dict)
    print('oph totals:\n')
    get_totals(oph_dict)
    print('tac totals:\n')
    get_totals(tac_dict)

stitch()