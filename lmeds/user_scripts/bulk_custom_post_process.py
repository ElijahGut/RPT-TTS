# NOTE: this script processes results across ALL listener groups. Make sure all the data has been collected,
# otherwise this script won't work!

import os
import re
import sys
import ast
import subprocess
import numpy as np
import pandas as pd

home_path = os.environ["HOME"] 
test_path = os.environ["TESTS"]

exp_name = sys.argv[1]

stim_file = os.listdir(os.path.join(home_path, 'master_stimuli'))[0]
sf = open(os.path.join(home_path, 'master_stimuli', stim_file,), 'r')
N = str(len(sf.readlines()))

# how to call this script: python3 bulk_custom_post_process.py [EXPERIMENT_NAME] 
# example call: python3 bulk_custom_post_process.py rpt_tts_demo 

def stitch():
    final_dicts = {}
    test_path = os.environ["TESTS"]
    raw_groups = os.listdir(test_path)
    groups = [d for d in raw_groups if exp_name in d]
    for g in groups:
        subprocess.call(['python3', 'custom_post_process.py', g, N])
    fds = os.listdir('./final_dicts/')
    for fd in fds:
        f = open(f'./final_dicts/{fd}', 'r')
        final_dict_str = f.read()
        final_dict = ast.literal_eval(final_dict_str)
        final_dicts.update(final_dict)
        f.close()
    # write to csv file
    fd_df = pd.DataFrame.from_dict(final_dicts).T
    fd_df.to_csv(f'./csvs_and_xlsx/{exp_name}.csv')
    fd_df.to_excel(f'./csvs_and_xlsx/{exp_name}.xlsx')
    return fd_df

stitch()