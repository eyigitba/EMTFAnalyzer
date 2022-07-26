# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2.py --filein file:step1.root --fileout file:step2.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-L1 --conditions auto:phase1_2021_realistic --step DIGI:pdigi_valid,L1 --geometry DB:Extended --era Run3 --python_filename step2_DIGI_L1.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('DIGI',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source(
    "PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('root:///afs/cern.ch/user/e/eyigitba/L1T_dev/CMSSW_12_3_0_pre4_BDT/src/step1.root'),
    inputCommands = cms.untracked.vstring(
        'keep *',
#        'drop *_genParticles_*_*',
        'drop *_genParticlesForJets_*_*',
        'drop *_kt4GenJets_*_*',
        'drop *_kt6GenJets_*_*',
        'drop *_iterativeCone5GenJets_*_*',
        'drop *_ak4GenJets_*_*',
        'drop *_ak7GenJets_*_*',
        'drop *_ak8GenJets_*_*',
        'drop *_ak4GenJetsNoNu_*_*',
        'drop *_ak8GenJetsNoNu_*_*',
        'drop *_genCandidatesForMET_*_*',
        'drop *_genParticlesForMETAllVisible_*_*',
        'drop *_genMetCalo_*_*',
        'drop *_genMetCaloAndNonPrompt_*_*',
        'drop *_genMetTrue_*_*',
        'drop *_genMetIC5GenJs_*_*'
    ),
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
    numberOfThreads = cms.untracked.uint32(8),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-L1'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.FEVTDEBUGoutput.outputCommands.append('keep *_simCscTriggerPrimitiveDigis*_*_*')
process.FEVTDEBUGoutput.outputCommands.append('keep *_simEmtfDigis*_*_*')

from EMTFAnalyzer.NTupleMaker.cscTriggerCustoms import addCSCTriggerRun3
process = addCSCTriggerRun3(process)

from EMTFAnalyzer.NTupleMaker.sampleProductionCustoms import dropNonMuonCollections
process = dropNonMuonCollections(process)

## drop muon collections that are not used by the L1 step (CSC local trigger or EMTF), or the analysis step
process.FEVTDEBUGoutput.outputCommands.append('drop CSCDetIdCSCStripDigiMuonDigiCollection_simMuonCSCDigis_MuonCSCStripDigi_*')
process.FEVTDEBUGoutput.outputCommands.append('drop RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_RPCDigiSimLink_*')
process.FEVTDEBUGoutput.outputCommands.append('drop GEMDigiSimLinkedmDetSetVector_simMuonGEMDigis_GEM_*')
process.FEVTDEBUGoutput.outputCommands.append('drop StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_MuonCSCStripDigiSimLinks_*')
process.FEVTDEBUGoutput.outputCommands.append('drop StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_MuonCSCWireDigiSimLinks_*')
process.FEVTDEBUGoutput.outputCommands.append('drop PSimHits_g4SimHits_MuonCSCHits_SIM')
process.FEVTDEBUGoutput.outputCommands.append('drop edmRandomEngineStates_randomEngineStateProducer__SIM')
process.FEVTDEBUGoutput.outputCommands.append('drop edmRandomEngineStates_randomEngineStateProducer__DIGI')
process.FEVTDEBUGoutput.outputCommands.append('drop SimTracks_g4SimHits__SIM')
process.FEVTDEBUGoutput.outputCommands.append('drop SimVertexs_g4SimHits__SIM')

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(
    process.digitisation_step,
    process.L1simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line
process.options.numberOfThreads = cms.untracked.uint32(8)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
