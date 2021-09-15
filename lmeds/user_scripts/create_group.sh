#!/bin/sh

# run source setup.sh before running this script!

NAME=${1}

cp -rf ${TESTS}/rpt_tts_demo/ tests/${NAME}
python3 ./lmeds/user_scripts/write_cgi.py ${NAME}

cd ${TESTS}/${NAME}
rm audio_and_video/*
rm stimuli/*
rm txt/*

cd ${HOME}
echo "created group ${NAME} in tests directory"