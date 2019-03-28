#2D-histogram plotting
#input:2-column data
import pdb
import numpy as np
import pandas as pd
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import matplotlib.colors

np.set_printoptions(threshold=np.inf)

data=pd.read_csv("dist_th_10ns.dat",header=None,delim_whitespace=True)
data2=pd.read_csv("try2.dat",header=None,delim_whitespace=True)
x=np.array(data[0])
y=np.array(data[1])
avg_pmf=np.array(data2[0])
#print (avg_pmf)

###2D-Histogram bining###
#########################
H,xedges,yedges,z=plt.hist2d(x,y,72,normed=True)
#np.place(H, H==0.00000000e+00, 1)
X, Y = np.meshgrid(xedges[0:-1], yedges[0:-1])
def centers(bins):
    return np.vstack([bins[:-1], bins[1:]]).mean(axis=0)


x_centers, y_centers = centers(xedges), centers(yedges)

#x_centers, y_centers = np.meshgrid(xedges,yedges)
###Free energy as a function of property###
###########################################
dg=-(0.0019872036*300)*np.log(H)
#print xedges
#print H
dg_min=(np.min(dg))
dgg=dg-dg_min
dgg1=np.transpose(dgg)
#pdb.set_trace()
dgg_new=np.add(avg_pmf,dgg1)
dgg_new1=np.transpose(dgg_new)
print dgg[0]
print dgg_new[0]
fig = plt.figure()
ax = plt.subplot(111, polar=False)
levels=np.array([0,1,2,4])
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["palegoldenrod","indianred","orange"])
cax = ax.contourf(X, Y, dgg_new1.T,4,linewidtgs=0.5)
fig.colorbar(cax, ax=ax)

plt.show()
