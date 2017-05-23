# HiggsAnalysisFCC

This scripts allows to easily design an analysis based on previously produced flat trees with the [Heppy](https://github.com/cbernet/heppy) framework.

Example:
```
./createAnalysis.py -n [analysis_name_in_heppy] -c [heppy_cfg] -t [heppy_tree_location] -o [output_dir] -p [analysis_parameters] -j [proc_dict] -b
```

```
./createAnalysis.py -n hmumu -c ../../heppy/test/analysis_pp_hmumu.py -t ../HeppyTrees/hmumu_v2 -o ../analysis_hmumu_v2 -p templates/hmumu_params.py```
