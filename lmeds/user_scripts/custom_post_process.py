# NOTE: this script processes results for ONE listener group or test directory,
# if your experiment has more than one group, use stitch.py

import os
import re
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# NOTE: make sure to call source setup.sh before calling this script!

# how to call this script: python custom_post_process [EXPERIMENT_NAME] [SEQUENCE_FILE_NAME] 
# NOTE: SEQUENCE_FILE_NAME is sequence.txt by default
# example call: python custom_post_process rpt_tts_demo sequence.txt

home_path = os.environ["HOME"] 
fig_path = os.environ["FIGS"] 
exp_name = sys.argv[1]
seq_name = sys.argv[2]

exp_title = ''

# number of expected entries if test was conducted correctly (default is 30)
N = 30

# gets relevant information from all users for one experiment. Returns a list of tuples corresponding to:
# (stimulus_name, stimulus string, user response i.e. marks, mos, tick response)
def get_outputs():
    seq_path = os.path.join(home_path, 'tests', exp_name, seq_name)
    seq_raw = open(seq_path, 'r')
    exp_title = seq_raw.readlines()[0].strip('\n*')
    exp_out_path = os.path.join(home_path, 'tests', exp_name, 'output', exp_title)
    outs = os.listdir(exp_out_path)
    stims = []
    stim_path = os.path.join(home_path, 'tests', exp_name, 'stimuli', 'libri_isolated.txt')
    stims_raw = open(stim_path, 'r')
    stims = stims_raw.readlines()
    stims_raw.close()
    final_output = []
    for o in outs:
        f = open(os.path.join(exp_out_path, o), 'r')
        out = f.readlines()
        out_clean = [l.strip('\n') for l in out]
        temp = []
        temp.append(o.strip('.csv'))
        for line in out_clean:
            split_line = line.split(';')
            if split_line[0].split(',')[0] == 'prominence' and ('libri_isolated' in line or 'focus' in line):
                st_name = split_line[0].split(',')[1].strip('[')
                st_result = split_line[1]
                st_ind = int(re.search(r'\d+', st_name).group())
                st_val = stims[st_ind-1].strip('\n')
                survey_result = split_line[-1]
                survey_result_split = survey_result.split(',')
                mos = survey_result_split[0][-1]
                ticks = survey_result_split[1:]
                final_tuple = (st_name, st_val, st_result, mos, ticks)
                temp.append(final_tuple)
        final_output.append(temp)
        temp = []
        f.close()
    seq_raw.close()
    return final_output


def post_process(N):
    final_output = get_outputs()
    final_dict = {}
    kappa_dict = {}
    for o in final_output:
        user_responses = o[1:]
        if len(user_responses) != N:
            print('Error in response for user: {}'.format(o[0]))
        for ur in user_responses:
            st_name = ur[0]
            st_val = ur[1]
            marks = [int(m) for m in ur[2].split(',')[1:]]
            score = int(ur[3])
            ticks = []
            if st_name not in kappa_dict:
                kappa_dict[st_name] = [marks]
            else:
                all_marks = kappa_dict[st_name]
                all_marks.append(marks)
                kappa_dict[st_name] = all_marks
            if ur[4][4] != '' and ('oph' in st_name or 'tac' in st_name):
                    print(st_name, ur[4][4], o[0])
            for t in ur[4][0:4]:
                if t == '':
                    ticks.append(0)
                else:
                    ticks.append(int(t))
            if st_name not in final_dict:
                final_dict[st_name] = (st_name, st_val, marks, [score], ticks)
            else:
                v = final_dict[st_name]
                v_marks = v[2]
                v_scores = v[3]
                v_ticks = v[4]
                v_scores.append(score)
                newv_marks = np.add(v_marks, marks)
                newv_scores = v_scores
                newv_ticks = np.add(v_ticks, ticks)
                newv = (st_name, st_val, newv_marks.tolist(), newv_scores, newv_ticks.tolist())
                final_dict[st_name] = newv

    # calculate mos
    for k in final_dict:
        v = final_dict[k]
        scores = v[3]
        mos = np.mean(scores)
        finalv = (v[0].replace('\'', '\''), v[1], v[2], round(mos, 2), v[4])
        final_dict[k] = finalv  

    return final_dict

# helper for bulk_plot_heatmaps
def plot_heatmap(st_name, stimulus, user_response, mos, cbarlabel):
    if 'tac' in st_name:
        st_name = st_name.replace('tac', 'fp')
    st_split = stimulus.split()
    ur_array = np.array(user_response)
    fig, ax= plt.subplots(figsize=(15,0.3))
    rcParams['font.family'] = 'serif'
    fig.suptitle('Heatmap for {}'.format(st_name),fontsize=16, x=0.42, y=4.5)
    im = ax.imshow(ur_array[np.newaxis,:], cmap='plasma', aspect='auto')
    ax.set_yticks([])
    ax.set_xticks(np.arange(len(ur_array)))
    ax.set_xticklabels(st_split)
    if len(st_split) <= 5:
        ax.tick_params(top=True, bottom=False,
                       labeltop=True, labelbottom=False, labelsize=14)
    elif len(st_split) <= 10 and len(st_split) > 5:
        ax.tick_params(top=True, bottom=False,
                       labeltop=True, labelbottom=False, labelsize=12)
    else:
        ax.tick_params(top=True, bottom=False,
                       labeltop=True, labelbottom=False, labelsize=10)
    ax.set_xlabel('Total marks: {}, PMOS: {}'.format(np.sum(ur_array), mos), labelpad=30, fontsize=14)
    cbar = plt.colorbar(im, ax=ax, shrink=10)
    im.set_clim(0)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    # save fig as pdf
    plt.savefig('{}{}.pdf'.format(fig_path, st_name), bbox_inches='tight')
    print('Saved plot for {}'.format(st_name))
    plt.close()
    return im, cbar

def bulk_plot_heatmaps(final_dict):
    for k in final_dict:
        v = final_dict[k]
        st_name = v[0]
        st = v[1]
        ur = v[2]
        mos = v[3]
        plot_heatmap(st_name, st, ur, mos, 'Counts')


final_dict = post_process(N)

# plot all heatmaps using annotation data
# bulk_plot_heatmaps(final_dict)

# write final dictionary to output file for stitch.py
f = open('./final_dicts/{}.txt'.format(exp_name), 'w')
f.write(str(final_dict))
f.close()

