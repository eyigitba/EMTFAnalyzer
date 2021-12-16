import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

options = VarParsing('analysis')
options.register("unpack", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when you want to unpack the CSC DAQ data.")
options.register("l1", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when you want to re-emulate the CSC trigger primitives.")
options.register("mc", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when running on MC.")
options.register("run3", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when using Run-3 data.")
options.register("runCCLUTOTMB", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when using the CCLUT OTMB algorithm.")
options.register("runCCLUTTMB", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when using the CCLUT TMB algorithm.")
options.register("runME11ILT", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when running the GEM-CSC integrated local trigger algorithm in ME1/1.")
options.register("runME21ILT", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True when running the GEM-CSC integrated local trigger algorithm in ME2/1.")
options.register("saveEdmOutput", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Set to True if you want to keep the EDM ROOT after unpacking and re-emulating.")
options.register("dropNonMuonCollections", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Option to drop most non-muon collections generally considered unnecessary for GEM/CSC analysis")
options.parseArguments()

process_era = Run3
if not options.run3:
      process_era = Run2_2018

process = cms.Process("L1CSCTPG", process_era)
process.load("Configuration/StandardSequences/GeometryRecoDB_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("EventFilter.CSCRawToDigi.cscUnpacker_cfi")
process.load('EventFilter.GEMRawToDigi.muonGEMDigis_cfi')
process.load("L1Trigger.L1TMuonEndCap.simEmtfDigis_cfi")
process.load('EventFilter.L1TRawToDigi.emtfStage2Digis_cfi')
process.load("L1Trigger.CSCTriggerPrimitives.cscTriggerPrimitiveDigis_cfi")
process.load("CalibMuon.CSCCalibration.CSCL1TPLookupTableEP_cff")
process.load('L1Trigger.L1TGEM.simGEMDigis_cff')

process.maxEvents = cms.untracked.PSet(
      input = cms.untracked.int32(options.maxEvents)
)

process.options = cms.untracked.PSet(
      SkipEvent = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source(
      "PoolSource",
      fileNames = cms.untracked.vstring(options.inputFiles),
      inputCommands = cms.untracked.vstring(
            'keep *',
            'drop CSCDetIdCSCShowerDigiMuonDigiCollection_simCscTriggerPrimitiveDigis_*_*'
      )
)

## global tag (data or MC, Run-2 or Run-3)
from Configuration.AlCa.GlobalTag import GlobalTag
if options.mc:
      process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
      if options.run3:
            process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')
else:
      process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
      if options.run3:
            process.GlobalTag = GlobalTag(process.GlobalTag, '112X_dataRun3_Prompt_v5', '')

## running on unpacked data, or after running the unpacker
if not options.mc or options.unpack:
      process.cscTriggerPrimitiveDigis.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
      process.cscTriggerPrimitiveDigis.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"

## l1 emulator
l1csc = process.cscTriggerPrimitiveDigis
l1emtf = process.simEmtfDigis
if options.l1:
      l1csc.commonParam.runCCLUT_OTMB = cms.bool(options.runCCLUTOTMB)
      l1csc.commonParam.runCCLUT_TMB = cms.bool(options.runCCLUTTMB)
      l1csc.commonParam.runME11ILT = options.runME11ILT
      l1csc.commonParam.runME21ILT = options.runME21ILT
      ## running on unpacked data, or after running the unpacker
      if (not options.mc or options.unpack):
            l1csc.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
            l1csc.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"
            ## GEM-CSC trigger enabled
            if options.runME11ILT or options.runME21ILT:
                  l1csc.GEMPadDigiClusterProducer = "muonCSCDigis:MuonGEMPadDigiCluster"

# Output
process.output = cms.OutputModule(
    "PoolOutputModule",
      outputCommands = cms.untracked.vstring(
            ['keep *',
             'drop *_rawDataCollector_*_*',
      ]),
      fileName = cms.untracked.string("lcts2.root"),
)

## for most studies, you don't need these collections.
## adjust as necessary
if options.dropNonMuonCollections:
      outputCom = process.output.outputCommands
      outputCom.append('drop *_rawDataCollector_*_*')
      outputCom.append('drop *_sim*al*_*_*')
      outputCom.append('drop *_hlt*al*_*_*')
      outputCom.append('drop *_g4SimHits_*al*_*')
      outputCom.append('drop *_simSi*_*_*')
      outputCom.append('drop *_hltSi*_*_*')
      outputCom.append('drop *_simBmtfDigis_*_*')
      outputCom.append('drop *_*_*BMTF*_*')
      outputCom.append('drop *_hltGtStage2ObjectMap_*_*')
      outputCom.append('drop *_simGtStage2Digis_*_*')
      outputCom.append('drop *_hltTriggerSummary*_*_*')

## schedule and path definition
process.unpacksequence = cms.Sequence(process.muonCSCDigis)
process.p1 = cms.Path(process.unpacksequence)

process.l1sequence = cms.Sequence(l1csc + l1emtf)
process.p2 = cms.Path(process.l1sequence)

process.p5 = cms.EndPath(process.output)
process.p6 = cms.EndPath(process.endOfProcess)

process.schedule = cms.Schedule()
## add the unpacker
if options.unpack:
      process.schedule.extend([process.p1])

## add the emulator
if options.l1:
      process.schedule.extend([process.p2])

if options.saveEdmOutput:
      process.schedule.extend([process.p5])

process.schedule.extend([process.p6])
