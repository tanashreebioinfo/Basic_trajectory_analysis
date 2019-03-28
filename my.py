import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import matplotlib.colors
import glob
import matplotlib as mpl
txtfiles = []

for file in glob.glob("imino_sasa_th_10ns.dat"):
        txtfiles.append(file)

#f=sys.argv[1]
#files=["solv_tg","solv_"]
for i in txtfiles:
        data = pd.read_csv(i,header=None,delim_whitespace=True)
        print i                       
        energy=np.array(list(data[1]))
        angle=np.array(list(data[0]))

        r_bins = np.linspace(np.min(energy), np.max(energy), 100)

        # add 180 to all angles and convert to radians, because polar plot needs 0 to 360
        angle += 0.0
        angle = np.radians(angle)
        #print(np.min(angle), np.max(angle))

        #angle_bins

        n_theta = 100
        d_theta = 2. * np.pi / (n_theta + 1.)
        theta_bins = np.linspace(-d_theta / 2., 2. * np.pi + d_theta / 2., n_theta)

        H, theta_edges, r_edges = np.histogram2d(angle % (2. * np.pi), energy, bins = (theta_bins, r_bins),normed=True)
        H_normalized = H/float(energy.shape[0])
        print H_normalized
        #plot data in the middle of the bins
        r_mid     = .5 * (r_edges[:-1] + r_edges[1:])
        theta_mid = .5 * (theta_edges[:-1] + theta_edges[1:])

        fig = plt.figure()
        ax = plt.subplot(111, polar=True)
        levels=np.array([0,0.25,0.75,1.0])
        print levels

        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["palegoldenrod","indianred","maroon","darkred"])
        #cax = ax.contourf(theta_mid, r_mid, H.T,5,level=[-1,0-1],cmap=plt.cm.Spectral,extend='both')
        cax = ax.contourf(theta_mid, r_mid, H_normalized.T,5,cmap=cmap,linewidths=0.5,extend='both',levels=levels)
        #ax.scatter(angle, energy, color='k', marker='+')
        #ax.set_rmax(1)
        #cax.set_clim(0,1)
        #v = np.linspace(0.0, 1.0,5,endpoint=True) 


        fig.colorbar(cax, ax=ax) 
        

        # Convert ticks back to -180 to +180 scale
        #print(ax.get_xticks())
        angle_labels = [float(item) for item in ax.get_xticks(minor=False)]

        for j, _ in enumerate(angle_labels):
            if angle_labels[j] > np.pi:
                angle_labels[j] = -(2*np.pi - angle_labels[j])
            angle_labels[j] = np.rad2deg(angle_labels[j])

        ax.set_xticklabels(angle_labels, fontsize=20)
        ax.tick_params(axis='both',labelsize=8,width=0.5)
        ax.grid(True)
        plt.rcParams['axes.labelsize'] = 16
        plt.rcParams['axes.labelweight'] = 'bold'

        #fig.savefig('dist_{0}.png'.format(i),dpi=300)
        
        #figManager = plt.get_current_fig_manager()
        #figManager.full_screen_toggle() 
        fig = plt.gcf()
        fig.set_size_inches((8,6), forward=False)

        fig.savefig(str(i)+".eps",format="eps", dpi=300)
        

        plt.show()

