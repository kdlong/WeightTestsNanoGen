#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile> <numcores>"
    exit 1
fi

customize="--customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=999"

fail=""
if [[ $# -gt 2 ]]; then
    if [[ $3 -gt 0 ]]; then 
        fail="${customize}\nprocess.lheWeights.failIfInvalidXML=False"
    fi
fi

if [[ $# -gt 3 ]]; then
    customize="${customize}\nprocess.externalLHEProducer.generateConcurrently=True --nThreads $3"
fi

fragment=${1/python\//}

cmsDriver.py Configuration/WeightTestsNanoGen/python/$fragment \
    --fileout file:$2 --mc --eventcontent RAWSIM,NANOAODSIM \
    --datatier GEN,NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN \
    --python_filename configs/${fragment/cff/cfg} \
    $customize $fail \
    -n 30 --no_exec
