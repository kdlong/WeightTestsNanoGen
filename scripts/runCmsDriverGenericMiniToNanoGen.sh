#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. (last two args optional, last arg only supported in refactor):"
    echo "    bash genericNanoGenFromMini.sh <das_path> <nevents> <failIfInvalidXML>"
    exit 1
fi

das_name=$1
temp=$(echo $1 | cut -d "/" -f2)
outfile=${temp}.root
config_name=configs/${outfile/.root/_cfg.py}
nevents=1000

if [[ $# -gt 1 ]]; then
    nevents=$2
fi

customize=""
if [[ $# -gt 2 ]]; then
    if [[ $3 -gt 0 ]]; then
        customize="--customise_commands process.lheWeights.failIfInvalidXML=False"
    fi
fi

cmsDriver.py step1 --filein "dbs:$das_name" \
    --fileout $outfile --mc --eventcontent NANOAODGEN --datatier NANOAODSIM \
    --conditions auto:mc --step NANOGEN --nThreads 1 --python_filename $config_name \
    --no_exec $customize -n $nevents
