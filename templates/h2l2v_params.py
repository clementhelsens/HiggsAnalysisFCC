import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"pth","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":1000},
    "pthl":{"name":"pth","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":5000},
    "mll":{"name":"ll_m","title":"m_{ll} [GeV]","bin":50,"xmin":12,"xmax":200},
    "mt":{"name":"mt","title":"m_{T} [GeV]","bin":50,"xmin":0,"xmax":200},
    "mr":{"name":"mr","title":"m_{R} [GeV]","bin":50,"xmin":0,"xmax":500},
    "ptl_1":{"name":"l1_pt","title":"p_{T}^{l, max} [GeV]","bin":50,"xmin":0,"xmax":500},
    "ptl_2":{"name":"l2_pt","title":"p_{T}^{l, min} [GeV]","bin":50,"xmin":0,"xmax":500},
    "nljets":{"name":"njets","title":"N_{jets}^{l}","bin":6,"xmin":-0.5,"xmax":5.5},
    "nbjets":{"name":"nbjets","title":"N_{jets}^{b}","bin":6,"xmin":-0.5,"xmax":5.5},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":500},
    "dphi":{"name":"dphi_ll","title":"#Delta #phi (l+, l-)","bin":50,"xmin":0,"xmax":3.1416},
    "dphillmet":{"name":"dphi_llmet","title":"#Delta #phi (ll, MET)","bin":50,"xmin":0,"xmax":3.1416},
}

colors = {}
colors['H'] = ROOT.kRed
colors['VV'] = ROOT.kAzure+6
colors['VVV'] = ROOT.kBlue
colors['tt'] = ROOT.kYellow

groups = collections.OrderedDict()
groups['H'] = ['pp_h012j_5f', 'pp_vbf_h01j_5f', 'pp_tth01j_5f', 'pp_vh01j_5f']
groups['VV'] = ['pp_vv012j_5f', 'pp_llv01j_5f']
groups['VVV'] = ['pp_vvv01j_5f']
groups['tt'] = ['pp_tt012j_5f', 'pp_tv012j_5f']

### signal and background uncertainties hypothesis
uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.1'

# for pt dependent analysis
ptmax = 2500.
nsteps = 25

# the first time needs to be set to True
runFull = True

# base selections
selbase_nomasscut = ('l2_pt > 25. && l1_pt > 20. && abs(l1_eta) < 4 && abs(l2_eta) < 4 &&'
                'is_of && met_pt > 20  && ll_m > 12. && nbjets == 0 && ll_pt > 45.')
                #'is_of && met_pt > 20 && ll_m > 12. && ll_pt > 45.')

selbase_masscut = ('l2_pt > 25. && l1_pt > 20. && abs(l1_eta) < 4 && abs(l2_eta) < 4 &&'
                'is_of && met_pt > 20  && ll_m > 12.  && ll_m < 100. && nbjets == 0 && ll_pt > 45. &&'
                #'is_of && met_pt > 20  && ll_m > 12.  && ll_m < 100 && ll_pt > 45. &&'
                'dphi_ll < 0.75 & mr > 50 && mr < 150')

sel_bases = {}
sel_bases['nomasscut'] = selbase_nomasscut
sel_bases['masscut'] = selbase_masscut
