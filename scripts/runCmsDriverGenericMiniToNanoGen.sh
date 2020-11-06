#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. (last two args optional): bash genericNanoGenFromMini.sh <das_path> <outfile.root> <config_name.py> <nevents>"
    exit 1
fi

das_name=$1
temp=$(echo $1 | cut -d "/" -f2)
outfile=${temp:1}.root
config_name=configs/${outfile/.root/_cfg.py}
nevents=1000

customize=""
if [[ $# -gt 1 ]]; then
    customize="--customise_commands process.lheWeights.failIfInvalidXML=False"
fi
if [[ $# -gt 2 ]]; then
    nevents=$3
fi

cmsDriver.py step1 --filein "dbs:$das_name" \
    --fileout $outfile --mc --eventcontent NANOAODGEN --datatier NANOAODSIM \
    --conditions auto:mc --step NANOGEN --nThreads 1 --python_filename $config_name \
    --no_exec $customize --customise Configuration/DataProcessing/Utils.addMonitoring -n $nevents

