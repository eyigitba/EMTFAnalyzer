import FWCore.ParameterSet.Config as cms

from EMTFAnalyzer.NTupleMaker.GEMEMTFMatcher_cfi import *
from EMTFAnalyzer.NTupleMaker.FlatNtuple_cfi import *

def add_analyzers_without_GEM_matching(process):

    ## collections, run 4 ntuplizers:
    ##   Run-2
    ##   Run-2 + GEM (ILT on)
    ##   Run-3 (CCLUT on)
    ##   Run-3 + GEM (CCLUT and ILT on)

    ##   Run-2
    FlatNtupleMCRun2 = FlatNtupleMC.clone()
    FlatNtupleMCRun2.emtfHitTag = cms.InputTag("simEmtfDigis")
    FlatNtupleMCRun2.emtfTrackTag = cms.InputTag("simEmtfDigis")

    ##   Run-2 + GEM
    FlatNtupleMCRun2GEM = FlatNtupleMC.clone()
    FlatNtupleMCRun2GEM.emtfHitTag = cms.InputTag("simEmtfDigisILT")
    FlatNtupleMCRun2GEM.emtfTrackTag = cms.InputTag("simEmtfDigisILT")`

    ##   Run-3
    FlatNtupleMCRun3.emtfHitTag = cms.InputTag("simEmtfDigisILTCCLUT")
    FlatNtupleMCRun3.emtfTrackTag = cms.InputTag("simEmtfDigisILTCCLUT")

    ##   Run-3 + GEM
    FlatNtupleMCRun3GEM = FlatNtupleMC.clone()
    FlatNtupleMCRun3GEM.emtfHitTag = cms.InputTag("simEmtfDigisRun3CCLUTILT")
    FlatNtupleMCRun3GEM.emtfTrackTag = cms.InputTag("simEmtfDigisRun3CCLUTILT")

    EMTFAnalyzers = cms.Sequence(
        FlatNtupleMCRun2 *
        FlatNtupleMCRun2GEM *
        FlatNtupleMCRun3 *
        FlatNtupleMCRun3GEM
    )

    process.Analysis_step = cms.Path(
        process.EMTFAnalyzers
    )
    return process

def add_analyzers_with_GEM_matching(process):

    ## pick up the right GEM copad collection
    GEMEMTFMatcher.gemCoPadTag = cms.InputTag("simCscTriggerPrimitiveDigisILT","","DIGI")

    ## Run-2 matcher
    GEMEMTFMatcherMCRun2 = GEMEMTFMatcher.clone()
    GEMEMTFMatcherMCRun2.emtfHitTag = cms.InputTag("simEmtfDigis")
    GEMEMTFMatcherMCRun2.emtfTrackTag = cms.InputTag("simEmtfDigis")

    ## Run-3 matcher
    GEMEMTFMatcher.emtfHitTag = cms.InputTag("simEmtfDigisRun3CCLUT")
    GEMEMTFMatcher.emtfTrackTag = cms.InputTag("simEmtfDigisRun3CCLUT")

    ## to be sure that the GEMEMTFMatcher is not screwing up any of the existing EMTFHit or EMTFTrack
    ## collections, run 4 ntuplizers:
    ##   Run-2
    ##   Run-2 + GEM
    ##   Run-3
    ##   Run-3 + GEM

    ##   Run-2
    FlatNtupleMCRun2 = FlatNtupleMC.clone()
    FlatNtupleMCRun2.emtfHitTag = cms.InputTag("simEmtfDigis")
    FlatNtupleMCRun2.emtfTrackTag = cms.InputTag("simEmtfDigis")

    ##   Run-2 + GEM
    FlatNtupleMCRun2GEM = FlatNtupleMC.clone()
    FlatNtupleMCRun2GEM.emtfHitTag = cms.InputTag("GEMEMTFMatcherMCRun2")
    FlatNtupleMCRun2GEM.emtfTrackTag = cms.InputTag("GEMEMTFMatcherMCRun2")

    ##   Run-3
    FlatNtupleMCRun3.emtfHitTag = cms.InputTag("simEmtfDigisRun3CCLUT")
    FlatNtupleMCRun3.emtfTrackTag = cms.InputTag("simEmtfDigisRun3CCLUT")

    ##   Run-3 + GEM
    FlatNtupleMCRun3GEM = FlatNtupleMC.clone()
    FlatNtupleMCRun3GEM.emtfHitTag = cms.InputTag("GEMEMTFMatcher")
    FlatNtupleMCRun3GEM.emtfTrackTag = cms.InputTag("GEMEMTFMatcher")

    GEMEMTFMatchers = cms.Sequence(
        GEMEMTFMatcherMCRun2 *
        GEMEMTFMatcher
    )

    EMTFAnalyzers = cms.Sequence(
        FlatNtupleMCRun2 *
        FlatNtupleMCRun2GEM *
        FlatNtupleMCRun3 *
        FlatNtupleMCRun3GEM
    )

    process.Analysis_step = cms.Path(
        process.GEMEMTFMatchers *
        process.EMTFAnalyzers
    )
    return process
