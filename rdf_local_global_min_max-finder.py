import sys
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import savitzy_gorlay as sv_g
from scipy.signal import argrelextrema

xurea=[]
yurea=[]

########extracting data till cut-off and smoothening of RDFs#######
###################################################################


u = open(sys.argv[1],"r") #user RDF file
for i in u.readlines():
        columns = i.split()
	if (float(columns[0]) <=10.0):
		yurea.append((float(columns[1])))
        	xurea.append(float(columns[0]))

y = np.array(yurea)
x = np.array(xurea)
yhat = sv_g.savitzky_golay(y, 11, 3) ### savitky_golay filter for smoothening
urea_rdf=yhat

######finding global_maximum######
##################################

max1=np.amax(urea_rdf)

for i in range(0,len(urea_rdf)):
	if(urea_rdf[i]==np.amax(urea_rdf)):
		print "gmax1 rmax1", urea_rdf[i], x[i]
		gmax1_index=i


#####finding local minimas######
################################
indirect_rdf=[]
indirect_x=[]
for i in range(gmax1_index,len(urea_rdf-1)):
			indirect_rdf.append(urea_rdf[i])
			indirect_x.append(x[i])


local_minima_indices=argrelextrema(np.array(indirect_rdf), np.less)

rmin1_index=local_minima_indices[0][0]

print "gmin1 rmin1", np.array(indirect_rdf)[argrelextrema(np.array(indirect_rdf), np.less)[0][0]], indirect_x[8]		

#####Smoothened_RDF_plot######
##############################	
plt.plot(x,yhat, color = "black")

plt.show()
