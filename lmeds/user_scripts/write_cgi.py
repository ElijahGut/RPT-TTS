import sys
import os

cgi_path = './cgi-bin/'
exp_name = sys.argv[1]
aud_ext = sys.argv[2]

f = open(os.path.join(cgi_path, exp_name+'.cgi'), 'w')

f_content = """#!/usr/bin/env python 
# -*- coding: utf-8 -*-  

import experiment_runner 
experiment_runner.runExperiment("{}",
                                "sequence.txt",
                                "english.txt",
                                disableRefresh=False,
                                audioExtList=["{}"],
                                allowUtilityScripts=True,
				individualSequences=True,
                                allowUsersToRelogin=True)""".format(exp_name, aud_ext)

f.write(f_content)
f.close()

os.chmod(os.path.join(cgi_path, exp_name+'.cgi'), 0o744)