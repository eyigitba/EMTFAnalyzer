from CRABClient.UserUtilities import config
config = config()
config.General.requestName = 'SingleMuFlatOneOverPt1To1000GeV_DIGI_L1_v1'
config.General.transferLogs = True
config.General.transferOutputs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1.py'
config.JobType.allowUndistributedCMSSW = True
#10M OneOverPt 1-1000GeV NoPU
config.Data.inputDataset = '/SingleMu/dildick-SingleMuFlatOneOverPt1To1000GeV_GEN_SIM_v2-18f81f22971714352b1f31337d5920af/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
config.Site.storageSite = 'T3_US_FNALLPC'
config.JobType.numCores = 4
config.JobType.maxMemoryMB = 6000   #Use approx (1+1*ncores)GB
