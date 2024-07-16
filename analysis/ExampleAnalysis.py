import ROOT
from analysis import Analysis

class ExampleHistograms(Analysis.Histograms):
    def create_histograms(self):
        #semi leptonic signal
        
        '''self.hist_system_semiPt=ROOT.TH1F("system_pt", f'{self.title};System p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_system_semiEta=ROOT.TH1F("system_eta", f'{self.title};System Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_semiPhi=ROOT.TH1F("system_phi", f'{self.title};System Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_semiMt=ROOT.TH1F("system_mt", f'{self.title};System Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jets_semiPt=ROOT.TH1F("jets_pt", f'{self.title};Jets p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jets_semiEta=ROOT.TH1F("jets_eta", f'{self.title};Jets Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_semiPhi=ROOT.TH1F("jets_phi", f'{self.title};Jets Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_semiMt=ROOT.TH1F("jets_mt", f'{self.title};Jets Mass (transverse) [GeV];a.u.', 100, 0, 250)
        self.hist_jets_semiM=ROOT.TH1F("jets_m", f'{self.title};Jets Mass [GeV];a.u.', 100, 0, 165)
        
        self.hist_lepton_semiPt=ROOT.TH1F("lepton_pt", f'{self.title};Lepton p_{{T}} [GeV];a.u.', 50, 0, 165)
        self.hist_lepton_semiMt=ROOT.TH1F("lepton_mt", f'{self.title};Lepton M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_lepton_semiEta=ROOT.TH1F("lepton_eta", f'{self.title};lepton Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton_semiPhi=ROOT.TH1F("lepton_phi", f'{self.title};Lepton Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_leptons_semiPt=ROOT.TH1F("lepton_pt", f'{self.title};Leptonic W p_{{T}} [GeV]; a.u.', 100, 0, 165)
        self.hist_leptons_semiMt=ROOT.TH1F("leptons_mt", f'{self.title};Leptonic W M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_leptons_semiEta=ROOT.TH1F("leptons_eta", f'{self.title};leptonic W Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_leptons_semiPhi=ROOT.TH1F("leptons_phi", f'{self.title};Leptonic W Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_jet0_semiPt=ROOT.TH1F("jet0_pt", f'{self.title};Leading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet0_semiEta=ROOT.TH1F("jet0_eta", f'{self.title};Leading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_semiPhi=ROOT.TH1F("jet0_phi", f'{self.title};Leading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_semiMt=ROOT.TH1F("jet0_mt", f'{self.title};Leading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet1_semiPt=ROOT.TH1F("jet1_pt", f'{self.title};Subleading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet1_semiEta=ROOT.TH1F("jet1_eta", f'{self.title};Subleading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_semiPhi=ROOT.TH1F("jet1_phi", f'{self.title};Subleading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_semiMt=ROOT.TH1F("jet1_mt", f'{self.title};Subleading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_missingET_semiMET=ROOT.TH1F("missingET_pt", f'{self.title};MET p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_missingET_semiEta=ROOT.TH1F("missingET_eta", f'{self.title};MET Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_missingET_semiPhi=ROOT.TH1F("missingET_phi", f'{self.title};MET Phi [rad];a.u.', 100, -3.5, 3.5)'''
        
        #fully leptonic signal
        
        '''self.hist_lepton1_lepPt=ROOT.TH1F("lepton1_pt", f'{self.title};lepton1 p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_lepton1_lepEta=ROOT.TH1F("lepton1_Eta", f'{self.title};lepton1 Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton1_lepPhi=ROOT.TH1F("lepton1_Phi", f'{self.title};lepton1 Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton1_lepMt=ROOT.TH1F("lepton1_Mt", f'{self.title};lepton1 M_{{T}} [GeV];a.u.', 100, 0, 165)
        
        self.hist_lepton2_lepPt=ROOT.TH1F("lepton2_pt", f'{self.title};lepton2 p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_lepton2_lepEta=ROOT.TH1F("lepton2_Eta", f'{self.title};lepton2 Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton2_lepPhi=ROOT.TH1F("lepton2_Phi", f'{self.title};lepton2 Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton2_lepMt=ROOT.TH1F("lepton2_Mt", f'{self.title};lepton2 M_{{T}} [GeV];a.u.', 100, 0, 165)
        
        self.hist_leptons_lepPt=ROOT.TH1F("leptons_pt", f'{self.title};leptons p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_leptons_lepEta=ROOT.TH1F("leptons_Eta", f'{self.title};leptons Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_leptons_lepPhi=ROOT.TH1F("leptons_Phi", f'{self.title};leptons Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_leptons_lepMt=ROOT.TH1F("leptons_Mt", f'{self.title};leptons M_{{T}} [GeV];a.u.', 100, 0, 165)
        
        self.hist_system_lepPt=ROOT.TH1F("leptons_pt", f'{self.title};leptons p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_system_lepEta=ROOT.TH1F("leptons_Eta", f'{self.title};leptons Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_lepPhi=ROOT.TH1F("leptons_Phi", f'{self.title};leptons Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_lepMt=ROOT.TH1F("leptons_Mt", f'{self.title};leptons M_{{T}} [GeV];a.u.', 100, 0, 165)
        
        self.hist_MissingET_lepMET=ROOT.TH1F("MissingET_MET", f'{self.title};MissingET MET [GeV];a.u.', 100, 0, 200)
        self.hist_MissingET_lepEta=ROOT.TH1F("MissingET_Eta", f'{self.title};MissingET Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_MissingET_lepPhi=ROOT.TH1F("MissingET_Phi", f'{self.title};MissingET Phi [rad];a.u.', 100, -3.5, 3.5)'''
        
        #hadronic signal
        
        '''self.hist_jets_hadPt=ROOT.TH1F("jets_pt", f'{self.title};Jets p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jets_hadEta=ROOT.TH1F("jets_eta", f'{self.title};Jets Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_hadPhi=ROOT.TH1F("jets_phi", f'{self.title};Jets Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_hadMt=ROOT.TH1F("jets_mt", f'{self.title};Jets Mass (transverse) [GeV];a.u.', 100, 0, 250)
        self.hist_jets_hadM=ROOT.TH1F("jets_m", f'{self.title};Jets Mass [GeV];a.u.', 100, 0, 165)
        
        self.hist_jet1_hadPt=ROOT.TH1F("jet1_pt", f'{self.title};Jet1 p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet1_hadEta=ROOT.TH1F("jet1_eta", f'{self.title};Jet1 Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_hadPhi=ROOT.TH1F("jet1_phi", f'{self.title};Jet1 Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_hadMt=ROOT.TH1F("jet1_mt", f'{self.title};Jet1 Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet2_hadPt=ROOT.TH1F("jet2_pt", f'{self.title};Jet2 p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet2_hadEta=ROOT.TH1F("jet2_eta", f'{self.title};Jet2 Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet2_hadPhi=ROOT.TH1F("jet2_phi", f'{self.title};Jet2 Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet2_hadMt=ROOT.TH1F("jet2_mt", f'{self.title};Jet2 Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet3_hadPt=ROOT.TH1F("jet3_pt", f'{self.title};Jet3 p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet3_hadEta=ROOT.TH1F("jet3_eta", f'{self.title};Jet3 Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet3_hadPhi=ROOT.TH1F("jet3_phi", f'{self.title};Jet3 Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet3_hadMt=ROOT.TH1F("jet3_mt", f'{self.title};Jet3 Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet4_hadPt=ROOT.TH1F("jet4_pt", f'{self.title};Jet4 p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet4_hadEta=ROOT.TH1F("jet4_eta", f'{self.title};Jet4 Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet4_hadPhi=ROOT.TH1F("jet4_phi", f'{self.title};Jet4 Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet4_hadMt=ROOT.TH1F("jet4_mt", f'{self.title};Jet4 Mass (transverse) [GeV];a.u.', 100, 0, 250)'''
        
        #semi leptonic ZZ bg
        
        '''self.hist_system_bg1_z_semiPt=ROOT.TH1F("system_pt", f'{self.title};System p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_system_bg1_z_semiEta=ROOT.TH1F("system_eta", f'{self.title};System Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_bg1_z_semiPhi=ROOT.TH1F("system_phi", f'{self.title};System Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_bg1_z_semiMt=ROOT.TH1F("system_mt", f'{self.title};System Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jets_bg1_z_semiPt=ROOT.TH1F("jets_pt", f'{self.title};Jets p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jets_bg1_z_semiEta=ROOT.TH1F("jets_eta", f'{self.title};Jets Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_bg1_z_semiPhi=ROOT.TH1F("jets_phi", f'{self.title};Jets Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_bg1_z_semiMt=ROOT.TH1F("jets_mt", f'{self.title};Jets Mass (transverse) [GeV];a.u.', 100, 0, 250)
        self.hist_jets_bg1_z_semiM=ROOT.TH1F("jets_m", f'{self.title};Jets Mass [GeV];a.u.', 100, 0, 165)
        
        self.hist_lepton_bg1_z_semiPt=ROOT.TH1F("lepton_pt", f'{self.title};Lepton p_{{T}} [GeV];a.u.', 50, 0, 165)
        self.hist_lepton_bg1_z_semiMt=ROOT.TH1F("lepton_mt", f'{self.title};Lepton M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_lepton_bg1_z_semiEta=ROOT.TH1F("lepton_eta", f'{self.title};lepton Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton_bg1_z_semiPhi=ROOT.TH1F("lepton_phi", f'{self.title};Lepton Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_leptons_bg1_z_semiPt=ROOT.TH1F("leptons_pt", f'{self.title};Leptons M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_leptons_bg1_z_semiMt=ROOT.TH1F("leptons_mt", f'{self.title};Leptonic W M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_leptons_bg1_z_semiEta=ROOT.TH1F("leptons_eta", f'{self.title};leptonic W Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_leptons_bg1_z_semiPhi=ROOT.TH1F("leptons_phi", f'{self.title};Leptonic W Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_jet0_bg1_z_semiPt=ROOT.TH1F("jet0_pt", f'{self.title};Leading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet0_bg1_z_semiEta=ROOT.TH1F("jet0_eta", f'{self.title};Leading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_bg1_z_semiPhi=ROOT.TH1F("jet0_phi", f'{self.title};Leading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_bg1_z_semiMt=ROOT.TH1F("jet0_mt", f'{self.title};Leading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet1_bg1_z_semiPt=ROOT.TH1F("jet1_pt", f'{self.title};Subleading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet1_bg1_z_semiEta=ROOT.TH1F("jet1_eta", f'{self.title};Subleading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_bg1_z_semiPhi=ROOT.TH1F("jet1_phi", f'{self.title};Subleading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_bg1_z_semiMt=ROOT.TH1F("jet1_mt", f'{self.title};Subleading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_missingET_bg1_z_semiMET=ROOT.TH1F("missingET_pt", f'{self.title};MET p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_missingET_bg1_z_semiEta=ROOT.TH1F("missingET_eta", f'{self.title};MET Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_missingET_bg1_z_semiPhi=ROOT.TH1F("missingET_phi", f'{self.title};MET Phi [rad];a.u.', 100, -3.5, 3.5)'''
        
        #semi leptonic aa bg
        
        '''self.hist_system_bg2_a_semiPt=ROOT.TH1F("system_pt", f'{self.title};System p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_system_bg2_a_semiEta=ROOT.TH1F("system_eta", f'{self.title};System Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_bg2_a_semiPhi=ROOT.TH1F("system_phi", f'{self.title};System Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_system_bg2_a_semiMt=ROOT.TH1F("system_mt", f'{self.title};System Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jets_bg2_a_semiPt=ROOT.TH1F("jets_pt", f'{self.title};Jets p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jets_bg2_a_semiEta=ROOT.TH1F("jets_eta", f'{self.title};Jets Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_bg2_a_semiPhi=ROOT.TH1F("jets_phi", f'{self.title};Jets Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jets_bg2_a_semiMt=ROOT.TH1F("jets_mt", f'{self.title};Jets Mass (transverse) [GeV];a.u.', 100, 0, 250)
        self.hist_jets_bg2_a_semiM=ROOT.TH1F("jets_m", f'{self.title};Jets Mass [GeV];a.u.', 100, 0, 165)
        
        self.hist_lepton_bg2_a_semiPt=ROOT.TH1F("lepton_pt", f'{self.title};Lepton p_{{T}} [GeV];a.u.', 50, 0, 165)
        self.hist_lepton_bg2_a_semiMt=ROOT.TH1F("lepton_mt", f'{self.title};Lepton M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_lepton_bg2_a_semiEta=ROOT.TH1F("lepton_eta", f'{self.title};lepton Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton_bg2_a_semiPhi=ROOT.TH1F("lepton_phi", f'{self.title};Lepton Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_leptons_bg2_a_semiPt=ROOT.TH1F("leptons_pt", f'{self.title};Leptons M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_leptons_bg2_a_semiMt=ROOT.TH1F("leptons_mt", f'{self.title};Leptonic W M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_leptons_bg2_a_semiEta=ROOT.TH1F("leptons_eta", f'{self.title};leptonic W Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_leptons_bg2_a_semiPhi=ROOT.TH1F("leptons_phi", f'{self.title};Leptonic W Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_jet0_bg2_a_semiPt=ROOT.TH1F("jet0_pt", f'{self.title};Leading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet0_bg2_a_semiEta=ROOT.TH1F("jet0_eta", f'{self.title};Leading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_bg2_a_semiPhi=ROOT.TH1F("jet0_phi", f'{self.title};Leading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_bg2_a_semiMt=ROOT.TH1F("jet0_mt", f'{self.title};Leading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet1_bg2_a_semiPt=ROOT.TH1F("jet1_pt", f'{self.title};Subleading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet1_bg2_a_semiEta=ROOT.TH1F("jet1_eta", f'{self.title};Subleading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_bg2_a_semiPhi=ROOT.TH1F("jet1_phi", f'{self.title};Subleading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_bg2_a_semiMt=ROOT.TH1F("jet1_mt", f'{self.title};Subleading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_missingET_bg2_a_semiMET=ROOT.TH1F("missingET_pt", f'{self.title};MET p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_missingET_bg2_a_semiEta=ROOT.TH1F("missingET_eta", f'{self.title};MET Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_missingET_bg2_a_semiPhi=ROOT.TH1F("missingET_phi", f'{self.title};MET Phi [rad];a.u.', 100, -3.5, 3.5)'''
        
        #semi lep sig and bg
        
        self.hist_dijet_semiPt=ROOT.TH1F("dijet_pt", f'{self.title};Di-jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_dijet_semiEta=ROOT.TH1F("dijet_eta", f'{self.title};Di-jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_dijet_semiPhi=ROOT.TH1F("dijet_phi", f'{self.title};Di-jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_dijet_semiMt=ROOT.TH1F("dijet_mt", f'{self.title};Di-jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        self.hist_dijet_semiM=ROOT.TH1F("dijet_m", f'{self.title};Di-jet Mass [GeV];a.u.', 100, 0, 165)
        
        self.hist_lepton_semiPt=ROOT.TH1F("lepton_pt", f'{self.title};Lepton p_{{T}} [GeV];a.u.', 50, 0, 165)
        self.hist_lepton_semiMt=ROOT.TH1F("lepton_mt", f'{self.title};Lepton M_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_lepton_semiEta=ROOT.TH1F("lepton_eta", f'{self.title};lepton Eta [Rad];a.u.', 100, -3.5, 3.5)
        self.hist_lepton_semiPhi=ROOT.TH1F("lepton_phi", f'{self.title};Lepton Phi [GeV];a.u.', 100, -3.5, 3.5)
        
        self.hist_jet0_semiPt=ROOT.TH1F("jet0_pt", f'{self.title};Leading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet0_semiEta=ROOT.TH1F("jet0_eta", f'{self.title};Leading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_semiPhi=ROOT.TH1F("jet0_phi", f'{self.title};Leading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet0_semiMt=ROOT.TH1F("jet0_mt", f'{self.title};Leading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
        self.hist_jet1_semiPt=ROOT.TH1F("jet1_pt", f'{self.title};Subleading Jet p_{{T}} [GeV];a.u.', 100, 0, 165)
        self.hist_jet1_semiEta=ROOT.TH1F("jet1_eta", f'{self.title};Subleading Jet Eta [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_semiPhi=ROOT.TH1F("jet1_phi", f'{self.title};Subleading Jet Phi [rad];a.u.', 100, -3.5, 3.5)
        self.hist_jet1_semiMt=ROOT.TH1F("jet1_mt", f'{self.title};Subleading Jet Mass (transverse) [GeV];a.u.', 100, 0, 250)
        
    def fill_histograms(self, sample):
        #semi leptonic signal
        
        '''self.hist_jet0_semiEta.Fill(sample.Jet[0].Eta)
        self.hist_jet0_semiPt.Fill(sample.Jet[0].PT)
        self.hist_jet0_semiPhi.Fill(sample.Jet[0].Phi)
        self.hist_jet0_semiMt.Fill(sample.Jet[0].Mass)
        
        self.hist_jet1_semiEta.Fill(sample.Jet[1].Eta)
        self.hist_jet1_semiPt.Fill(sample.Jet[1].PT)
        self.hist_jet1_semiPhi.Fill(sample.Jet[1].Phi)
        self.hist_jet1_semiMt.Fill(sample.Jet[1].Mass)
        
        self.hist_missingET_semiEta.Fill(sample.MissingET[0].Eta)
        self.hist_missingET_semiMET.Fill(sample.MissingET[0].MET)
        self.hist_missingET_semiPhi.Fill(sample.MissingET[0].Phi)
        

        # Add muons using pT
        dimuon=sample.Muon[0].P4()+sample.Muon[1].P4()
        self.hist_dimuonPt.Fill(dimuon.Pt())
        if len(sample.Muon)==1:
            lepton = sample.Muon[0].P4()
        else:
            lepton = sample.Electron[0].P4()
            
        self.hist_lepton_semiPt.Fill(lepton.Pt())
        self.hist_lepton_semiEta.Fill(lepton.Eta())
        self.hist_lepton_semiPhi.Fill(lepton.Phi())
        self.hist_lepton_semiMt.Fill(lepton.Mt())
        
        w2 = lepton + sample.MissingET[0].P4()
    
        # Add muons using pT
        w = sample.Jet[0].P4()+sample.Jet[1].P4()
        
        self.hist_leptons_semiPt.Fill(w2.Pt())
        self.hist_leptons_semiEta.Fill(w2.Eta())
        self.hist_leptons_semiPhi.Fill(w2.Phi())
        self.hist_leptons_semiMt.Fill(w2.Mt())
        
        system = w + lepton + sample.MissingET[0].P4()
        self.hist_system_semiPt.Fill(system.Pt())
        self.hist_system_semiEta.Fill(system.Eta())
        self.hist_system_semiPhi.Fill(system.Phi())
        self.hist_system_semiMt.Fill(system.Mt())
        
        self.hist_jets_semiPt.Fill(w.Pt())
        self.hist_jets_semiEta.Fill(w.Eta())
        self.hist_jets_semiPhi.Fill(w.Phi())
        self.hist_jets_semiMt.Fill(w.Mt())
        self.hist_jets_semiM.Fill(w.M())'''
        
        #fully leptonic signal
        
        '''if len(sample.Muon)==0:
            lepton1 = sample.Electron[0].P4()
            lepton2 = sample.Electron[1].P4()
        elif len(sample.Muon)==1:
            lepton1 = sample.Muon[0].P4()
            lepton2 = sample.Electron[0].P4()
        else:
            lepton1 = sample.Muon[0].P4()
            lepton2 = sample.Muon[1].P4()
            
        leptons = lepton1 + lepton2
        
        system = leptons + sample.MissingET[0].P4()
            
        self.hist_lepton1_lepPt.Fill(lepton1.Pt())
        self.hist_lepton1_lepPhi.Fill(lepton1.Phi())
        self.hist_lepton1_lepEta.Fill(lepton1.Eta())
        self.hist_lepton1_lepMt.Fill(lepton1.Mt())
        
        self.hist_lepton2_lepPt.Fill(lepton2.Pt())
        self.hist_lepton2_lepPhi.Fill(lepton2.Phi())
        self.hist_lepton2_lepEta.Fill(lepton2.Eta())
        self.hist_lepton2_lepMt.Fill(lepton2.Mt())
        
        self.hist_leptons_lepPt.Fill(leptons.Pt())
        self.hist_leptons_lepPhi.Fill(leptons.Phi())
        self.hist_leptons_lepEta.Fill(leptons.Eta())
        self.hist_leptons_lepMt.Fill(leptons.Mt())
        
        self.hist_system_lepPt.Fill(system.Pt())
        self.hist_system_lepEta.Fill(system.Eta())
        self.hist_system_lepPhi.Fill(system.Phi())
        self.hist_system_lepMt.Fill(system.Mt())
        
        self.hist_MissingET_lepEta.Fill(sample.MissingET[0].Eta)
        self.hist_MissingET_lepMET.Fill(sample.MissingET[0].MET)
        self.hist_MissingET_lepPhi.Fill(sample.MissingET[0].Phi)'''
        
        #hadronic signal
        
        '''jets = sample.Jet[0].P4() +sample.Jet[2].P4() +sample.Jet[2].P4() +sample.Jet[3].P4()
        
        self.hist_jets_hadPt.Fill(jets.Pt())
        self.hist_jets_hadEta.Fill(jets.Eta())
        self.hist_jets_hadPhi.Fill(jets.Phi())
        self.hist_jets_hadMt.Fill(jets.Mt())
        self.hist_jets_hadM.Fill(jets.M())
        
        self.hist_jet1_hadEta.Fill(sample.Jet[0].Eta)
        self.hist_jet1_hadMt.Fill(sample.Jet[0].Mass)
        self.hist_jet1_hadPhi.Fill(sample.Jet[0].Phi)
        self.hist_jet1_hadPt.Fill(sample.Jet[0].PT)
        
        self.hist_jet2_hadEta.Fill(sample.Jet[1].Eta)
        self.hist_jet2_hadMt.Fill(sample.Jet[1].Mass)
        self.hist_jet2_hadPhi.Fill(sample.Jet[1].Phi)
        self.hist_jet2_hadPt.Fill(sample.Jet[1].PT)
        
        self.hist_jet3_hadEta.Fill(sample.Jet[2].Eta)
        self.hist_jet3_hadMt.Fill(sample.Jet[2].Mass)
        self.hist_jet3_hadPhi.Fill(sample.Jet[2].Phi)
        self.hist_jet3_hadPt.Fill(sample.Jet[2].PT)
        
        self.hist_jet4_hadEta.Fill(sample.Jet[3].Eta)
        self.hist_jet4_hadMt.Fill(sample.Jet[3].Mass)
        self.hist_jet4_hadPhi.Fill(sample.Jet[3].Phi)
        self.hist_jet4_hadPt.Fill(sample.Jet[3].PT)'''
        
        #semi leptonic QQWM, bg
        
        '''self.hist_jet0_bg1_qqwm_semiEta.Fill(sample.Jet[0].Eta)
        self.hist_jet0_bg1_qqwm_semiPt.Fill(sample.Jet[0].PT)
        self.hist_jet0_bg1_qqwm_semiPhi.Fill(sample.Jet[0].Phi)
        self.hist_jet0_bg1_qqwm_semiMt.Fill(sample.Jet[0].Mass)
        
        self.hist_jet1_bg1_z_semiEta.Fill(sample.Jet[1].Eta)
        self.hist_jet1_bg1_z_semiPt.Fill(sample.Jet[1].PT)
        self.hist_jet1_bg1_z_semiPhi.Fill(sample.Jet[1].Phi)
        self.hist_jet1_bg1_z_semiMt.Fill(sample.Jet[1].Mass)
        
        self.hist_missingET_bg1_z_semiEta.Fill(sample.MissingET[0].Eta)
        self.hist_missingET_bg1_z_semiMET.Fill(sample.MissingET[0].MET)
        self.hist_missingET_bg1_z_semiPhi.Fill(sample.MissingET[0].Phi)
        
        if len(sample.Muon)==1:
            lepton = sample.Muolepton2 = sample.Electron[1].P4()n[0].P4()
        else:
            lepton = sample.Electron[0].P4()
            
        self.hist_lepton_bg1_z_semiPt.Fill(lepton.Pt())
        self.hist_lepton_bg1_z_semiEta.Fill(lepton.Eta())
        self.hist_lepton_bg1_z_semiPhi.Fill(lepton.Phi())
        self.hist_lepton_bg1_z_semiMt.Fill(lepton.Mt())
        
        w2 = lepton + sample.MissingET[0].P4()

        w = sample.Jet[0].P4()+sample.Jet[1].P4()
        
        self.hist_leptons_bg1_z_semiPt.Fill(w2.Pt())
        self.hist_leptons_bg1_z_semiEta.Fill(w2.Eta())
        self.hist_leptons_bg1_z_semiPhi.Fill(w2.Phi())
        self.hist_leptons_bg1_z_semiMt.Fill(w2.Mt())
        
        system = w + lepton + sample.MissingET[0].P4()
        self.hist_system_bg1_z_semiPt.Fill(system.Pt())
        self.hist_system_bg1_z_semiEta.Fill(system.Eta())
        self.hist_system_bg1_z_semiPhi.Fill(system.Phi())
        self.hist_system_bg1_z_semiMt.Fill(system.Mt())
        
        self.hist_jets_bg1_z_semiPt.Fill(w.Pt())
        self.hist_jets_bg1_z_semiEta.Fill(w.Eta())
        self.hist_jets_bg1_z_semiPhi.Fill(w.Phi())
        self.hist_jets_bg1_z_semiMt.Fill(w.Mt())
        self.hist_jets_bg1_z_semiM.Fill(w.M())'''
        
        #semi leptonic aa bg
        
        '''self.hist_jet0_bg2_a_semiEta.Fill(sample.Jet[0].Eta)
        self.hist_jet0_bg2_a_semiPt.Fill(sample.Jet[0].PT)
        self.hist_jet0_bg2_a_semiPhi.Fill(sample.Jet[0].Phi)
        self.hist_jet0_bg2_a_semiMt.Fill(sample.Jet[0].Mass)
        
        self.hist_jet1_bg2_a_semiEta.Fill(sample.Jet[1].Eta)
        self.hist_jet1_bg2_a_semiPt.Fill(sample.Jet[1].PT)
        self.hist_jet1_bg2_a_semiPhi.Fill(sample.Jet[1].Phi)
        self.hist_jet1_bg2_a_semiMt.Fill(sample.Jet[1].Mass)
        
        self.hist_missingET_bg2_a_semiEta.Fill(sample.MissingET[0].Eta)
        self.hist_missingET_bg2_a_semiMET.Fill(sample.MissingET[0].MET)
        self.hist_missingET_bg2_a_semiPhi.Fill(sample.MissingET[0].Phi)
        
        if len(sample.Muon)==1:
            lepton = sample.Muon[0].P4()
        else:
            lepton = sample.Electron[0].P4()
            
        lepton2 = sample.Electron[1].P4()self.hist_lepton_bg2_a_semiPt.Fill(lepton.Pt())
        self.hist_lepton_bg2_a_semiEta.Fill(lepton.Eta())
        self.hist_lepton_bg2_a_semiPhi.Fill(lepton.Phi())
        self.hist_lepton_bg2_a_semiMt.Fill(lepton.Mt())
        
        w2 = lepton + sample.MissingET[0].P4()
        
        w = sample.Jet[0].P4()+sample.Jet[1].P4()
        
        self.hist_leptons_bg2_a_semiPt.Fill(w2.Pt())
        self.hist_leptons_bg2_a_semiEta.Fill(w2.Eta())
        self.hist_leptons_bg2_a_semiPhi.Fill(w2.Phi())
        self.hist_leptons_bg2_a_semiMt.Fill(w2.Mt())
        
        system = w + lepton + sample.MissingET[0].P4()
        self.hist_system_bg2_a_semiPt.Fill(system.Pt())
        self.hist_system_bg2_a_semiEta.Fill(system.Eta())
        self.hist_system_bg2_a_semiPhi.Fill(system.Phi())
        self.hist_system_bg2_a_semiMt.Fill(system.Mt())
        
        self.hist_jets_bg2_a_semiPt.Fill(w.Pt())
        self.hist_jets_bg2_a_semiEta.Fill(w.Eta())
        self.hist_jets_bg2_a_semiPhi.Fill(w.Phi())
        self.hist_jets_bg2_a_semiMt.Fill(w.Mt())
        self.hist_jets_bg2_a_semiM.Fill(w.M())'''
        
        #semi-lep bg and sig
        
        if len(sample.Muon)==0:
            lepton1 = sample.Electron[0].P4()
        elif len(sample.Electron)==0:
            lepton1 = sample.Muon[0].P4()
        else:
            return False
            
        dijet = sample.Jet[0].P4() + sample.Jet[0].P4()
        
        self.hist_dijet_semiEta.Fill(dijet.Eta())
        self.hist_dijet_semiM.Fill(dijet.M())
        self.hist_dijet_semiMt.Fill(dijet.Mt())
        self.hist_dijet_semiPhi.Fill(dijet.Phi())
        self.hist_dijet_semiPt.Fill(dijet.Pt())
     
        self.hist_jet0_semiEta.Fill(sample.Jet[0].Eta)
        self.hist_jet0_semiPt.Fill(sample.Jet[0].PT)
        self.hist_jet0_semiPhi.Fill(sample.Jet[0].Phi)
        self.hist_jet0_semiMt.Fill(sample.Jet[0].Mass)
        
        self.hist_jet1_semiEta.Fill(sample.Jet[1].Eta)
        self.hist_jet1_semiPt.Fill(sample.Jet[1].PT)
        self.hist_jet1_semiPhi.Fill(sample.Jet[1].Phi)
        self.hist_jet1_semiMt.Fill(sample.Jet[1].Mass)
        
        self.hist_lepton_semiPt.Fill(lepton1.Pt())
        self.hist_lepton_semiPhi.Fill(lepton1.Phi())
        self.hist_lepton_semiEta.Fill(lepton1.Eta())
        self.hist_lepton_semiMt.Fill(lepton1.Mt())
    
class ExampleAnalysis(Analysis.Analysis):
    """
    An example analysis that plots the pT of the leading muon.
    """
    def __init__(self):
        super(ExampleAnalysis, self).__init__(ExampleHistograms)
 
    def selection(self, sample):
        '''semi leptonic'''
        #if len(sample.Jet)==2:
        #    return True
        #return False 
        
        if (len(sample.Muon)+len(sample.Electron))>=1 and len(sample.Jet)==2:
            return True
        return False
        
        '''fully leptonic'''
        #if (len(sample.Muon)+len(sample.Electron))==2:
        #    return True
        #return False
 
        '''hadronic'''
       # if len(sample.Jet)==4:
       #     return True
       # return False