# HiggsAnalysisFCC

This scripts allows to easily design an analysis based on prevously produced flat trees with the [Heppy](https://github.com/cbernet/heppy) framework.

Example:
```
./createAnalysis.py -n [analysis_name] -c [heppy_cfg] -t [heppy_tree_location] -o [output_dir] -p [analysis_parameters] -j [proc_dict] -b
```

```
./parseAnalysis_v2.py -n hmumu -c ../heppy/test/analysis_pp_hmumu.py -t ../HeppyTrees/hmumu_v2 -o test -p templates/hmumu_params.py
```
