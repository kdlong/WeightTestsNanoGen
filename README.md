Some scripts and results of testing the gen weight refactor

Needs to run in a CMSSW version that has NanoGen, so a nightly build or CMSSW_11_2_0_pre>=7

Example: ```bash scripts/runCmsDriverGenericMiniToNanoGen.sh /TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM 10```

In the new weight refactor code, a variable failIfInvalidXML controls whether or not the parsing should try to recover from a poorly formed weight header. A 3rd argument can be used to se this variable (1 or 0 for true or false).

If you just want to see that the weights are added properly, you can use

```python test/testNanoWeights.py <NanoGenFile.root> [--scan]```

Where the optional ```--scan``` option will print the values of the weights using TTree::Scan
