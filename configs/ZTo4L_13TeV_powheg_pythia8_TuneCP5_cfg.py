# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM --fileout ZTo4L_13TeV_powheg_pythia8_TuneCP5.root --mc --eventcontent NANOAODGEN --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANOGEN --nThreads 1 --python_filename configs/ZTo4L_13TeV_powheg_pythia8_TuneCP5_cfg.py --no_exec --customise_commands process.lheWeights.failIfInvalidXML=False --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms



process = cms.Process('NANOGEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nanogen_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( (
        'file:/afs/cern.ch/user/k/kelong/work/WeightStudy/CMSSW_11_1_0_pre2/src/Configuration/WeightTestsNanoGen/0D365A43-653D-D243-B629-881614B3055E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/536650AD-25A6-2341-9164-13900DEF9770.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/83B21322-62AF-F649-AFC8-BD1B14130C7C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/7DF15745-C0E3-D947-8114-018966330587.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6D49E273-36B8-664D-B2F1-B74B4F234257.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/BA175A22-C4D9-0D49-A6F5-628C510CBDF1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/EEBF3148-4BAB-FF40-8553-3606ADA3BC6A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/EDB1BC63-F7F0-B34D-BD8A-429AD40E6E1B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/60C95D04-CC00-9445-B7B2-10B14EA1B2D7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/D279782F-102B-E34B-9D71-22EA590C977A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/118C45EB-63D3-2D4C-BB77-A87112D1D4D8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/57D75D2D-2EF4-DD48-AEA5-CB886C57DA11.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/25874002-3C86-0B40-B973-9F79DF79C8DD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/D23E26DB-A58C-F54D-8D0A-C3C7366195D4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/52F95250-77AE-FA4E-BD8E-DF9F463E0A30.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4EB0DD31-AC05-DC42-9047-70016E2FEA18.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/649BA145-4C89-5A4A-8118-A34CA009571A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/7A57B57D-55A8-374F-BD21-F7C2ECCF6E56.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/EAA11919-EF00-0C4B-97B7-186910E44D21.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A9BFF97E-10EF-044B-851F-953886F3CBC4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4085EFBD-8A9D-BC43-A3CB-3138CC2948A8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6136B63B-65E6-604F-B753-2761992E0BED.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8278199D-F000-A24F-AD9B-E254ACBCDCA9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/81EEF006-95CE-534F-A7F4-20E6912D38B4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/70863341-FE8B-C04A-A5DA-DAD231864979.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/28958819-1EA7-704A-A14D-DD83857967AC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/97E6B76A-5912-C14A-B20C-5A881DBADB42.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/11FEAE31-9183-C54E-B38E-4813E0701B25.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/3298CB5D-DBA5-6745-90BF-121BB4AF2659.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/973E92FF-9537-244E-AA8D-F415DFFBC6DA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0C6A478D-DCC0-CA40-9D59-BBDB7AE91CD7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FC83CE89-AA73-C347-AF21-888C3D091CA9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DA84225F-89D3-B24A-9AB9-8BFAB4E79C8B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/99F63B9C-AA33-5942-8849-B97B06793066.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/394CB744-FB0E-B549-91FF-B9BDC69739AC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/08986B2F-7F2E-2346-9899-DE514254BAC9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DEFC5EB4-87F7-BD49-A0FB-D9C01278DE1D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/276AA5D9-DA8B-3949-A849-7D412CD32418.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C079D587-669B-8140-B640-4A306DD53BE2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/24B69C49-D4B5-6940-BA40-1809BC309AC4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6FF928DA-2332-0B4A-B606-DD51751A2B19.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/5E728ED4-71A7-2348-B97E-E312D65EF6C7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2BAB4E46-FCC2-4F47-A4EF-3BE7A9589BFF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4BE1951A-7C7C-2F46-AAEE-E515258D58E4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/AD227B5D-7CCE-4144-9C8C-A79325CAB435.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/08D47B7B-D108-1D4D-A615-BFD959580E43.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/58B5DD83-98C1-BF4C-AA38-CC78DC358DF9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E69BDF3B-A378-5044-8788-309917A50908.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/F8B0F635-CEE5-D245-9A42-7FDA98C9C818.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/C05D6414-C9C6-124B-BED6-DCCD12811AAA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/3079D94C-D026-5C48-95C5-5AD0921CAD13.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/ECC90F43-9BA9-154D-9EE5-048217CE3397.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/7BAEF847-86D5-2D46-9DC0-60E6E212C6B9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/84EDCAC4-AE86-EB4D-AF77-DCDA94F87CC0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E265CB99-0B50-0447-91C9-479E76089F21.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2556804A-987B-1C46-84EE-23BA7B44E658.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/04A33B5B-FDFF-6544-9AD1-F0E5AB1835E1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/5417FAE3-8A39-5348-ACBD-12458DE52979.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/CC6353B3-761C-E646-A750-315711424641.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/1E4978B4-DEEF-2C4D-8F8A-C2658B904AE8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/56D98B55-8AF9-BD4B-AF97-699CD3F518A7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9BFB3D66-DEE4-3548-ABA8-F988036C5330.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/95C36D3F-1BF7-A741-9266-03A5A554FA3F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DB22E91A-7291-3248-ACA4-E232E1995B93.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6303DB9C-4F06-B347-892D-C6BA18850671.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/17D66FDF-59CA-4648-B9D3-4B2B8B0777C6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/AA547CA6-2724-104F-9720-1FE93643B814.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/BE1A0E1B-50DC-8449-9A98-73C90EEEC2F5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E0751B00-F59C-6246-BA7F-CC17F4F2C4B4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/13BA0FE7-DFCB-B541-913D-4CC16658C3A8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E062D5CB-8392-F542-A8D0-DB9FF4688718.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/F5A0ABBA-348B-4640-B672-7FFB365D0931.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0F167A53-1F32-E04F-B856-D6B2B1ADBCE3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/D0D3240F-6ACD-0D42-BFB8-AAD952C9E407.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9B84F77A-B7DD-874D-AD77-F7734FC76E13.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/EF185314-EFB8-B745-BD7F-91D8427E0CD4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/019DDBEA-83EE-A042-BCA7-BC7B265A0EFF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/70A7EA60-CA48-FF41-A210-4D9A5A94DACC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9D5E87BB-5936-7B43-B0A5-EC91919976FE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6C08256B-2ED5-8642-B8CC-8190FA653413.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/95378FB7-46DB-BF41-9176-889041788F8C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/AE629410-B549-C048-8012-BD1F5E41B319.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/D7532451-6D06-4D44-8B04-DAC50E7DE983.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DF740BD6-BA19-314F-BA31-E9C9D6F4B27D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E2A9B4F6-8E49-5945-A633-BC47EDF4FFB5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/7526BECF-21BB-3340-8B3A-37E63F163BF7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/60975E54-C67C-9248-95F5-85B6D29B0007.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/43C0D775-5898-A847-906D-5B0AE9B56C03.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/281D2CF9-147E-4048-BB65-9510EED820C8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4C09E2E2-6F6D-244F-B3C6-BDAB25DE4698.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C0F82343-5570-0D4D-8780-3AF37F8DE8E0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/CCE57EDF-6FAE-8B43-9FDC-4BA4979E080C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/BFF88B8E-9AAB-F747-BF1D-11D311B8904E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9A5DF363-F5BD-F146-9802-305742792135.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A0440B25-D03D-9A41-A7CB-803DE339CE35.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/49E1FBA9-5B48-8842-A186-6DD36696F50A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FF696952-0391-FF41-BC14-54B62F74011D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6BEE7DBF-5A0F-8745-A1FB-BE50913D3333.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/17D36030-A584-8443-AD9D-B938F8D9559C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DFF8C227-B424-6642-8680-6A10FC76AA90.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0A7A2F6A-1C0C-C447-9C0C-19E5707D3BCC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/F80C5F57-84E4-2C41-A61D-B82D2EC6F8FD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6BFF5DE7-C63F-054E-A9E2-63DDE8A0DAFF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A0256A5A-2AA0-E740-9CCE-0201D789F38A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6D3B9DB0-32D4-9349-B169-A7C50DD9507D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8A76EF69-6600-A54D-80F6-DEACA6913F17.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/629ADDCA-A7CB-0740-9999-EDE5552754D7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/3AD2BA17-5F2B-544B-AE29-7D280A51258D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C36360A7-6228-2C40-AFB1-9259A1035CB3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B0EF633D-D6F9-6E4D-A2A8-2B1363ADB1C3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/62D67DBE-1A98-B144-B81A-F33DCB0CB83F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/464C4FEB-5182-FF43-B8C9-0D183D06C81D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/543EE38A-7B43-2848-BDD2-581B540ACB6E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/806A4BB6-35BC-1144-AB5A-C79F17528E53.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6ACB081C-7ACE-E24D-9E42-812E58CBA94B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B3E48387-BDB3-1B43-A646-242CB28960FA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/506CCEA5-48F0-AD43-90E5-4A6F96ED9409.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6F26C0C6-FC8B-4D4C-8559-0159379505DD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/5E8DDA8A-A3F5-FC4C-AB62-BC5677883655.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/3900613A-E1BC-2C4A-957C-16B0D2B410A4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/93DE4536-EE3A-C645-9FDF-4C39507E8F32.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2D735545-E64B-8940-B8FC-1DE76A39BC07.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4C47BE15-6212-B045-BE64-31BE5EC00E0B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2D379B43-80A2-A44C-BB03-ED65798A61BE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E63B40D2-AE9F-6646-8742-E79E82BED0F6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/339CC00C-F6C2-C54C-B26C-C63CFD8D458D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/40D87628-C4CC-2D44-B9C7-3F97806EC713.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/068491CC-F700-424D-8F15-5AA835A6B24E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/15567BD9-5E80-1343-9096-25AB7039DD06.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/233EFC6A-DF1C-B541-B5C5-C5548B75D3C7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/A19ECADC-95BA-644D-A0C2-228E7A2A9C68.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/08501FA9-E179-174C-B9CE-7D67182EF6B4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/25B81580-96EA-9748-A3B2-62BE663EAB66.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/25C3838E-5496-AA43-8E7A-5D1961CD095F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8C6EDC39-B6EB-7544-93C2-476F79E81135.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/EE6EBA44-E565-B946-93D9-958BBF2EFD64.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/ABF24E27-081E-E346-B250-9B2553ADB543.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2A08977B-E6AB-E94A-AF1F-6BDA7A0D12DD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/189FA65A-B05B-D74E-8908-09EEF0632C5C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/DACB919F-A52D-E34A-913D-A8EADE0D7B6F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/F749AB0E-6D23-F440-BDB9-C0D1342082FE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/30AD5EB6-161A-B441-8163-0DC7F05B2297.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/542E6B4D-DD5C-8E4A-B90C-1959EE31A16D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2F486DB6-ADAB-814A-991E-C9E49120528F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/63E84237-E672-B947-BBF5-965920ECA666.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A9A35B00-B69F-CC4D-9A64-C1F1DFDBCB9C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/5A8ED051-D640-5F41-9E3F-0EB6BC123483.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/90F2FAE0-E989-444C-8F14-66E2F328A377.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A2051DFF-9894-4D4A-B2BA-51A96A181A4D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/8CFFEF27-2ADD-C641-9ECC-ED62B7C20A8E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A4D2795D-CF26-F446-88CA-3C4577E4E218.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E4FC23A6-357E-B34E-8E9D-0395610BBC65.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E458B9C1-8691-0349-9C19-1BAA0E7CAB42.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/04550ECA-2D78-C446-92F2-8A038F334236.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/721BEC5B-5CE1-254D-8176-5D0220EEBCE9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8318DF03-EEFD-1F4C-B555-08EA28F4EF9E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/238B8A6E-4C78-114B-A348-AB3021373346.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9C0BB4A5-A2DC-4C40-A0F1-260A0D2ACA1A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0E9587C5-7AF5-CC46-AC90-9988D22CBCE9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/29072632-8429-7949-B471-0A5D5DA680AC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/CFCC9D73-9BDB-7442-AB49-9F137595E29F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/E916F232-A048-6D48-AC49-09ACD7EA33FE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/178E6B26-5258-1F4B-A055-6D07A6E5087C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/721D03C9-CB3C-DD42-B6DA-F2E970AE4165.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0F476C51-B44E-0C4F-B751-7206563C0EF7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0BC58025-E24C-4841-A33A-CCE52401F182.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/AFD9D978-CB2C-C645-8ACF-B85E1FEA0CEA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/7087052C-E6D0-6C4C-89DD-30D4D808216E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/023559E6-14DA-5A41-A3D3-ABA8EC839056.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A002FEA4-9780-A947-9E89-F23D107F8A9F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/5F2293F6-F2C9-844C-B7DA-F186C4435005.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4477FB2E-1A47-564C-807B-300C8B5758C2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/07BF418B-47F2-C741-9D7C-6A3B535C3066.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/070FC9B7-F58F-C744-9B5C-DAF8A9BB6251.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/4DA63040-9064-CB44-963A-84ACDC89644B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8D79B195-A2A7-AA4A-932E-3690CE9BF365.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DB8CA6B6-4AA0-B74E-93B9-AA5EAE9A2CEA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E388AD08-68FB-ED48-8F22-18F9B1A44D11.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/85075D4D-1DB9-EA43-BE4C-DF76FD644EB3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FED25E5B-1B99-9041-B020-CE6F6C9D2658.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FA759D75-EDF1-BB43-8358-2D505D15E0D5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FFCB7843-87C8-9940-881E-66BEDD3C6A99.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0226C663-CC5B-DA41-A9DB-D786BB18E20E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/836A08AD-2647-3C42-BFD0-0BEE9F2C2DFC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/AAABC466-AAE2-774F-9E68-494970E4C442.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/AC2F978B-0AFC-7C4C-B8A3-82D1D502E27C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DCB56CD1-52BC-E54E-914C-1B64BF995138.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FA53A33A-24EA-3049-8514-BED6374BABC7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/43F46E12-0C41-F048-A281-E3B1FFEA279F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/26BEDC2A-8BE1-7E47-BA26-E00DF85F7E70.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C9FD3144-9BF5-FE4B-BD62-4A67E767F623.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/67B8B0FB-795B-3247-89FD-7AACB5DA1587.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/240EDB63-CD3B-874E-8752-44AAEA70DC1F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/AB5F971D-6F85-5E46-BB65-8EE65EABA5E6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/32220880-1CA6-9942-8C9B-EDC2680AFDC2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/9220D7A3-97C6-B64F-87F5-C6F0A551B16A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/3F591447-BF7E-A346-A97E-E42A5941AED6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/A7409C11-6D16-6440-8A1C-775C20212965.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/F694FF7F-6685-AC4B-BA55-897A0C5C85A7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/A8ABBD88-D4B7-AB4C-8CF4-3A4C1D1F7B14.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/5CC42C83-4D53-EB48-9BC5-9F2DBD3F17EB.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/C499EC45-37A4-1940-9CBE-275BFABD0719.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/800B2C9D-F29F-7A45-B9AB-33E9AF4F3413.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/40CB39E8-AFB8-D847-B42C-567E9553553F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/0DAE5E67-52E1-5546-8442-C89272743064.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/D3974688-7934-A742-80B3-AE3384CDF4AD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/43D385B4-BB24-9A46-AE46-6E12824F4FCA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/38528D44-ADD2-C043-A2E7-C05FD7C53B3F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/EBFB9E7F-544D-3047-9CA2-5A2A0C838511.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/FEB4DC29-BEFB-9040-9CD8-DE30EDDBAD2D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/9A8B607B-F116-3D4A-8DB1-6626573F1A49.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/08C10064-4535-4B43-A262-E8AD8BE38C30.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/FEFFAE6D-50E5-4C48-924A-E0B223EE0BC8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/17BB2B21-3DF4-3241-AFF5-34B6AED5E09C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9570A7FF-BABC-D647-92BE-18043963529E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B2A8E48A-A122-E44C-9976-03E1DD081B22.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/038684CF-115D-C745-BF1E-104C6451B416.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/3A626DB7-D342-B740-9380-38CD48943DE2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/D68B8F19-42D1-D147-9EAB-384D90C24907.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/86644058-EED1-2D41-947D-E04ED06A26BA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/F466C785-27DD-C746-BCBE-66ED6EE6DBC6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/0DFD1791-0458-9F4E-8E0E-1B88B90C2B60.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/63FA3357-67DB-8A44-8348-D420BAEFB88F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/C3807E5B-B859-514B-9992-7907F6270567.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/5049B934-E253-3542-88F3-407C0CB0E974.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/CFD5D148-FCA3-474F-9ADB-5168459C4E94.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/650BF813-4687-4C4D-9AF3-187B157DB854.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B36DC095-083F-504B-8D3E-D6B733394982.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/BEF51F36-E040-C744-B245-AA00F550C361.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/309A1458-418D-384D-B479-7A0D2A251493.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C3175EB3-F017-8F45-B992-6DCE6D3DD6D1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/3A8EF788-2199-B741-8119-6EB6E1A91DAE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DA0FD957-F547-E844-8F64-46E351FA6E47.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9777F062-547B-8D4A-B0E0-8D87FB223FB1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/84FA72AC-C4AC-354D-BB08-E200FBC70647.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B8CE0E90-4C87-6B42-B320-258E144FB240.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B7A647FE-7525-444F-992A-36D0A6DED5A1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8E4B358B-1CDA-7F43-A011-199D4E45EB9F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/069DA916-033E-5C44-8294-35A0F677683F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C39D56B0-2FBB-374A-B868-89C10036807F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/092EFB9E-4E2A-9549-9218-42ED5DBBB8F8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B168D3A4-CD5A-E24C-8ECA-9810C7E4C541.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C8CC5E65-551A-254A-ADE6-02565F93334E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E12B9CCF-46A9-3A47-8D29-91CFB7A667DF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/995BEBE0-C109-3341-BCC4-BDCBAD9381B5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8CD2F714-3B55-B948-84DF-FD00BAB05963.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/55706DAC-2EE8-0E4B-9FEC-EC35DC9A05B4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/CFAE81B6-288F-0D4A-B756-BCAA4AF9B120.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/0D8EB2F7-4176-4F43-8F66-44759B6D5BF9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A52876E1-2AC7-4740-BD08-6D1E63CFF00C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/8E7E0FC3-E5FD-F943-A21C-490CB945C7D5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/42E36F5B-1174-3442-8F1D-BF2F65728EE5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/AF0B8A44-883A-4C4F-85BC-9803E2C3EC82.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/158D935E-D05F-8946-AF70-1754A6E9E271.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E6DA8618-3BB0-F848-A77F-28BAB4E722DD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6676F51E-A973-9141-AB8A-A9F266EDF1A9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/15967E2E-35D0-3E40-A41C-C339EA498A6C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/77032894-2ABF-E845-82F1-941422182B36.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/828E2B68-771A-E842-B218-1B7DDCF900A4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/3A2B6664-1D95-A842-A3E9-0FF518B3C1F7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/4E9D4CDF-097E-5B47-81B7-48E5D964FCDC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/02A3537C-8FD7-1249-B74E-B1B093F53C34.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/3E104CB4-DD1B-4D4E-8B9B-0433C799E6D2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/096C82DA-0F15-E140-B700-629E888CD60F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/1A45D56D-CCB0-0A46-B1AD-16D464315802.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/7C0E70F2-F9C7-2A45-8FB3-D3324DB9A231.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/2F4D601B-B737-474A-89CC-36267ED6BB0D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/D33994CD-F6A8-CE47-B1C0-6E0D2517EA9D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/AD904DE3-EC2A-744E-97DA-EE3DE3B9E230.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/14105E08-1C86-E549-9CB4-DA97715CEDEF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/826D16F7-26B7-6443-BBC6-932640C59702.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/8DD10E29-0EF9-544F-9318-4754C30D254F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/62B6C216-3867-3F4A-8CEE-61D1E065C5E2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/D1280D7B-2367-454C-98A5-C01DF80E4CFE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/7EF53FB1-F39E-1345-8FE4-9CA2CBAC8D4F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/E815EDFC-5E13-AD4A-A199-0517EEB4245C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/32CF8414-4D10-2D45-86CE-700C761D54A0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/A9159B87-6103-3A48-9E09-34A3D9B8ACFA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/A1D59C04-3FC2-674B-A374-E25F16F091C4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/C471AC36-2C82-F24D-8F69-79E368CAEF8A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/906C08DD-1436-6A40-9A67-1DFD565F4D3D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/4E44139C-80D8-DF45-B819-13F26943E99D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/81D9CDB1-EC4B-3244-A514-9113AF2C4673.root', 
        '/store/mc/RunIIAutumn18MiniAOD/ZZTo4L_13TeV_powheg_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/52FE5169-54DF-5145-A188-D9F5BF024C5D.root'
     ) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODGENoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('ZTo4L_13TeV_powheg_pythia8_TuneCP5.root'),
    outputCommands = process.NANOAODGENEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mcRun2_asymptotic_v7', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanogenMiniSequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODGENoutput_step = cms.EndPath(process.NANOAODGENoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODGENoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nanogen_cff
from PhysicsTools.NanoAOD.nanogen_cff import customizeNanoGENFromMini 

#call to customisation function customizeNanoGENFromMini imported from PhysicsTools.NanoAOD.nanogen_cff
process = customizeNanoGENFromMini(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.lheWeights.failIfInvalidXML=False
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
