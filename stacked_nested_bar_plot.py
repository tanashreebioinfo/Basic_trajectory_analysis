import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_clustered_stacked(dfall, labels=None, title=" ",  H="/", **kwargs):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns) 
    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=0,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
		      fontsize=15,
                      **kwargs)  # make bar plots
	
 
    h,l = axe.get_legend_handles_labels() # get the handles we want to modify

    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                rect.set_hatch(H * int(i / n_col)) #edited part     
                rect.set_width(1 / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(df.index, rotation = 0,size=22)
    axe.set_title(title)

    # Add invisible data to add another legend
    n=[]        
    for i in range(n_df):
        n.append(axe.bar(0, 0, color="gray", hatch=H * i))

    l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
    if labels is not None:
        l2 = plt.legend(n, labels, loc=[1.01, 0.1]) 
    axe.add_artist(l1)
    plt.show()	
    return axe
#####customised colormap##########
##################################
colors = [(0, 0, 0), (0.5, 0, 0), (1, 1, 1)]
n_bins = [3, 6, 10, 100]  # Discretizes the interpolation into bins
cmap_name = 'my_list'
fig, axs = plt.subplots(2, 2, figsize=(9, 12))
fig.subplots_adjust(left=0.02, bottom=0.06, right=0.95, top=0.94, wspace=0.05)
for n_bin, ax in zip(n_bins, axs.ravel()):
    # Create the colormap
    cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=n_bin)
###################################

f1 = np.loadtxt('lpd_dna_sod_all.txt', usecols=range(1))
f2 = np.loadtxt('lpd_dna_cla_all.txt', usecols=range(1))
m1= np.transpose(np.reshape(f1, (3, 8)))
m2= np.transpose(np.reshape(f2, (3, 8)))

df1 = pd.DataFrame(m1,index=[2,3,4,5,6,7,8,9],columns=["150mM","500mM","1000mM"])
df2 = pd.DataFrame(m2,index=[2,3,4,5,6,7,8,9],columns=["150mM","500mM","1000mM"])

#plot_clustered_stacked([df1, df2],["Na+", "Cl+"],cmap=plt.cm.viridis) #or cmap=cm
plot_clustered_stacked([df1, df2],["Na+", "Cl+"],color=("DarkBlue","teal", "DarkSeaGreen"))

