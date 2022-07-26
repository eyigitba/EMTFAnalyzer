from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMuFlatOneOverPt1To1000GeV_Ntuple_fixed__negEndcap_v1'
config.General.workArea = 'logs'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC' #'Analysis' #(If youhave an input dataset)
config.JobType.psetName = 'EMTFAnalyzer/NTupleMaker/test/SingleMuFlatOneOverPt1To1000GeV_GEN_SIM_DIGI_Ntuple_neg.py'
config.JobType.outputFiles = ['EMTF_MC_NTuple_SingleMu.root'] ## Must be the same as the output file in process.TFileService in config.JobType.psetName python file
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 8000   #Use approx (1+1*ncores)GB

config.Data.useParent = False
config.Data.inputDBS = 'global' #'phys03
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000
config.Data.totalUnits = 100000000 # 50% will get filtered out
config.Data.publication = True
config.Data.outputPrimaryDataset = 'SingleMu'
config.Data.outputDatasetTag = config.General.requestName
config.Data.outLFNDirBase = '/store/user/eyigitba/emtf/L1Ntuples/Run3/crabOut/'


config.Site.storageSite = 'T2_CH_CERN'
