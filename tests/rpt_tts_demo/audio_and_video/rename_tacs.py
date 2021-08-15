import os
import re

def rename():
    files = os.listdir(os.getcwd())
    for f in files:
        f_clean = f.lstrip('0')
        s = re.search(r'\d+', f_clean)
        if s != None:
            num = s.group()
            template = 'libri_isolated_{}_tac.wav'.format(num)
            print(f, template)
            os.rename(f, template)
rename()