#!/usr/bin/env python
# -*- coding: utf-8 -*-

import experiment_runner
experiment_runner.runExperiment("rpt_tts_demo",
                                "sequence.txt",
                                "english.txt",
                                disableRefresh=False,
                                audioExtList=[".mp3"],
                                allowUtilityScripts=True,
				individualSequences=True,
                                allowUsersToRelogin=True)
