from DataFormats.FWLite import Runs,Handle
import IPython

def writeHeader(outfile_name, edmfile, onlyWeights=True):
    with open(outfile_name, "w") as outfile:
        outfile.write("# ---> From file %s" % edmfile)

        source = "externalLHEProducer"
        #source = "source"
        runs = Runs(edmfile)
        run = runs.__iter__().next()
        runInfoHandle = Handle("LHERunInfoProduct")
        run.getByLabel(source, runInfoHandle)
        runInfo = runInfoHandle.product()
        foundrwgt = False
        IPython.embed()
        for i, h in enumerate(runInfo.headers_begin()):
            print i, h, runInfo.headers_size()
            if i == runInfo.headers_size() or i > 20:
                break
            # For some of the 7_1_X samples, the header is added for each LHE file, read only the first copy
            if "initrwgt" in str(h.tag()):
                if foundrwgt:
                    break
                foundrwgt = True
            if not foundrwgt and onlyWeights:
                continue
            for line in h.lines():
                outfile.write(line)
                
filemap = { 
        "DrellYan_LO_MGMLMv242_2017" : "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FlatPU28to62HcalNZSRAW_94X_mcRun2_asymptotic_v3-v1/260000/5436C913-046D-E911-B076-0025905A60BE.root",
        "DrellYan_LO_MGMLMv233_2016" : "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/CC675D46-5EDF-E811-B537-3CFDFE63DF40.root",
        "DrellYan_NLO_MGFXFXv233_2016" : "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_plus5percentMaterial_94X_mcRun2_asymptotic_v3-v2/70000/860C654F-633D-E911-8316-0CC47A2B03A2.root",
        "WZVBS_2017" : "root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/7E4F4321-598D-6A45-9681-8F8BA9817ECE.root",
        "DrellYan_NLO_MGFXFXv242_2017" : "root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/61CD1B34-65BD-DF42-812C-87CEF2E9AD1A.root",
        "ZZTo4L_powheg_2016" : "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/B84CB0F2-E2C6-E811-BC6F-001A649D4631.root",
        "ZZTo4L_powheg_2017" : "root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/A3FB9D9C-6F10-6349-8345-BC3068E2E75A.root",
}

for name, filepath in filemap.iteritems():
    print "Reading header for file %s at %s" % (name, filepath)
    writeHeader(name + "_weightInfo.txt", filepath)
    writeHeader(name + "_lheheader.txt", filepath, False)