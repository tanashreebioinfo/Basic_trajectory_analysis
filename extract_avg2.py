#programme to bin the data according to the range and calculate average value
import numpy as np
import sys
import pandas as pd
import pdb
from math import sqrt

# driver code 
file_input=sys.argv[1]
data = pd.read_csv(file_input,header=None,delim_whitespace=True)

energy=list(data[1]) 
angle=list(data[0])

arr_ang=[]
arr_ener=[]
l=float(sys.argv[2])
r=float(sys.argv[3])

def standard_deviation(lst,both=True):
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_items
    variance = ssd / (num_items - 1)
    sd = sqrt(variance)
    if both==True:
        print mean, "\t",sd/sqrt(len(lst))
    else:
        print mean

for item in range(len(angle)):
        if angle[item] >=l and angle[item] <=r:
            arr_ang.append(angle[item])
            arr_ener.append(energy[item])
#print arr_ang
#print arr_ener
#print sum(arr_ener)/float(len(arr_ener))


standard_deviation(arr_ang,both=False)
standard_deviation(arr_ener,both=True)



        
