
---------
RPT-TTS
---------

-----

RPT-TTS is a web platform for collecting error annotation data online for speech synthesis evaluation, based on the LMEDS platform by Tim Mahrt.

LMEDS was developed for conducting Rapid Prosody Transcription (RPT) annotations over the internet. RPT-TTS adapts LMEDS for text-to-speech (TTS) evaluation.

RPT-TTS was initially used for: Gutierrez, E., Oplustil-Gallegos, P., Lai, C. (2021) Location, Location: Enhancing the Evaluation of Text-to-Speech synthesis using the Rapid Prosody Transcription Paradigm. Proc. 11th ISCA Speech Synthesis Workshop (SSW 11), 25-30, doi: 10.21437/SSW.2021-5. 

RPT-TTS builds upon the original LMEDS platform by:

- Embedding multiple tasks in one page, namely the RPT and MOS tasks; 
- Adding support for Latin square design experiments;
- Showing the MOS slider value for the user

.. sectnum::
.. contents::

Requirements
==============

``Python 3.3.*`` or above

Bash (if on Windows use Git Bash)

Usage
=========

Before using RPT-TTS, you will need:

- Audio samples of synthetic speech from different systems in either mp3 or wav format;
- A stimulus file. This is a txt file containing all the stimuli used for the experiment, each on their own line with no quotes.

**NB: The audio samples need to conform to the following naming convention**:

``[STIMULUS FILE NAME]_[ID]_[SYSTEM]``

Stimulus file name: the stem of the stimulus file.
Id: number of stimulus in the stimulus file (e.g. 15th entry has an id of 15). 
System: a shorthand for the system used to synthesise the stimulus (e.g. "tac" for Tacotron or "fast" for FastPitch).

e.g. suppose your stimulus file is called libri_isolated.txt, and you have three systems to evaluate: slt (Festival slt), oph (Ophelia), tac (Tacotron). Suppose also that the first sentence in the stimulus file is *Then Anders felt brave again.* Then the audio sample of the slt system for this stimulus (*Then Anders felt brave again*) should be denoted as libri_isolated_1_slt. For the tac system this would be libri_isolated_1_tac, and so on. 

Once all the audio samples follow this naming convention, follow these steps:

1. Change the HOME path in setup.sh to the path of the cloned directory
2. Run ``source setup.sh``
3. Place the audio samples in the master_audio_and_video folder
4. Place the stimulus file in the master_stimuli folder
5. Customise the consent form in english.txt. english.txt is the dictionary file and can be found in ``./tests/rpt_tts_demo``. For more details on the dictionary file, refer to the LMEDS manual. The relevant fields to modify are consent_title and consent_form
6. (Optional): customise pmos_question.txt in the ``./tests/rpt_tts_demo`` folder. This is the question that will be shown to participants e.g. How natural is the intonation of the speaker?
7. Run ``create_experiment.py`` (see Section 3)
8. Run ``lmeds_local_server.py`` to test the experiments on your local machine. Refer to the LMEDS manual for more details
9. Once all the data has been collected, run ``bulk_post_process.py`` (see Section 4)
10. You are now ready to analyse the processed data generated in ``./lmeds/user_scripts/csvs_and_xlsx``!


Running create_experiment.py
================

``python3 create_experiment.py [EXPERIMENT_NAME] [EXPERIMENT_ALIAS] [STIMULUS_FILE_NAME] [AUDIO_EXTENSION] [SYSTEM_1] [SYSTEM_2] [SYSTEM_3] ...``

Example run: ``python3 create_experiment.py rpt_tts_demo DEMO_experiment libri_isolated mp3 slt oph tac``

This script builds an experiment based on the stimulus file, the audio samples provided, and the systems to evaluate. The samples and systems are arranged in a Latin square design. 

The experiment alias is an alternate name for the experiment which will be used for the first line of the sequence file and as the name of various output folders (see LMEDS manual for details). The convention is to have a short version of the experiment name in uppercase followed by _experiment, e.g. DEMO_experiment. The audio extension argument can either be mp3 or wav, depending on the format of the audio samples. The final arguments are the shorthand system names. **These should match the shorthand system names that were used when naming the audio samples**.

Running bulk_post_process.py
================

``python3 bulk_post_process.py [EXPERIMENT_NAME]``

Example run: ``python3 bulk_post_process.py rpt_tts_demo``

This script processes the data from all listener groups in the specified experiment and compiles the data in both csv and xlsx formats. The outputs of the script can be found in the ``./lmeds/user_scripts/csvs_and_xlsx`` directory.

Installation
================

Please see the manual for instructions on installing LMEDS on a server or running
LMEDS on a local computer (no server required).

Contact
================

Please feel free to contact s1740779@ed.ac.uk if you have any questions. 

Citing RPT-TTS/LMEDS
===============

If you use RPT-TTS and/or LMEDS in your research, please cite them like so:

Elijah Gutierrez. RPT-TTS. Rapid Prosody Transcription paradigm for Text-to-Speech evaluation.
https://github.com/ElijahGut/RPT-TTS, 2021.

Tim Mahrt. LMEDS: Language markup and experimental design software.
https://github.com/timmahrt/LMEDS, 2016.
