import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":300},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":3000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":75,"xmin":100,"xmax":180},
    "mll":{"name":"zed_m","title":"m_{ll} [GeV]","bin":50,"xmin":12,"xmax":200},
}

colors = {}
colors['H'] = ROOT.kRed
colors['Z#gamma'] = ROOT.kMagenta-9

groups = collections.OrderedDict()
groups['H'] = ['pp_h012j_5f', 'pp_vbf_h01j_5f', 'pp_tth01j_5f', 'pp_vh01j_5f']
groups['Z#gamma'] = ['pp_vv012j_5f', 'pp_llv01j_5f']

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
selbase_nomasscut = ('zed_m > 50. && zed_m < 200. &&'
                'l1_pt > 20. && l2_pt > 20. && a_pt > 15. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4 && abs(a_eta) < 4')

selbase_masscut = ('zed_m > 75. && zed_m < 105. &&'
                'l1_pt > 20. && l2_pt > 20. && a_pt > 15. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4 && abs(a_eta) < 4 &&'
                'higgs_m > 122.5 && higgs_m < 127.5')
sel_bases = {}
sel_bases['nomasscut'] = selbase_nomasscut
sel_bases['masscut'] = selbase_masscut
