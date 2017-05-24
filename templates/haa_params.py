import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":1000},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":5000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":50,"xmax":180},
    "mhl":{"name":"higgs_m","title":"m_{H} [GeV]","bin":45,"xmin":50,"xmax":500},
}

colors = {}
colors['H'] = ROOT.kRed
colors['pp #rightarrow #gamma#gamma'] = ROOT.kYellow
colors['gg #rightarrow #gamma#gamma'] = ROOT.kOrange

groups = collections.OrderedDict()
groups['H'] = ['pp_h012j_5f', 'pp_vbf_h01j_5f', 'pp_tth01j_5f', 'pp_vh01j_5f']
groups['gg #rightarrow #gamma#gamma'] = ['gg_aa01j_5f']
groups['pp #rightarrow #gamma#gamma'] = ['pp_aa012j_5f']

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
selbase_nomasscut = ('a1_pt > 30. && a2_pt > 30. &&'
                     'abs(a1_eta) < 4.0 && abs(a2_eta) < 4.0')

selbase_masscut = ('a1_pt > 30. && a2_pt > 30. &&'
                   'abs(a1_eta) < 4.0 && abs(a2_eta) < 4.0 &&'
                   'higgs_m > 122.5 && higgs_m < 127.5')

sel_bases = {}
sel_bases['nomasscut'] = selbase_nomasscut
sel_bases['masscut'] = selbase_masscut
