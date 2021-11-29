# EMTFAnalyzer
Analysis tools for EMTF. 

## Setup
The EMTFAnalyzer is designed to run on `lxplus`, uses crab for job submissions, and pulls input files from EOS. The version of CMSSW is critical since trigger primitives and other aspects of the EMTF will change. 
```
cmsrel CMSSW_12_1_0_pre3
cd CMSSW_12_1_0_pre3/src/
cmsenv
git cms-init
git cms-rebase-topic dildick:CMSSW_12_1_X-EMTF-CCLUT
git clone git@github.com:dildick/EMTFAnalyzer.git
scram b -j 4
```

## Structure
The EMTFAnalyzer repository has two main directories, `AWBTools` which has not been kept upto date, and `NTupleMaker` which is used for Run3 BDT Training Preperation. `NTupleMaker` is then divided into `crab`, `src`, `python`, and `test`.

The `crab` directory has not been kept upto date and most scripts have been replaced by scripts in `test`. 

In the `src` directory are Branch and Matcher helper classes. 

In the `python` directory are the actual NTuple process definitions. 

In the `test` directory are where the crab configurations and PSets are for the jobs.

## Steps for Generating NTuples
1.) The first step to generating NTuples for BDT Training is to generate a MC sample. This is done using `NTupleMaker/test/crab_SingleMuFlatOneOverPt1To1000GeV_GEN_SIM.py` which will get saved to EOS - this step is only the generation and simuluation of the MC. 

2.) The second step is to run the emulation of this MC Sample to digitization and trigger primitives is done using `NTupleMaker/test/step2_DIGI_L1.py` which will also be saved to EOS.

3.) Then the third step is to run the NTuplization step which will generate NTuples based on `NTupleMake/python/FlatNtuple_cff.py` and will be sent to crab using `NTupleMaker/test/Run3_MC_NTuple.py`.

4.) Lastly, these NTuples need to be hadded together to be used as input into the BDT. 
