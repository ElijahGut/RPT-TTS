#!/bin/bash

TYPE=${1}
NUM=${2}

if [[ "$TYPE" == "trad" ]]; then 
    cp -rv pilot_experiment_trad ./pilot_experiment_trad_${NUM}
    cd pilot_experiment_trad_${NUM}
    mv output/PILOT_experiment_trad output/PILOT_experiment_trad_${NUM}
    mv individual_sequences/PILOT_experiment_trad individual_sequences/PILOT_experiment_trad_${NUM}
    cd ../../cgi-bin/
    cp ./pilot_experiment.cgi ./pilot_experiment_trad_${NUM}.cgi
elif [[ "$TYPE" == "norm" ]]; then
    cp -rv pilot_experiment_4 ./pilot_experiment_${NUM}
    cd pilot_experiment_${NUM}
    mv output/PILOT_experiment_4 output/PILOT_experiment_${NUM}
    mv individual_sequences/PILOT_experiment_4 individual_sequences/PILOT_experiment_${NUM}
    cd ../../cgi-bin/
    cp ./pilot_experiment.cgi ./pilot_experiment_${NUM}.cgi
elif [[ "$TYPE" == "focus" ]]; then
    cp -rv prosody_experiment ./prosody_experiment_${NUM}
    cd prosody_experiment_${NUM}
    mv output/PROSODY_experiment output/PROSODY_experiment_${NUM}
    mv individual_sequences/PROSODY_experiment individual_sequences/PROSODY_experiment_${NUM}
    cd ../../cgi-bin/
    cp ./prosody_experiment.cgi ./prosody_experiment_${NUM}.cgi
else
    echo 'Wrong argument. Please pick between trad, norm, or focus.'
fi






