
---------
RPT-TTS
---------

-----

RPT-TTS is a web platform for collecting error annotation data online for speech synthesis evaluation, based on the LMEDS platform by Tim Mahrt.

LMEDS was developed for conducting Rapid Prosody Transcription (RPT) annotations over the internet. RPT-TTS adapts LMEDS for text-to-speech (TTS) evaluation.

RPT-TTS was initially used for: Gutierrez, E., Oplustil-Gallegos, P., Lai, C. (2021) Location, Location: Enhancing the Evaluation of Text-to-Speech synthesis using the Rapid Prosody Transcription Paradigm. Proc. 11th ISCA Speech Synthesis Workshop (SSW 11), 25-30, doi: 10.21437/SSW.2021-5. 

RPT-TTS builds upon the original LMEDS platform by:

- embedding multiple tasks in one page, namely the RPT and MOS tasks; 
- adding support for Latin square design experiments;
- showing the MOS slider value for the user

.. sectnum::
.. contents::

Requirements
==============

``Python 3.3.*`` or above
Bash 

Usage
=========

Before using RPT-TTS, you will need:

- audio samples of synthetic speech in either mp3 or wav format;
- a txt file containing all stimuli each on their own line

Installation
================

Please see the manual for instructions on installing LMEDS on a server, running
LMEDS on a local computer (no server required), or for using the included user scripts.

Citing LMEDS
===============

If you use RPT-TTS and/or LMEDS in your research, please cite them like so:

Elijah Gutierrez. RPT-TTS. Rapid Prosody Transcription paradigm for Text-to-Speech evaluation.
https://github.com/ElijahGut/RPT-TTS, 2021.

Tim Mahrt. LMEDS: Language markup and experimental design software.
https://github.com/timmahrt/LMEDS, 2016.
