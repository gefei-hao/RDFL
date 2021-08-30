"""
    RFL-score.py [input_dir] [output_file] (optional)
"""
#This script was written by Huang Junjie on July 10, 2021。
import os, re, sys, math
from itertools import islice
from def_bay_chem import bayesian


if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(0)
dout = sys.argv[1]
fout = 'scores.txt'
if len(sys.argv) >= 3:
    fout = sys.argv[2]
fi=open('./PaDEL/conf.bak').readlines()
fo=open('./PaDEL/conf','w')
for line in fi:
    if re.search('DescriptorFile', line):
        fo.write(line.replace('output.file', "PaDEL_OUT.csv"))
    elif re.search('Directory', line):
        fo.write(line.replace('input.file', dout))
    else:
        fo.write(line)
fo.close()
os.system("java -jar ./PaDEL/PaDEL-Descriptor.jar -config ./PaDEL/conf -descriptortypes ./PaDEL/1_2.xml >/dev/null 2>&1")

with open("./PaDEL_OUT.csv") as f:
    data = f.read().replace(',','\t')
    with open('PaDEL_OUT.tsv','w') as f:
        f.write(data)
with open(fout, 'a') as result:
    data= open('PaDEL_OUT.tsv')
    for line in islice(data,1,None):
        a = line.split()
        name = a[0]
        ALogP = a[1]
        nHeavyAtom = a[5]
        nN = a[9]
        nO = a[10]
        BCUTc = a[21]
        nHBAcc2 = a[25]
        nRotBt = a[30]
        PSA = a[32]
        mw = a[33]
        b = float(ALogP)
        c = float(nHeavyAtom)
        d = float(nN)
        e = float(nO)
        f = float(BCUTc)
        g = float(nHBAcc2)
        h = float(nRotBt)
        i = float(PSA)
        j = float(mw)
        score = bayesian(b, c, d, e, f, g, h, i, j)
        end = name + ' ' + str(score) + '\n'
        result.write(end)
#### file clean#########
if os.path.exists('./PaDEL_OUT.csv'):
    os.remove('./PaDEL_OUT.csv')
if os.path.exists('./PaDEL_OUT.csv.log'):
    os.remove('./PaDEL_OUT.csv.log')
