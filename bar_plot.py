import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 3
menMeans = [-28.983,-28.922,-28.985]
menStd =   [0.030511, 0.050821, 0.053277]
womenMeans = [-10.282,-10.302,-10.275]
womenStd =   [0.018701,0.029029,0.011453]
womenMeans2 = [-18.7,-18.647,-18.684]
womenStd2 =   [0.029805,0.055267,0.05333]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars

## the bars
rects1 = ax.bar(ind, menMeans, width,
                color='navy',
                yerr=menStd,
                error_kw=dict(elinewidth=2,ecolor='black'))

rects2 = ax.bar(ind+width, womenMeans, width,
                    color='teal',
                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='black'))



rects3 = ax.bar(ind+2*width, womenMeans2, width,
                    color='yellowgreen',
                    yerr=womenStd2,
                    error_kw=dict(elinewidth=2,ecolor='black'))

# axes and labels
ax.set_xlim(-width,len(ind)+width)
#ax.set_ylim(0,45)
ax.set_ylabel('Energy (kcal/mol)')
ax.set_title('Trp-8M')
xTickMarks = ['set'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0],rects3[0]), ('total', 'ele' ,'vdw') )

plt.show()


