#!/usr/bin/env python
import subprocess, glob, optparse, json, ast, os
from pprint import pprint
import ntpath
import importlib

#_____________________________________________________________________________
def options():
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-n', '--analysis_name', dest='analysis_name', type=str, default='')
    parser.add_option('-c', '--heppy_cfg', dest='heppy_cfg', type=str, default='')
    parser.add_option('-j', '--proc_file_json', dest='proc_file_json', type=str, default='/afs/cern.ch/work/h/helsens/public/FCCDicts/procDict.json')
    parser.add_option('-t', '--heppy_tree_dir', dest='heppy_tree_dir', type=str, default='')
    parser.add_option('-o', '--analysis_output', dest='analysis_output', type=str, default='')
    parser.add_option('-p', '--param_file', dest='param_file', type=str, default='')
    parser.add_option('-b', '--binned', dest='binned', default=True)
    return parser.parse_args()

#______________________________________________________________________________
def main():
    
    ops, args = options()

    args = split_comma_args(args)

    # give this analysis a name
    analysisName = ops.analysis_name

    # heppy analysis configuration
    heppyCfg = ops.heppy_cfg

    # process dictionary
    processDict = ops.proc_file_json

    # heppy trees location directory
    treeDir = ops.heppy_tree_dir

    # analysis dir
    analysisDir = ops.analysis_output

    # param file
    paramFile = ops.param_file
    param = importlib.import_module(os.path.splitext(ntpath.basename(paramFile))[0])

    # use binned samples or not
    binned = ops.binned 

    # tree location
    treePath = '/heppy.analyzers.examples.{}.TreeProducer.TreeProducer_1/tree.root'.format(analysisName)

    # retrieve list of processes from heppy cfg
    processes = []
    with open(heppyCfg) as f:
        lines = f.readlines()
        for l in lines:
            if 'splitFactor' in l:
                processes.append(l.rsplit('.', 1)[0])

    with open(processDict) as f:
        procDict = json.load(f)
    
    # prepare analysis dir
    os.system('mkdir -p {}'.format(analysisDir))
    os.system('cp tools.py {}'.format(analysisDir))
    os.system('cp {} {}'.format(paramFile, analysisDir))
    
    analysisFile = '{}/analysis_{}.py'.format(analysisDir, analysisName)
    template = open(analysisFile, 'w')
    template.write('#!/usr/bin/env python\n')
    template.write('import collections\n')
    template.write('from tools import *\n')
    template.write('from {} import *\n'.format(os.path.splitext(ntpath.basename(paramFile))[0]))
    template.write('\n')
    template.write('#_________________________________________________________________________________________________\n')
    template.write('def initProcesses(listOfProcesses, block):\n')
    template.write('\n')
    template.write('    ### initialize processes for {} analysis\n'.format(analysisName))
    template.write('\n')

    for p in processes:

       xsec = procDict[p]['crossSection']
       nev = procDict[p]['numberOfEvents']
       eff = procDict[p]['matchingEfficiency']
       kf = procDict[p]['kfactor']

       tree = '{}/{}/{}'.format(os.path.abspath(treeDir), p, treePath)

       matched_xsec = xsec*eff
       
       template.write('    {} = Process("{}",\n'.format(p, p))
       template.write('                          tree="{}",\n'.format(tree))
       template.write('                          nevents={},\n'.format(nev))
       template.write('                          xsec={},\n'.format(xsec))
       template.write('                          effmatch={},\n'.format(eff))
       template.write('                          kfactor={},\n'.format(kf))
       template.write('                         )\n')
       template.write('\n')

    template.write('    ### list of processes\n')
    for p in processes:
        template.write('    listOfProcesses.append({})\n'.format(p))

    template.write('\n')
    template.write('# here create loop from associations\n')

    #form groups according to param file
    for name, procs in param.groups.iteritems():
        template.write('    block["{}"] = [\n'.format(name))
	for procstr in procs:
            for proc in processes:
	        if binned:
	            if procstr in proc and 'HT' in proc:
		        template.write('                    {},\n'.format(proc))
		else:
		    if procstr in proc and 'HT' not in proc:
		        template.write('                    {},\n'.format(proc))
	template.write('                  ]\n'.format(name))
    
    template.write('\n')
    template.write('#_________________________________________________________________________________________________\n')
    template.write('def main():\n')

    template.write('    ### run analyses \n')
    template.write('    for ns, bs in sel_bases.iteritems():\n')
    template.write('        listOfProcesses = []\n')
    template.write('        block = collections.OrderedDict()\n')
    template.write('        initProcesses(listOfProcesses, block)\n')
    template.write('        producePlots(bs, listOfProcesses, block, colors, variables, ptmax, nsteps, uncertainties, ns, intLumi, delphesVersion, runFull)\n')
    template.write('\n')
    template.write('#_________________________________________________________________________________________________\n')
    template.write('if __name__ == "__main__": main()\n')
    
    os.system('chmod u+x {}'.format(analysisFile))

#______________________________________________________________________________
def split_comma_args(args):
    new_args = []
    for arg in args:
        new_args.extend( arg.split(',') )
    return new_args
#______________________________________________________________________________
if __name__ == '__main__': 
    main()
