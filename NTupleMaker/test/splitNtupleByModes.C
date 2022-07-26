
// Macro to split ntuples by mode
#include "EMTFAnalyzer/NTupleMaker/interface/Read_FlatNtuple.h"
// #include "EMTFAnalyzer/NTupleMaker/plugins/FlatNtuple.h"
#include <vector>


const bool verbose = false;
const int MAX_EVT = -1;  // Max number of events to process
const int PRT_EVT = 10000;   // Print every N events


const TString in_dir = "/eos/cms/store/user/eyigitba/emtf/L1Ntuples/Run3/crabOut/SingleMu/SingleMuFlatOneOverPt1To1000GeV_combined/";
const TString in_file = "EMTFNtuple_hadded_negEndcap_v1_4";

const TString in_dir_file = in_dir + in_file + ".root";

const int mode = 15;

const TString out_dir = "/eos/cms/store/user/eyigitba/emtf/L1Ntuples/Run3/crabOut/SingleMu/SingleMuFlatOneOverPt1To1000GeV_combined/modeSplit/run2/";

TString STR(int x) { return std::to_string(x); }
TString STR(float x) { 
  std::ostringstream out;
  out << std::setprecision(2) << x;
  return out.str();
}


// Main function to make efficiency turn-on plots
void splitNtupleByModes() {

  TFile* input_file = new TFile(in_dir_file);
  TTree *in_tree_run2; input_file->GetObject("FlatNtupleMCRun2/tree",in_tree_run2);
  TTree *in_tree_run2_GEM; input_file->GetObject("FlatNtupleMCRun2GEM/tree",in_tree_run2_GEM);
  TTree *in_tree_run3; input_file->GetObject("FlatNtupleMCRun3/tree",in_tree_run3);
  TTree *in_tree_run3_GEM; input_file->GetObject("FlatNtupleMCRun3GEM/tree",in_tree_run3_GEM);

  TFile* out_mode_3 = new TFile(out_dir + in_file + "_mode_3.root", "RECREATE");
  TFile* out_mode_5 = new TFile(out_dir + in_file + "_mode_5.root", "RECREATE");
  TFile* out_mode_6 = new TFile(out_dir + in_file + "_mode_6.root", "RECREATE");
  TFile* out_mode_7 = new TFile(out_dir + in_file + "_mode_7.root", "RECREATE");
  TFile* out_mode_9 = new TFile(out_dir + in_file + "_mode_9.root", "RECREATE");
  TFile* out_mode_10 = new TFile(out_dir + in_file + "_mode_10.root", "RECREATE");
  TFile* out_mode_11 = new TFile(out_dir + in_file + "_mode_11.root", "RECREATE");
  TFile* out_mode_12 = new TFile(out_dir + in_file + "_mode_12.root", "RECREATE");
  TFile* out_mode_13 = new TFile(out_dir + in_file + "_mode_13.root", "RECREATE");
  TFile* out_mode_14 = new TFile(out_dir + in_file + "_mode_14.root", "RECREATE");
  TFile* out_mode_15 = new TFile(out_dir + in_file + "_mode_15.root", "RECREATE");

  // out_mode_15->cd();
  // TDirectory* run2 = out_mode_15->mkdir("FlatNtupleMCRun2");
  // TDirectory* run2GEM = out_mode_15->mkdir("FlatNtupleMCRun2GEM");
  // TDirectory* run3 = out_mode_15->mkdir("FlatNtupleMCRun3");
  // TDirectory* run3GEM = out_mode_15->mkdir("FlatNtupleMCRun3GEM");
  out_mode_15->cd();
  TTree *tree_run2_mode_15 = in_tree_run2->CloneTree(0);
  out_mode_14->cd();
  TTree *tree_run2_mode_14 = in_tree_run2->CloneTree(0);
  out_mode_13->cd();
  TTree *tree_run2_mode_13 = in_tree_run2->CloneTree(0);
  out_mode_12->cd();
  TTree *tree_run2_mode_12 = in_tree_run2->CloneTree(0);
  out_mode_11->cd();
  TTree *tree_run2_mode_11 = in_tree_run2->CloneTree(0);
  out_mode_10->cd();
  TTree *tree_run2_mode_10 = in_tree_run2->CloneTree(0);
  out_mode_9->cd();
  TTree *tree_run2_mode_9 = in_tree_run2->CloneTree(0);
  out_mode_7->cd();
  TTree *tree_run2_mode_7 = in_tree_run2->CloneTree(0);
  out_mode_6->cd();
  TTree *tree_run2_mode_6 = in_tree_run2->CloneTree(0);
  out_mode_5->cd();
  TTree *tree_run2_mode_5 = in_tree_run2->CloneTree(0);
  out_mode_3->cd();
  TTree *tree_run2_mode_3 = in_tree_run2->CloneTree(0);
  // tree_run2_mode_15->SetDirectory(run2);

  // TTree *tree_run2_GEM_mode_15 = in_tree_run2_GEM->CloneTree(0);
  // tree_run2_GEM_mode_15->SetDirectory(run2GEM);

  // TTree *tree_run3_mode_15 = in_tree_run3->CloneTree(0);
  // tree_run3_mode_15->SetDirectory(run3);

  // TTree *tree_run3_GEM_mode_15 = in_tree_run3_GEM->CloneTree(0);
  // tree_run3_GEM_mode_15->SetDirectory(run3GEM);

  InitializeMaps();
  SetBranchAddresses(in_tree_run2);

  std::cout << "Initialized branches" << std::endl;
  std::cout << "Reading " << in_tree_run2->GetEntries() << " events" << std::endl;

  for (int i=0; i<in_tree_run2->GetEntries(); i++){
  // for (int i=0; i<200000; i++){
    if ( i % 10000 == 0) std::cout << "event: " << i << std::endl;
    in_tree_run2->GetEntry(i);
    if (I("nTracks") == 0) continue;
    bool isMode15 = false;
    bool isMode14 = false;
    bool isMode13 = false;
    bool isMode12 = false;
    bool isMode11 = false;
    bool isMode10 = false;
    bool isMode9 = false;
    bool isMode7 = false;
    bool isMode6 = false;
    bool isMode5 = false;
    bool isMode3 = false;
    for (int iMu = 0; iMu < I("nTracks"); iMu++){
      if (I("trk_mode",iMu) == 15)   isMode15 = true;
      if (I("trk_mode",iMu) == 14)   isMode14 = true;
      if (I("trk_mode",iMu) == 13)   isMode13 = true;
      if (I("trk_mode",iMu) == 12)   isMode12 = true;
      if (I("trk_mode",iMu) == 11)   isMode11 = true;
      if (I("trk_mode",iMu) == 10)   isMode10 = true;
      if (I("trk_mode",iMu) == 9)    isMode9 = true;
      if (I("trk_mode",iMu) == 7)    isMode7 = true;
      if (I("trk_mode",iMu) == 6)    isMode6 = true;
      if (I("trk_mode",iMu) == 5)    isMode5 = true;
      if (I("trk_mode",iMu) == 3)    isMode3 = true;

    }
    if (!isMode13) continue;
    if (isMode15) {
        tree_run2_mode_15->Fill();
    }
    if (isMode14) {
        tree_run2_mode_14->Fill();
    }
    if (isMode13) {
        tree_run2_mode_13->Fill();
    }
    if (isMode12) {
        tree_run2_mode_12->Fill();
    }
    if (isMode11) {
        tree_run2_mode_11->Fill();
    }
    if (isMode10) {
        tree_run2_mode_10->Fill();
    }
    if (isMode9) {
        tree_run2_mode_9->Fill();
    }
    if (isMode7) {
        tree_run2_mode_7->Fill();
    }
    if (isMode6) {
        tree_run2_mode_6->Fill();
    }
    if (isMode5) {
        tree_run2_mode_5->Fill();
    }
    if (isMode3) {
        tree_run2_mode_3->Fill();
    }

  }
  out_mode_15->cd();
  tree_run2_mode_15->Write();
  out_mode_15->Close();

  out_mode_14->cd();
  tree_run2_mode_14->Write();
  out_mode_14->Close();

  out_mode_13->cd();
  tree_run2_mode_13->Write();
  out_mode_13->Close();

  out_mode_12->cd();
  tree_run2_mode_12->Write();
  out_mode_12->Close();

  out_mode_11->cd();
  tree_run2_mode_11->Write();
  out_mode_11->Close();

  out_mode_10->cd();
  tree_run2_mode_10->Write();
  out_mode_10->Close();

  out_mode_9->cd();
  tree_run2_mode_9->Write();
  out_mode_9->Close();

  out_mode_7->cd();
  tree_run2_mode_7->Write();
  out_mode_7->Close();

  out_mode_6->cd();
  tree_run2_mode_6->Write();
  out_mode_6->Close();

  out_mode_5->cd();
  tree_run2_mode_5->Write();
  out_mode_5->Close();

  out_mode_3->cd();
  tree_run2_mode_3->Write();
  out_mode_3->Close();

} // End function: void