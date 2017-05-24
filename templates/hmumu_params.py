import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":1000},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":5000},
    "mhl":{"name":"higgs_m","title":"m_{H} [GeV]","bin":75,"xmin":50,"xmax":2000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":50,"xmin":50,"xmax":150},
    "ptmu_1":{"name":"mu1_pt","title":"p_{T}^{#mu, max} [GeV]","bin":100,"xmin":20,"xmax":500},
    "ptmu_2":{"name":"mu2_pt","title":"p_{T}^{#mu, min} [GeV]","bin":100,"xmin":20,"xmax":500},
    "nljets":{"name":"njets","title":"N_{jets}^{l}","bin":4,"xmin":-0.5,"xmax":3.5},
    "nbjets":{"name":"nbjets","title":"N_{jets}^{b}","bin":4,"xmin":-0.5,"xmax":3.5},
    "njets":{"name":"njets","title":"N_{jets}^{b}","bin":4,"xmin":-0.5,"xmax":3.5},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":100},
}

colors = {}
colors['H'] = ROOT.kRed
colors['tt'] = ROOT.kYellow
colors['DY'] = ROOT.kGreen+2
colors['VV'] = ROOT.kBlue

groups = collections.OrderedDict()
groups['H'] = ['pp_h012j_5f', 'pp_vbf_h01j_5f', 'pp_tth01j_5f', 'pp_vh01j_5f']
groups['tt'] = ['pp_tt012j_5f']
groups['DY'] = ['pp_v0123j_5f', 'pp_ll012j_5f'] 
groups['VV'] = ['pp_vv012j_5f', 'pp_llv01j_5f']

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
selbase_nomasscut = ('mu2_pt > 20. && mu1_eta < 4 && mu2_eta < 4 &&'
            'nbjets == 0 &&'
            'met_pt < 50')

selbase_masscut = ('mu2_pt > 20. && mu1_eta < 4 && mu2_eta < 4 &&'
            'nbjets == 0 &&'
            'met_pt < 50 &&'
            'higgs_m > 122.5 && higgs_m < 127.5')

sel_bases = {}
sel_bases['nomasscut'] = selbase_nomasscut
sel_bases['masscut'] = selbase_masscut
