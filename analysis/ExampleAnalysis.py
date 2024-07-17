import ROOT
from analysis import Analysis

class ExampleHistograms(Analysis.Histograms):
    def create_histograms(self):
        
        """
        semi leptonic code
        
        
        self.hist_semilep_leptonPt=ROOT.TH1F("lepton_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_semilep_leptoneta=ROOT.TH1F("lepton_eta", f'{self.title};leading lepton Eta;a.u.', 50, -5, 5)
        self.hist_semilep_leptonphi=ROOT.TH1F("lepton_phi", f'{self.title};leading lepton Phi;a.u.', 50, -5, 5)
        self.hist_semilep_leptonMt=ROOT.TH1F("lepton_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 250, 0, 10000)
        #self.hist_muon1Pt=ROOT.TH1F("muon1_pt", f'{self.title};subleading muon p_{{T}} [GeV];a.u.', 50, 0, 5000)
        
        self.hist_semilep_jet1Pt=ROOT.TH1F("jet1_pt", f'{self.title};leading jet p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_semilep_jet1eta=ROOT.TH1F("jet1_eta", f'{self.title};leading jet Eta;a.u.', 50, -5, 5)
        self.hist_semilep_jet1phi=ROOT.TH1F("jet1_phi", f'{self.title};leading jet Phi;a.u.', 50, -5, 5)
        self.hist_semilep_jet1Mt=ROOT.TH1F("jet1_Mt", f'{self.title};leading Jet Mt [Gev];a.u.', 50, 0, 300)
        
        self.hist_semilep_jet2Pt=ROOT.TH1F("jet2_pt", f'{self.title};subleading jet2 p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_semilep_jet2eta=ROOT.TH1F("jet2_eta", f'{self.title};subleading jet2 Eta;a.u.', 75, -10, 10)
        self.hist_semilep_jet2phi=ROOT.TH1F("jet2_phi", f'{self.title};subleading jet2Phi;a.u.', 50, -5, 5)
        self.hist_semilep_jet2Mt=ROOT.TH1F("jet2_Mt", f'{self.title};subleading Jet2 Mt [Gev];a.u.', 50, 0, 300)
        
        self.hist_semilep_fatjetPt=ROOT.TH1F("fatjet_pt", f'{self.title};fat jet p_{{T}} [GeV];a.u.', 200, 0, 10000)
        self.hist_semilep_fatjeteta=ROOT.TH1F("fatjet_eta", f'{self.title};fat jet Eta;a.u.', 50, -5, 5)
        self.hist_semilep_fatjetphi=ROOT.TH1F("fatjet_phi", f'{self.title};fat jet Phi;a.u.', 50, -5, 5)
        self.hist_semilep_fatjetMt=ROOT.TH1F("fatjet_Mt", f'{self.title};fat jet Mt [Gev];a.u.', 50, 0, 300)
        
        #self.hist_missingETPt=ROOT.TH1F("missingET_pt", f'{self.title};leading missingET p_{{T}} [GeV];a.u.', 50, 0, 5000)
        self.hist_semilep_missingETeta=ROOT.TH1F("missingET_eta", f'{self.title};leading missingET Eta;a.u.', 50, -5, 5)
        self.hist_semilep_missingETphi=ROOT.TH1F("missingET_phi", f'{self.title};leading missingET Phi;a.u.', 50, -5, 5)
        self.hist_semilep_missingETMt=ROOT.TH1F("missingET_Mt", f'{self.title};leading missingET Mt [Gev];a.u.', 50, 0, 10000)

        #self.hist_dimuonPt=ROOT.TH1F("dimuon_pt", f'{self.title};di-muon p_{{T}} [GeV];a.u.', 100, 0, 5000)
        self.hist_semilep_systemPt=ROOT.TH1F("system_pt", f'{self.title};system p_{{T}} [GeV];a.u.', 50, 0, 200)
        self.hist_semilep_systemMass=ROOT.TH1F("system_mass", f'{self.title}:system mass [Gev];a.u. ', 250, 0, 11000)
        self.hist_semilep_systemphi=ROOT.TH1F("system_phi", f'{self.title};system phi;a.u.', 50, -5, 5)
        self.hist_semilep_systemeta=ROOT.TH1F("system_eta", f'{self.title}:system eta;a.u. ', 50, -5, 5)
        
        self.hist_semilep_total_jetPt=ROOT.TH1F("combinedjets_pt", f'{self.title};combined jets p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_semilep_total_jeteta=ROOT.TH1F("combinedjets_eta", f'{self.title};combined jets Eta;a.u.', 50, -5, 5)
        self.hist_semilep_total_jetphi=ROOT.TH1F("combinedjets_phi", f'{self.title};combined jets Phi;a.u.', 50, -5, 5)
        self.hist_semilep_total_jetMt=ROOT.TH1F("combinedjets_Mt", f'{self.title};combined jets Mt [Gev];a.u.', 50, 0, 11000)
        
        self.hist_semilep_leptonic_channelPt=ROOT.TH1F("l_vl_pt", f'{self.title};l and v p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_semilep_leptonic_channeleta=ROOT.TH1F("l_vl_eta", f'{self.title};l and v Eta;a.u.', 50, -5, 5)
        self.hist_semilep_leptonic_channelphi=ROOT.TH1F("l_vl_phi", f'{self.title};l and v Phi;a.u.', 50, -5, 5)
        self.hist_semilep_leptonic_channelMt=ROOT.TH1F("l_vl_Mt", f'{self.title};l and v Mt [Gev];a.u.', 50, 0, 200)
        
        #self.hist_2d_ploteta=ROOT.TH2F("lepton_against_jet", f'{self.title};l and j [Gev];a.u.', 50, -5, 5)
        """
        
        """
        semi leptonic background
        """
        
        self.hist_semilep_bg_leptonPt=ROOT.TH1F("lepton_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_semilep_bg_leptoneta=ROOT.TH1F("lepton_eta", f'{self.title};leading lepton Eta ;a.u.', 50, -5, 5)
        self.hist_semilep_bg_leptonphi=ROOT.TH1F("lepton_phi", f'{self.title};leading lepton Phi [Rad];a.u.', 50, -5, 5)
        self.hist_semilep_bg_leptonMt=ROOT.TH1F("lepton_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_semilep_bg_fatjetPt=ROOT.TH1F("fatjet_pt", f'{self.title};leading fatjet p_{{T}} [GeV];a.u.', 200, 0, 10000)
        self.hist_semilep_bg_fatjeteta=ROOT.TH1F("fatjet_eta", f'{self.title};leading fatjet Eta ;a.u.', 50, -5, 5)
        self.hist_semilep_bg_fatjetphi=ROOT.TH1F("fatjet_phi", f'{self.title};leading fatjet Phi [Rad];a.u.', 50, -5, 5)
        self.hist_semilep_bg_fatjetMt=ROOT.TH1F("fatjet_Mt", f'{self.title};leading fatjet Mt [Gev];a.u.', 50, 0, 300)
        
        self.hist_semilep_bg_missingETeta=ROOT.TH1F("missingET_eta", f'{self.title};leading missingET Eta ;a.u.', 50, -5, 5)
        self.hist_semilep_bg_missingETphi=ROOT.TH1F("missingET_phi", f'{self.title};leading missingET Phi [Rad];a.u.', 50, -5, 5)
        self.hist_semilep_bg_missingETMt=ROOT.TH1F("missingET_Mt", f'{self.title};leading missingET Mt [Gev];a.u.', 50, 0, 1000)


        self.hist_semilep_bg_systemPt=ROOT.TH1F("system_pt", f'{self.title};system p_{{T}} [GeV];a.u.', 50, 0, 200)
        self.hist_semilep_bg_systemMass=ROOT.TH1F("system_mass", f'{self.title}:system mass [Gev];a.u. ', 250, 0, 10000)
        self.hist_semilep_bg_systemphi=ROOT.TH1F("system_phi", f'{self.title};system phi [rad];a.u.', 50, -5, 5)
        self.hist_semilep_bg_systemeta=ROOT.TH1F("system_eta", f'{self.title}:system eta ;a.u. ', 50, -5, 5)
        
        

        """
        leptonic code
        
        
        self.hist_leptonic_leptonsPt=ROOT.TH1F("leptons_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_leptonic_leptonseta=ROOT.TH1F("leptons_eta", f'{self.title};leading lepton Eta [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_leptonsphi=ROOT.TH1F("leptons_phi", f'{self.title};leading lepton Phi [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_leptonsMt=ROOT.TH1F("leptons_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_leptonic_missingETeta=ROOT.TH1F("missingET_eta", f'{self.title};leading missingET Eta [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_missingETphi=ROOT.TH1F("missingET_phi", f'{self.title};leading missingET Phi [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_missingETMt=ROOT.TH1F("missingET_Mt", f'{self.title};leading missingET Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_leptonic_lepton1Pt=ROOT.TH1F("lepton1_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_leptonic_lepton1eta=ROOT.TH1F("lepton1_eta", f'{self.title};leading lepton Eta [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_lepton1phi=ROOT.TH1F("lepton1_phi", f'{self.title};leading lepton Phi [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_lepton1Mt=ROOT.TH1F("lepton1_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_leptonic_lepton2Pt=ROOT.TH1F("lepton2_pt", f'{self.title};lepton 2 p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_leptonic_lepton2eta=ROOT.TH1F("lepton2_eta", f'{self.title};lepton 2 Eta [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_lepton2phi=ROOT.TH1F("lepton2_phi", f'{self.title};lepton 2 Phi [Rad];a.u.', 100, -5, 5)
        self.hist_leptonic_lepton2Mt=ROOT.TH1F("lepton2_Mt", f'{self.title};lepton 2 Mt [Gev];a.u.', 250, 0, 10000)
        
        #self.hist_counter=ROOT.TH1F("counter", f'{self.title}:counter [Gev]:a.u.', 1, 0.5, 1.5)
        """
        
        """
        Leptonic background code
        
        self.hist_lep_bg_leptonsPt=ROOT.TH1F("leptons_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_lep_bg_leptonseta=ROOT.TH1F("leptons_eta", f'{self.title};leading lepton Eta [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_leptonsphi=ROOT.TH1F("leptons_phi", f'{self.title};leading lepton Phi [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_leptonsMt=ROOT.TH1F("leptons_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_lep_bg_missingETeta=ROOT.TH1F("missingET_eta", f'{self.title};leading missingET Eta [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_missingETphi=ROOT.TH1F("missingET_phi", f'{self.title};leading missingET Phi [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_missingETMt=ROOT.TH1F("missingET_Mt", f'{self.title};leading missingET Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_lep_bg_lepton1Pt=ROOT.TH1F("lepton1_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_lep_bg_lepton1eta=ROOT.TH1F("lepton1_eta", f'{self.title};leading lepton Eta [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_lepton1phi=ROOT.TH1F("lepton1_phi", f'{self.title};leading lepton Phi [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_lepton1Mt=ROOT.TH1F("lepton1_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 250, 0, 10000)
        
        self.hist_lep_bg_lepton2Pt=ROOT.TH1F("lepton2_pt", f'{self.title};lepton 2 p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_lep_bg_lepton2eta=ROOT.TH1F("lepton2_eta", f'{self.title};lepton 2 Eta [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_lepton2phi=ROOT.TH1F("lepton2_phi", f'{self.title};lepton 2 Phi [Rad];a.u.', 100, -5, 5)
        self.hist_lep_bg_lepton2Mt=ROOT.TH1F("lepton2_Mt", f'{self.title};lepton 2 Mt [Gev];a.u.', 250, 0, 10000)
        """
        
        
        """combinedjets
        Hadronic code
        
        self.hist_had_fatjet1Pt=ROOT.TH1F("fatjet1_pt", f'{self.title};leading fatjet1 p_{{T}} [GeV];a.u.', 200, 0, 10000)
        self.hist_had_fatjet1eta=ROOT.TH1F("fatjet1_eta", f'{self.title};leading fatjet1 Eta [Rad];a.u.', 50, -5, 5)
        self.hist_had_fatjet1phi=ROOT.TH1F("fatjet1_phi", f'{self.title};leading fatjet1 Phi [Rad];a.u.', 50, -5, 5)
        self.hist_had_fatjet1Mt=ROOT.TH1F("fatjet1_Mt", f'{self.title};leading fatjet1 Mt [Gev];a.u.', 50, 0, 300)
        
        self.hist_had_fatjet2Pt=ROOT.TH1F("fatjet2_pt", f'{self.title};fatjet2 p_{{T}} [GeV];a.u.', 200, 0, 10000)
        self.hist_had_fatjet2eta=ROOT.TH1F("fatjet2_eta", f'{self.title};fatjet2 Eta [Rad];a.u.', 50, -5, 5)
        self.hist_had_fatjet2phi=ROOT.TH1F("fatjet2_phi", f'{self.title};fatjet2 Phi [Rad];a.u.', 50, -5, 5)
        self.hist_had_fatjet2Mt=ROOT.TH1F("fatjet2_Mt", f'{self.title};fatjet2 Mt [Gev];a.u.', 50, 0, 300)
        """
        
        """
        Hadronic background code
        
        self.hist_had_bg_fatjet1Pt=ROOT.TH1F("fatjet1_pt", f'{self.title};leading fatjet1 p_{{T}} [GeV];a.u.', 200, 0, 10000)
        self.hist_had_bg_fatjet1eta=ROOT.TH1F("fatjet1_eta", f'{self.title};leading fatjet1 Eta [Rad];a.u.', 50, -5, 5)
        self.hist_had_bg_fatjet1phi=ROOT.TH1F("fatjet1_phi", f'{self.title};leading fatjet1 Phi [Rad];a.u.', 50, -5, 5)
        self.hist_had_bg_fatjet1Mt=ROOT.TH1F("fatjet1_Mt", f'{self.title};leading fatjet1 Mt [Gev];a.u.', 50, 0, 300)
        
        self.hist_had_bg_fatjet2Pt=ROOT.TH1F("fatjet2_pt", f'{self.title};fatjet2 p_{{T}} [GeV];a.u.', 200, 0, 10000)
        self.hist_had_bg_fatjet2eta=ROOT.TH1F("fatjet2_eta", f'{self.title};fatjet2 Eta [Rad];a.u.', 50, -5, 5)
        self.hist_had_bg_fatjet2phi=ROOT.TH1F("fatjet2_phi", f'{self.title};fatjet2 Phi [Rad];a.u.', 50, -5, 5)
        self.hist_had_bg_fatjet2Mt=ROOT.TH1F("fatjet2_Mt", f'{self.title};fatjet2 Mt [Gev];a.u.', 50, 0, 300)
        """
        """
        vbf
        
        
        #self.hist_missingETPt=ROOT.TH1F("missingET_pt", f'{self.title};leading missingET p_{{T}} [GeV];a.u.', 50, 0, 5000)
        self.hist_vbf_missingET1eta=ROOT.TH1F("missingET_eta", f'{self.title};missingET 1 Eta [Rad];a.u.', 50, -7.5, 7.5)
        self.hist_vbf_missingET1phi=ROOT.TH1F("missingET_phi", f'{self.title};missingET 1 Phi [Rad];a.u.', 50, -5, 5)
        self.hist_vbf_missingET1Mt=ROOT.TH1F("missingET_Mt", f'{self.title};missingET 1 Mt [Gev];a.u.', 50, 0, 500)
        
        #self.hist_vbf_missingET2eta=ROOT.TH1F("missingET_eta", f'{self.title};missingET 2 Eta [Rad];a.u.', 50, -7.5, 7.5)
        #self.hist_vbf_missingET2phi=ROOT.TH1F("missingET_phi", f'{self.title};missingET 2 Phi [Rad];a.u.', 50, -5, 5)
        #self.hist_vbf_missingET2Mt=ROOT.TH1F("missingET_Mt", f'{self.title};missingET 2 Mt [Gev];a.u.', 50, 0, 500)
        """
        
        """
        code for vbf
        
        self.hist_vbf_lep_missingET1eta=ROOT.TH1F("missingET_eta", f'{self.title};missingET 1 Eta [Rad];a.u.', 50, -7.5, 7.5)
        self.hist_vbf_lep_missingET1phi=ROOT.TH1F("missingET_phi", f'{self.title};missingET 1 Phi [Rad];a.u.', 50, -5, 5)
        self.hist_vbf_lep_missingET1Mt=ROOT.TH1F("missingET_Mt", f'{self.title};missingET 1 Mt [Gev];a.u.', 50, 0, 500)
        """
        
        """
        Photon induced code
        
        
        self.hist_photoninduced_semilep_leptonPt=ROOT.TH1F("lepton_pt", f'{self.title};leading lepton p_{{T}} [GeV];a.u.', 250, 0, 10000)
        self.hist_photoninduced_semilep_leptoneta=ROOT.TH1F("lepton_eta", f'{self.title};leading lepton Eta;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_leptonphi=ROOT.TH1F("lepton_phi", f'{self.title};leading lepton Phi;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_leptonMt=ROOT.TH1F("lepton_Mt", f'{self.title};leading lepton Mt [Gev];a.u.', 120, 0, 1000)
        #self.hist_muon1Pt=ROOT.TH1F("muon1_pt", f'{self.title};subleading muon p_{{T}} [GeV];a.u.', 50, 0, 5000)
        
        #self.hist_photoninduced_semilep_jet1Pt=ROOT.TH1F("jet1_pt", f'{self.title};leading jet p_{{T}} [GeV];a.u.', 250, 0, 1000)
        #self.hist_photoninduced_semilep_jet1eta=ROOT.TH1F("jet1_eta", f'{self.title};leading jet Eta;a.u.', 50, -5, 5)
        #self.hist_photoninduced_semilep_jet1phi=ROOT.TH1F("jet1_phi", f'{self.title};leading jet Phi;a.u.', 50, -5, 5)
        #self.hist_photoninduced_semilep_jet1Mt=ROOT.TH1F("jet1_Mt", f'{self.title};leading Jet Mt [Gev];a.u.', 50, 0, 300)
        
        #self.hist_photoninduced_semilep_jet2Pt=ROOT.TH1F("jet2_pt", f'{self.title};subleading jet2 p_{{T}} [GeV];a.u.', 250, 0, 10000)
        #self.hist_photoninduced_semilep_jet2eta=ROOT.TH1F("jet2_eta", f'{self.title};subleading jet2 Eta;a.u.', 75, -10, 10)
        #self.hist_photoninduced_semilep_jet2phi=ROOT.TH1F("jet2_phi", f'{self.title};subleading jet2Phi;a.u.', 50, -5, 5)
        #self.hist_photoninduced_semilep_jet2Mt=ROOT.TH1F("jet2_Mt", f'{self.title};subleading Jet2 Mt [Gev];a.u.', 50, 0, 300)
        
        self.hist_photoninduced_semilep_fatjetPt=ROOT.TH1F("fatjet_pt", f'{self.title};fat jet p_{{T}} [GeV];a.u.', 70, 0, 1000)
        self.hist_photoninduced_semilep_fatjeteta=ROOT.TH1F("fatjet_eta", f'{self.title};fat jet Eta;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_fatjetphi=ROOT.TH1F("fatjet_phi", f'{self.title};fat jet Phi;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_fatjetMt=ROOT.TH1F("fatjet_Mt", f'{self.title};fat jet Mt [Gev];a.u.', 70, 0, 1000)
        
        #self.hist_missingETPt=ROOT.TH1F("missingET_pt", f'{self.title};leading missingET p_{{T}} [GeV];a.u.', 50, 0, 5000)
        self.hist_photoninduced_semilep_missingETeta=ROOT.TH1F("missingET_eta", f'{self.title};leading missingET Eta;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_missingETphi=ROOT.TH1F("missingET_phi", f'{self.title};leading missingET Phi;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_missingETMt=ROOT.TH1F("missingET_Mt", f'{self.title};leading missingET Mt [Gev];a.u.', 70, 0, 1000)

        #self.hist_dimuonPt=ROOT.TH1F("dimuon_pt", f'{self.title};di-muon p_{{T}} [GeV];a.u.', 100, 0, 5000)
        self.hist_photoninduced_semilep_systemPt=ROOT.TH1F("system_pt", f'{self.title};system p_{{T}} [GeV];a.u.', 50, 0, 1000)
        self.hist_photoninduced_semilep_systemMass=ROOT.TH1F("system_mass", f'{self.title}:system mass [Gev];a.u. ', 70, 0, 11000)
        self.hist_photoninduced_semilep_systemphi=ROOT.TH1F("system_phi", f'{self.title};system phi;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_systemeta=ROOT.TH1F("system_eta", f'{self.title}:system eta;a.u. ', 50, -5, 5)
        
        #self.hist_photoninduced_semilep_total_jetPt=ROOT.TH1F("combinedjets_pt", f'{self.title};combined jets p_{{T}} [GeV];a.u.', 250, 0, 10000)
        #self.hist_photoninduced_semilep_total_jeteta=ROOT.TH1F("combinedjets_eta", f'{self.title};combined jets Eta;a.u.', 50, -5, 5)
        #self.hist_photoninduced_semilep_total_jetphi=ROOT.TH1F("combinedjets_phi", f'{self.title};combined jets Phi;a.u.', 50, -5, 5)
        #self.hist_photoninduced_semilep_total_jetMt=ROOT.TH1F("combinedjets_Mt", f'{self.title};combined jets Mt [Gev];a.u.', 50, 0, 11000)
        
        self.hist_photoninduced_semilep_leptonic_channelPt=ROOT.TH1F("l_vl_pt", f'{self.title};l and v p_{{T}} [GeV];a.u.', 120, 0, 1000)
        self.hist_photoninduced_semilep_leptonic_channeleta=ROOT.TH1F("l_vl_eta", f'{self.title};l and v Eta;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_leptonic_channelphi=ROOT.TH1F("l_vl_phi", f'{self.title};l and v Phi;a.u.', 50, -5, 5)
        self.hist_photoninduced_semilep_leptonic_channelMt=ROOT.TH1F("l_vl_Mt", f'{self.title};l and v Mt [Gev];a.u.', 50, 0, 1000)
        """
        

    def fill_histograms(self, sample):
        """
        semi leptonic
        
        
        if len(sample.Muon)==1:
            lepton = sample.Muon[0].P4()
        else:
            lepton = sample.Electron[0].P4()
            
        
        self.hist_semilep_leptonPt.Fill(lepton.Pt())
        self.hist_semilep_leptoneta.Fill(lepton.Eta())
        self.hist_semilep_leptonphi.Fill(lepton.Phi())
        self.hist_semilep_leptonMt.Fill(lepton.Mt())
        
        self.hist_semilep_jet1Pt.Fill(sample.Jet[0].PT)
        self.hist_semilep_jet1eta.Fill(sample.Jet[0].Eta)
        self.hist_semilep_jet1phi.Fill(sample.Jet[0].Phi)
        self.hist_semilep_jet1Mt.Fill(sample.Jet[0].Mass)
        
        self.hist_semilep_jet2Pt.Fill(sample.Jet[1].PT)
        self.hist_semilep_jet2eta.Fill(sample.Jet[1].Eta)
        self.hist_semilep_jet2phi.Fill(sample.Jet[1].Phi)
        self.hist_semilep_jet2Mt.Fill(sample.Jet[1].Mass)
        
        self.hist_semilep_fatjetPt.Fill(sample.FatJet[0].PT)
        self.hist_semilep_fatjeteta.Fill(sample.FatJet[0].Eta)
        self.hist_semilep_fatjetphi.Fill(sample.FatJet[0].Phi)
        self.hist_semilep_fatjetMt.Fill(sample.FatJet[0].Mass)
        
        #self.hist_missingETPt.Fill(sample.MissingET.PT)
        self.hist_semilep_missingETeta.Fill(sample.MissingET[0].Eta)
        self.hist_semilep_missingETphi.Fill(sample.MissingET[0].Phi)
        self.hist_semilep_missingETMt.Fill(sample.MissingET[0].MET)
        
        w = sample.FatJet[0].P4()
        system = w + lepton + sample.MissingET[0].P4()
        self.hist_semilep_systemPt.Fill(system.Pt())
        self.hist_semilep_systemMass.Fill(system.M())
        self.hist_semilep_systemeta.Fill(system.Eta())
        self.hist_semilep_systemphi.Fill(system.Phi())
        
        total_jet = sample.Jet[0].P4() + sample.Jet[1].P4()
        self.hist_semilep_total_jetPt.Fill(total_jet.Pt())
        self.hist_semilep_total_jetMt.Fill(total_jet.Mt())
        self.hist_semilep_total_jeteta.Fill(total_jet.Eta())
        self.hist_semilep_total_jetphi.Fill(total_jet.Phi())
        
        leptonic_channel = lepton + sample.MissingET[0].P4()
        self.hist_semilep_leptonic_channelPt.Fill(leptonic_channel.Pt())
        self.hist_semilep_leptonic_channelMt.Fill(leptonic_channel.M())
        self.hist_semilep_leptonic_channeleta.Fill(leptonic_channel.Eta())
        self.hist_semilep_leptonic_channelphi.Fill(leptonic_channel.Phi())
        
        #self.hist_2d_ploteta.Fill(lepton.eta(), sample.FatJet[0].eta)        
        """
        
        """
        semi leptonic background
        """
        
        if len(sample.Muon)==0:
            lepton = sample.Electron[0].P4() 
        elif len(sample.Electron)==0:
            lepton = sample.Muon[0].P4() 
        else:
            return False
            
            
        self.hist_semilep_bg_leptonPt.Fill(lepton.Pt())
        self.hist_semilep_bg_leptoneta.Fill(lepton.Eta())
        self.hist_semilep_bg_leptonphi.Fill(lepton.Phi())
        self.hist_semilep_bg_leptonMt.Fill(lepton.Mt())
        
        self.hist_semilep_bg_fatjetPt.Fill(sample.FatJet[0].PT)
        self.hist_semilep_bg_fatjeteta.Fill(sample.FatJet[0].Eta)
        self.hist_semilep_bg_fatjetphi.Fill(sample.FatJet[0].Phi)
        self.hist_semilep_bg_fatjetMt.Fill(sample.FatJet[0].Mass)
        
        self.hist_semilep_bg_missingETeta.Fill(sample.MissingET[0].Eta)
        self.hist_semilep_bg_missingETphi.Fill(sample.MissingET[0].Phi)
        self.hist_semilep_bg_missingETMt.Fill(sample.MissingET[0].MET)
        
        w = sample.FatJet[0].P4()
        system = w + lepton + sample.MissingET[0].P4()
        self.hist_semilep_bg_systemPt.Fill(system.Pt())
        self.hist_semilep_bg_systemMass.Fill(system.M())
        self.hist_semilep_bg_systemeta.Fill(system.Eta())
        self.hist_semilep_bg_systemphi.Fill(system.Phi())
        
        
        """
        Leptonic code
        
        
        #if len(sample.Muon)==2:
            #return True
        #return False
        
        if len(sample.Muon)==0 and len(sample.Electron)>=2:
            lepton1 = sample.Electron[0].P4()
            lepton2 = sample.Electron[1].P4()
            #print('0, 2')
        elif len(sample.Muon)>=1 and len(sample.Electron)>=1:
            lepton1 = sample.Muon[0].P4()
            lepton2 = sample.Electron[0].P4()
            #print('1,1')
        elif len(sample.Muon)>=2 and len(sample.Electron)==0:
            lepton1 = sample.Muon[0].P4()
            lepton2 = sample.Muon[1].P4()
            #print('2,0')
        else:
            #print('0,0')
            return False
            
        leptons= lepton1 + lepton2
        system = leptons + sample.MissingET[0].P4()
        
        self.hist_leptonic_leptonsPt.Fill(leptons.Pt())
        self.hist_leptonic_leptonseta.Fill(leptons.Eta())
        self.hist_leptonic_leptonsphi.Fill(leptons.Phi())
        self.hist_leptonic_leptonsMt.Fill(leptons.Mt())
        
        
        self.hist_leptonic_missingETeta.Fill(sample.MissingET[0].Eta)
        self.hist_leptonic_missingETphi.Fill(sample.MissingET[0].Phi)
        self.hist_leptonic_missingETMt.Fill(sample.MissingET[0].MET)
        
        self.hist_leptonic_lepton1Pt.Fill(lepton1.Pt())
        self.hist_leptonic_lepton1eta.Fill(lepton1.Eta())
        self.hist_leptonic_lepton1phi.Fill(lepton1.Phi())
        self.hist_leptonic_lepton1Mt.Fill(lepton1.Mt())
        
        self.hist_leptonic_lepton2Pt.Fill(lepton2.Pt())
        self.hist_leptonic_lepton2eta.Fill(lepton2.Eta())
        self.hist_leptonic_lepton2phi.Fill(lepton2.Phi())
        self.hist_leptonic_lepton2Mt.Fill(lepton2.Mt())
        
        #self.hist_counter.Fill(1)
        """
        
        """
        leptonic background code
        
        if len(sample.Muon)==0 and len(sample.Electron)>=4:
            lepton1 = sample.Electron[0].P4()
            lepton2 = sample.Electron[1].P4()
            #print('0, 2')
        elif len(sample.Muon)>=2 and len(sample.Electron)>=2:
            lepton1 = sample.Muon[0].P4()
            lepton2 = sample.Electron[0].P4()
            #print('1,1')
        elif len(sample.Muon)>=4 and len(sample.Electron)==0:
            lepton1 = sample.Muon[0].P4()
            lepton2 = sample.Muon[1].P4()
            #print('2,0')
        else:
            #print('0,0')
            return False
            
        leptons= lepton1 + lepton2
        system = leptons + sample.MissingET[0].P4()
        
        self.hist_lep_bg_leptonsPt.Fill(leptons.Pt())
        self.hist_lep_bg_leptonseta.Fill(leptons.Eta())
        self.hist_lep_bg_leptonsphi.Fill(leptons.Phi())
        self.hist_lep_bg_leptonsMt.Fill(leptons.Mt())
        
        
        self.hist_lep_bg_missingETeta.Fill(sample.MissingET[0].Eta)
        self.hist_lep_bg_missingETphi.Fill(sample.MissingET[0].Phi)
        self.hist_lep_bg_missingETMt.Fill(sample.MissingET[0].MET)
        
        self.hist_lep_bg_lepton1Pt.Fill(lepton1.Pt())
        self.hist_lep_bg_lepton1eta.Fill(lepton1.Eta())
        self.hist_lep_bg_lepton1phi.Fill(lepton1.Phi())
        self.hist_lep_bg_lepton1Mt.Fill(lepton1.Mt())
        
        self.hist_lep_bg_lepton2Pt.Fill(lepton2.Pt())
        self.hist_lep_bg_lepton2eta.Fill(lepton2.Eta())
        self.hist_lep_bg_lepton2phi.Fill(lepton2.Phi())
        self.hist_lep_bg_lepton2Mt.Fill(lepton2.Mt())
        """
        
        """
        Hadronic code
        
        self.hist_had_fatjet1Pt.Fill(sample.FatJet[0].PT)
        self.hist_had_fatjet1eta.Fill(sample.FatJet[0].Eta)
        self.hist_had_fatjet1phi.Fill(sample.FatJet[0].Phi)
        self.hist_had_fatjet1Mt.Fill(sample.FatJet[0].Mass)


        self.hist_had_fatjet2Pt.Fill(sample.FatJet[1].PT)
        self.hist_had_fatjet2eta.Fill(sample.FatJet[1].Eta)
        self.hist_had_fatjet2phi.Fill(sample.FatJet[1].Phi)
        self.hist_had_fatjet2Mt.Fill(sample.FatJet[1].Mass)
        """
        
        """
        Hadronic background code
        
        self.hist_had_bg_fatjet1Pt.Fill(sample.FatJet[0].PT)
        self.hist_had_bg_fatjet1eta.Fill(sample.FatJet[0].Eta)
        self.hist_had_bg_fatjet1phi.Fill(sample.FatJet[0].Phi)
        self.hist_had_bg_fatjet1Mt.Fill(sample.FatJet[0].Mass)

        self.hist_had_bg_fatjet2Pt.Fill(sample.FatJet[1].PT)
        self.hist_had_bg_fatjet2eta.Fill(sample.FatJet[1].Eta)
        self.hist_had_bg_fatjet2phi.Fill(sample.FatJet[1].Phi)
        self.hist_had_bg_fatjet2Mt.Fill(sample.FatJet[1].Mass)
        """
        
        """
        vbf
        
        
        self.hist_vbf_missingET1eta.Fill(sample.MissingET[0].Eta)
        self.hist_vbf_missingET1phi.Fill(sample.MissingET[0].Phi)
        self.hist_vbf_missingET1Mt.Fill(sample.MissingET[0].MET)
        
        #self.hist_vbf_missingET2eta.Fill(sample.MissingET[1].Eta)
        #self.hist_vbf_missingET2phi.Fill(sample.MissingET[1].Phi)
        #self.hist_vbf_missingET2Mt.Fill(sample.MissingET[1].MET)
        """
        
        """
        code for semi lep channel and vbf
        
        self.hist_vbf_lep_missingET1eta.Fill(sample.MissingET[0].Eta)
        self.hist_vbf_lep_missingET1phi.Fill(sample.MissingET[0].Phi)
        self.hist_vbf_lep_missingET1Mt.Fill(sample.MissingET[0].MET)
        """
        
        """
        Photon induced code
        
        
        if len(sample.Muon)==1:
            lepton = sample.Muon[0].P4()
        else:
            lepton = sample.Electron[0].P4()
            
        if len(sample.FatJet)==1:
            fatjet = sample.FatJet[0].P4()
        else:
            return False
        
        self.hist_photoninduced_semilep_leptonPt.Fill(lepton.Pt())
        self.hist_photoninduced_semilep_leptoneta.Fill(lepton.Eta())
        self.hist_photoninduced_semilep_leptonphi.Fill(lepton.Phi())
        self.hist_photoninduced_semilep_leptonMt.Fill(lepton.Mt())
        
        #self.hist_photoninduced_semilep_jet1Pt.Fill(sample.Jet[0].PT)
        #self.hist_photoninduced_semilep_jet1eta.Fill(sample.Jet[0].Eta)
        #self.hist_photoninduced_semilep_jet1phi.Fill(sample.Jet[0].Phi)
        #self.hist_photoninduced_semilep_jet1Mt.Fill(sample.Jet[0].Mass)
        
        #self.hist_photoninduced_semilep_jet2Pt.Fill(sample.Jet[1].PT)
        #self.hist_photoninduced_semilep_jet2eta.Fill(sample.Jet[1].Eta)
        #self.hist_photoninduced_semilep_jet2phi.Fill(sample.Jet[1].Phi)
        #self.hist_photoninduced_semilep_jet2Mt.Fill(sample.Jet[1].Mass)
        
        self.hist_photoninduced_semilep_fatjetPt.Fill(fatjet.Pt())
        self.hist_photoninduced_semilep_fatjeteta.Fill(fatjet.Eta())
        self.hist_photoninduced_semilep_fatjetphi.Fill(fatjet.Phi())
        self.hist_photoninduced_semilep_fatjetMt.Fill(fatjet.Mt())
        
        #self.hist_missingETPt.Fill(sample.MissingET.PT)
        self.hist_photoninduced_semilep_missingETeta.Fill(sample.MissingET[0].Eta)
        self.hist_photoninduced_semilep_missingETphi.Fill(sample.MissingET[0].Phi)
        self.hist_photoninduced_semilep_missingETMt.Fill(sample.MissingET[0].MET)
        
        w = sample.FatJet[0].P4()
        system = w + lepton + sample.MissingET[0].P4()
        self.hist_photoninduced_semilep_systemPt.Fill(system.Pt())
        self.hist_photoninduced_semilep_systemMass.Fill(system.M())
        self.hist_photoninduced_semilep_systemeta.Fill(system.Eta())
        self.hist_photoninduced_semilep_systemphi.Fill(system.Phi())
        
        #total_jet = sample.Jet[0].P4() + sample.Jet[1].P4()
        #self.hist_photoninduced_semilep_total_jetPt.Fill(total_jet.Pt())
        #self.hist_photoninduced_semilep_total_jetMt.Fill(total_jet.Mt())
        #self.hist_photoninduced_semilep_total_jeteta.Fill(total_jet.Eta())
        #self.hist_photoninduced_semilep_total_jetphi.Fill(total_jet.Phi())
        
        leptonic_channel = lepton + sample.MissingET[0].P4()
        self.hist_photoninduced_semilep_leptonic_channelPt.Fill(leptonic_channel.Pt())
        self.hist_photoninduced_semilep_leptonic_channelMt.Fill(leptonic_channel.M())
        self.hist_photoninduced_semilep_leptonic_channeleta.Fill(leptonic_channel.Eta())
        self.hist_photoninduced_semilep_leptonic_channelphi.Fill(leptonic_channel.Phi())
        """
        
class ExampleAnalysis(Analysis.Analysis):
    """
    An example analysis that plots the pT of the leading muon.
    """
    def __init__(self):
        super(ExampleAnalysis, self).__init__(ExampleHistograms)

    def selection(self, sample):
        #if len(sample.Muon)>0 or len(sample.Electron)>0:
            #return True
        #return False
    
        #if len(sample.FatJet) == 1:
            #return True
        #return False
        
        if (len(sample.Muon)+len(sample.Electron))>=1:
            return True
        return False
    
        #if (len(sample.Muon) + len(sample.Electron))>=2:
            #return True
        #return False
        
        #if len(sample.FatJet) == 2:
           #return True
        #return False
        
        #if len(sample.MissingET) > 0:
            #return True
        #return False
