import codecs
import sys
from statistics import mean, stdev

cfL1=sys.argv[1]
cfL2=sys.argv[2]

entrada1=codecs.open(cfL1,"r",encoding="utf-8")
entrada2=codecs.open(cfL2,"r",encoding="utf-8")


ratios=[]
while 1:
    liniaL1=entrada1.readline()
    if not liniaL1:
        break
    liniaL2=entrada2.readline()
    liniaL1=liniaL1.rstrip()
    liniaL2=liniaL2.rstrip()
    lenL1=len(liniaL1)
    lenL2=len(liniaL2)
    ratio=lenL2/lenL1
    ratios.append(ratio)
    
mean=mean(ratios)
stdev=stdev(ratios)
max_length_factor=mean+2*stdev

print("MEAN: ",mean)
print("STDEV:",stdev)
print("MAX LENGTH FACTOR:",max_length_factor)
