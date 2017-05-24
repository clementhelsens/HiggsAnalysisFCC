import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":1000},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":50,"xmin":0,"xmax":5000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":36,"xmin":80,"xmax":170},
    "mhl":{"name":"higgs_m","title":"m_{H} [GeV]","bin":55,"xmin":50,"xmax":600},
}

colors = {}
colors['H'] = ROOT.kRed
colors['tt'] = ROOT.kYellow
colors['VVV'] = ROOT.kBlue
colors['ZZ'] = ROOT.kGreen+2

groups = collections.OrderedDict()
groups['H'] = ['pp_h012j_5f', 'pp_vbf_h01j_5f', 'pp_tth01j_5f', 'pp_vh01j_5f']
groups['tt'] = ['pp_tt012j_5f']
groups['VVV'] = ['pp_vvv01j_5f']
groups['ZZ'] = ['pp_llll01j_5f']

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
ptmax = 1000.
nsteps = 10

# the first time needs to be set to True
runFull = True

# base selections
selbase_nomasscut = ('zed1_m > 40. && zed1_m < 120. &&'
                'zed2_m > 12. && zed2_m < 120. &&'
                'l1_pt > 20. && l2_pt > 10. && l3_pt > 7. && l4_pt > 5. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4')

selbase_masscut = ('zed1_m > 40. && zed1_m < 120. &&'
                'zed2_m > 12. && zed2_m < 120. &&'
                'l1_pt > 20. && l2_pt > 10. && l3_pt > 7. && l4_pt > 5. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4 &&'
                'higgs_m > 122.5 && higgs_m < 127.5')

sel_bases = {}
sel_bases['nomasscut'] = selbase_nomasscut
sel_bases['masscut'] = selbase_masscut
