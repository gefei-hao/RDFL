# RDFL
Relative drug-fragment Likelihood

## Introduction
The relative drug-fragment likelihood (RDFL) a druglike fragment prediction tool was developed based on the probability ratio 
of the distribution of molecular descriptors. It build on a collection of over 4000 drug fragment and over 5000 non-drug fragment. 

If you use RFL for published research, please cite the paper. 


Thanks!

## Obtaining RDFL 
NLGenomeSweeper can be obtained from the [GitHub page](https://github.com/Huangjunjie2021/RDFL)


## Requirements & Installation
This is a pipeline to be run on unix based machines.
The following software must be available in your path.

* Python 3, version 3.5 or greater
* jdk1.8
* PaDEL Descriptor  #We upload a package of PaDEL, and it's available.



## Using this script

### Running RDFL

usage: python RDFL.py  input file （mol2/smi）   out file [optional]
                        


### Examples

python RDFL.py example.smi score.txt


### additional output files
 PaDEL_OUT.tsv           # the calculation result of PaDEL Descriptor



