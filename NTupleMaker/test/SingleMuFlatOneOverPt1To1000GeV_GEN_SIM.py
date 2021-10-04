# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: Configuration/Generator/python/SingleMuPt10_pythia8_cfi.py --fileout file:step1.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions auto:phase1_2021_realistic --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM --geometry DB:Extended --era Run3 --python_filename SingleMu_GEN_SIM.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('SIM',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRun3RoundOptics25ns13TeVLowSigmaZ_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('GEMCode.GEMValidation.randomizeMuonGun')
process.load('Configuration.Generator.SingleMuFlatLogPt_100MeVto2TeV_cfi')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/Generator/python/SingleMuFlatLogPt_100MeVto2TeV_cfi nevts:10'),
    #annotation = cms.untracked.string('step1 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

process.generator = cms.EDProducer("FlatRandomOneOverPtGunProducer",

    PGunParameters = cms.PSet(
        # This specifies range in 1/Pt
        # It coresponds to Pt = 1 to 1000 GeV
        MinOneOverPt = cms.double(0.001),
        MaxOneOverPt = cms.double(1.),
        PartID = cms.vint32(-13),
        MaxEta = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359) ## in radians
    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('single mu pt 0.1to10'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)

## filter for gen level
process.genMuons = cms.EDFilter("PdgIdCandViewSelector",
                                src = cms.InputTag("genParticles"),
                                pdgId = cms.vint32(13, -13)
                            )

## filter for sim level
process.genMuonsCSC = cms.EDFilter("CandViewSelector",
                                   src = cms.InputTag("genMuons"),
                                   cut = cms.string("pt > 0.5 & abs(eta)<2.4 & abs(eta)>1.2"),
                                   filter = cms.bool(True)
                               )

## filter sequence
process.gen_mu_select = cms.Sequence(process.genMuons * process.genMuonsCSC)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)

## add the selections
process.generation_step += process.gen_mu_select
process.simulation_step += process.gen_mu_select

process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path).insert(0, process.generator)

process.options.numberOfThreads = cms.untracked.uint32(4)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
