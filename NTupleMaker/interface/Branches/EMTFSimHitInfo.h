
#ifndef BranchesEMTFSimHitInfo_h
#define BranchesEMTFSimHitInfo_h

// Common branch info
#include "EMTFAnalyzer/NTupleMaker/interface/Branches/Common.h"

// Helpful tools
#include "EMTFAnalyzer/NTupleMaker/interface/HelperFunctions.h"

// EMTF classes
#include "DataFormats/L1TMuon/interface/EMTFHit.h"


//////////////////////////////
///  EMTF hit information  ///
//////////////////////////////
struct EMTFSimHitInfo {
  std::vector<TString> ints = {{"nSimHits", "nSimHitsCSC", "nSimHitsRPC", "nSimHitsBX0", "nSimHitsCSCBX0", "nSimHitsRPCBX0", "nSimHitsGEM", "nSimHitsGEMBX0"}};
  std::vector<TString> vFlt = {{"sim_hit_eta", "sim_hit_theta", "sim_hit_phi", "sim_hit_phi_loc"}};
  std::vector<TString> vInt = {{"sim_hit_eta_int", "sim_hit_theta_int", "sim_hit_phi_int", "sim_hit_endcap", "sim_hit_sector", "sim_hit_sector_index",
                                "sim_hit_station", "sim_hit_ring", "sim_hit_CSC_ID", "sim_hit_chamber", "sim_hit_FR", "sim_hit_pattern", "sim_hit_quality",
                                "sim_hit_alct_quality", "sim_hit_clct_quality", "sim_hit_roll", "sim_hit_subsector", "sim_hit_isCSC", "sim_hit_isRPC",
                                "sim_hit_valid", "sim_hit_BX", "sim_hit_strip", "sim_hit_strip_hi", "sim_hit_strip_low", "sim_hit_wire", "sim_hit_neighbor",
                                "sim_hit_match_iHit", "sim_hit_match_exact",
                                "sim_hit_roll", "sim_hit_isGEM"}};
  std::map<TString, int> mInts;
  std::map<TString, std::vector<float> > mVFlt;
  std::map<TString, std::vector<int> > mVInt;

  void Initialize();
  void Reset();
  inline void CheckSize() { CHECKSIZE(mVFlt); CHECKSIZE(mVInt); }
  void Fill(const l1t::EMTFHit & emtfHit);
};


/////////////////////////////////
///  Print out for debugging  ///
/////////////////////////////////

inline void PrintEMTFSimHit( const l1t::EMTFHit & hit ) {
  if (hit.Is_CSC()) {
    std::cout << "CSC LCT in BX " << hit.BX() << ", endcap " << hit.Endcap() << ", sector " << hit.Sector()
              << " (" << hit.Sector_idx() << "), subsector " << hit.Subsector() << ", station " << hit.Station()
              << ", ring " << hit.Ring() << ", CSC ID " << hit.CSC_ID() << ", chamber " << hit.Chamber()
              << ", pattern " << hit.Pattern() << ", quality " << hit.Quality()
              << ", strip " << hit.Strip() << ", wire " << hit.Wire() << std::endl;
  }
  else if (hit.Is_RPC()) {
    std::cout << "RPC hit in BX " << hit.BX() << ", endcap " << hit.Endcap() << ", sector " << hit.Sector()
	      << " (" << hit.Sector_idx() << "), subsector " << hit.Subsector() << ", station " << hit.Station()
	      << ", ring " << hit.Ring() << ", chamber " << hit.Chamber()
	      << ", theta " << hit.Theta_fp() << ", phi " << hit.Phi_fp() << std::endl;
  }
  else if (hit.Is_GEM()) {
    std::cout << "GEM hit in BX " << hit.BX() << ", endcap " << hit.Endcap()
              << ", station " << hit.Station()
              << ", ring " << hit.Ring() << ", chamber " << hit.Chamber()
              << ", strip " << hit.Strip() << std::endl;
  }
  else std::cout << "EMTF hit is neither CSC nor RPC nor GEM?!?" << std::endl;
}

inline void PrintSimHit( const std::map<TString, std::vector<int> > * iHit , const int i) {

  if (ACCESS(*iHit, "sim_hit_isCSC").at(i)) {
    std::cout << "* Found in BX " << ACCESS(*iHit, "sim_hit_BX").at(i) << ", endcap " << ACCESS(*iHit, "sim_hit_endcap").at(i)
              << ", sector " << ACCESS(*iHit, "sim_hit_sector").at(i) << " (" << ACCESS(*iHit, "sim_hit_sector_index").at(i)
              << "), subsector " << ACCESS(*iHit, "sim_hit_subsector").at(i) << ", station " << ACCESS(*iHit, "sim_hit_station").at(i)
              << ", ring " << ACCESS(*iHit, "sim_hit_ring").at(i) << ", CSC ID " << ACCESS(*iHit, "sim_hit_CSC_ID").at(i)
              << ", chamber " << ACCESS(*iHit, "sim_hit_chamber").at(i) << ", neighbor " << ACCESS(*iHit, "sim_hit_neighbor").at(i)
	      << ", pattern " << ACCESS(*iHit, "sim_hit_pattern").at(i) << ", quality " << ACCESS(*iHit, "sim_hit_quality").at(i)
	      << ", strip " << ACCESS(*iHit, "sim_hit_strip").at(i) << ", wire " << ACCESS(*iHit, "sim_hit_wire").at(i) << std::endl;
  }
  else if (ACCESS(*iHit, "sim_hit_isRPC").at(i)) {
    std::cout << "* Found in BX " << ACCESS(*iHit, "sim_hit_BX").at(i) << ", endcap " << ACCESS(*iHit, "sim_hit_endcap").at(i)
	      << ", sector " << ACCESS(*iHit, "sim_hit_sector").at(i) << " (" << ACCESS(*iHit, "sim_hit_sector_index").at(i)
	      << "), subsector " << ACCESS(*iHit, "sim_hit_subsector").at(i) << ", station " << ACCESS(*iHit, "sim_hit_station").at(i)
	      << ", ring " << ACCESS(*iHit, "sim_hit_ring").at(i) << ", chamber " << ACCESS(*iHit, "sim_hit_chamber").at(i)
	      << ", neighbor " << ACCESS(*iHit, "sim_hit_neighbor").at(i)
	      << ", theta " << ACCESS(*iHit, "sim_hit_theta_int").at(i) << ", phi " << ACCESS(*iHit, "sim_hit_phi_int").at(i) << std::endl;
  }
  else if (ACCESS(*iHit, "sim_hit_isGEM").at(i)) {
    std::cout << "* Found in BX " << ACCESS(*iHit, "sim_hit_BX").at(i) << ", endcap " << ACCESS(*iHit, "sim_hit_endcap").at(i)
              << ", station " << ACCESS(*iHit, "sim_hit_station").at(i)
              << ", ring " << ACCESS(*iHit, "sim_hit_ring").at(i) << ", chamber " << ACCESS(*iHit, "sim_hit_chamber").at(i)
              << ", neighbor " << ACCESS(*iHit, "sim_hit_neighbor").at(i)
              << ", strip " << ACCESS(*iHit, "sim_hit_strip").at(i) << std::endl;
  }
  else std::cout << "iHit with index " << i << " is neither CSC nor RPC nor GEM?!?" << std::endl;
}

#endif  // #ifndef BranchesEMTFHitInfo_h
