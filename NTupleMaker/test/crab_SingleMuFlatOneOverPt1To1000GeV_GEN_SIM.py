from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMuFlatOneOverPt1To1000GeV_GEN_SIM_v1'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC' #'Analysis' #(If youhave an input dataset)
config.JobType.psetName = 'SingleMuFlatOneOverPt1To1000GeV_GEN_SIM.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 1
#config.JobType.maxMemoryMB = 3000   #Use approx (1+1*ncores)GB

#config.Data.inputDBS = 'global' #'phys03
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
config.Data.totalUnits = 100000000 # 50% will get filtered out
config.Data.publication = True
config.Data.outputPrimaryDataset = 'SingleMu'
config.Data.outputDatasetTag = config.General.requestName
config.Site.storageSite = 'T3_US_FNALLPC'
