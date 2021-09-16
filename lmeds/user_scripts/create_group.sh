#!/bin/bash

# run source setup.sh before running this script!

NAME=${1}
AUD_EXT=${2}

cp -rf ${HOME}tests/rpt_tts_demo/ ${HOME}tests/${NAME}
python3 ./lmeds/user_scripts/write_cgi.py ${NAME} ${AUD_EXT}

cd ${HOME}tests/${NAME}
rm audio_and_video/*
rm stimuli/*
rm txt/*

cd ${HOME}
echo "created group ${NAME} in tests directory"