# Created by Gaelle Hervieux
#
# Generate Spatial extent of single and compound extremes across the CCLME figure.

# Figure 10: Spatial extent of single and compound extremes across the CCLME. Time series of the 
# total area affected by single (top panels) and compound (bottom panels) extremes, expressed as 
# a percentage of the (a) CCLME, (b) offshore (making up 34.8% of the CCLME), and (c) nearshore 
# (making up 13.9% of the CCLME). Note, y-axes ranges for compound extremes (bottom panels) differ 
# between regions.  

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.lines import Line2D
import copy

# 1 - Read Data
 
ds=xr.open_dataset('../DATA/SpatialExtent.nc')
# CCLME
Tlme=ds['Tlme']
Clme=ds['Clme']
Hlme=ds['Hlme']
TClme=ds['TClme']
THlme=ds['THlme']
HClme=ds['HClme']
THClme=ds['THClme']
# Nearshore CCLME 
Tlme75=ds['Tlme75']
Clme75=ds['Clme75']
Hlme75=ds['Hlme75']
TClme75=ds['TClme75']
THlme75=ds['THlme75']
HClme75=ds['HClme75']
THClme75=ds['THClme75']
# Offshore CCLME
Tlme75300=ds['Tlme75300']
Clme75300=ds['Clme75300']
Hlme75300=ds['Hlme75300']
TClme75300=ds['TClme75300']
THlme75300=ds['THlme75300']
HClme75300=ds['HClme75300']
THClme75300=ds['THClme75300']
year=ds.indexes['time'].to_datetimeindex()

STtitle=['SMHW','LCX','SHX']
MTtitle=['SMHW-LCX','LCX-SHX','SMHW-SHX','SMHW-LCX-SHX']
Scolors=['xkcd:burnt umber','xkcd:sage','xkcd:barney purple']
Mcolors=['xkcd:orange','xkcd:green','xkcd:orchid','black']

# 2 - Plot

# CCLME
TSarea=[Tlme,Clme,Hlme]
TMarea=[TClme,HClme,THlme,THClme]

fig, axs = plt.subplots(nrows=2,ncols=1,
                        figsize=(12,8),num=2,clear=True)
fig.subplots_adjust(hspace=.5,wspace=.2,top=0.8)
axs=axs.flatten()
for iarea in range(0,len(TSarea)):
  axs[0].plot(year,TSarea[iarea],color=Scolors[iarea],linewidth=.75,label=f'{STtitle[iarea]}')
for iarea in range(0,len(TMarea)):
  axs[1].plot(year,TMarea[iarea],color=Mcolors[iarea],linewidth=.75,label=f'{MTtitle[iarea]}')
axs[0].set_ylim(0,100)
axs[1].set_ylim(0,35)
for ix in range(0,2):
  axs[ix].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix].grid()
  axs[ix].set_yticklabels(axs[ix].get_yticklabels(),fontsize=17)
  axs[ix].set_xlim(year[0],year[-1])
  axs[ix].set_ylabel('',fontsize=17)
axs[0].set_xticklabels('',fontsize=17)
axs[1].set_xticklabels(axs[1].get_xticklabels(),fontsize=17)
handles, labels = axs[0].get_legend_handles_labels()
handles = [copy.copy(ha) for ha in handles ]
# set the linewidths to the copies
[ha.set_linewidth(3) for ha in handles ]
axs[0].legend(handles, labels, loc='upper center',ncols=len(TSarea),bbox_to_anchor=(0.5,1.45), prop={'size': 18})
handles, labels = axs[1].get_legend_handles_labels()
handles = [copy.copy(ha) for ha in handles ]
# set the linewidths to the copies
[ha.set_linewidth(3) for ha in handles ]
axs[1].legend(handles, labels, loc='upper center',ncols=len(TMarea), bbox_to_anchor=(0.5,1.45), prop={'size': 18})
axs[1].text(-0.12, 1.5,'Area Affected (%)',fontsize=18,transform=axs[1].transAxes,rotation='vertical',va='center')
fig.suptitle(f'CCLME', fontsize=18)
outfile=f'SpatialExtent_CCLME.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

# Nearshore CCLME 

TSarea75=[Tlme75,Clme75,Hlme75]
TMarea75=[TClme75,HClme75,THlme75,THClme75]

fig, axs = plt.subplots(nrows=2,ncols=1,
                        figsize=(12,8),num=2,clear=True)
fig.subplots_adjust(hspace=.5,wspace=.2,top=0.8)
axs=axs.flatten()
for iarea in range(0,len(TSarea75)):
  axs[0].plot(year,TSarea75[iarea],color=Scolors[iarea],linewidth=.75,label=f'{STtitle[iarea]}')
for iarea in range(0,len(TMarea75)):
  axs[1].plot(year,TMarea75[iarea],color=Mcolors[iarea],linewidth=.75,label=f'{MTtitle[iarea]}')
axs[0].set_ylim(0,100)
axs[1].set_ylim(0,60)
for ix in range(0,2):
  axs[ix].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix].grid()
  axs[ix].set_yticklabels(axs[ix].get_yticklabels(),fontsize=17)
  axs[ix].set_xlim(year[0],year[-1])
  axs[ix].set_ylabel('',fontsize=18)
axs[0].set_xticklabels('',fontsize=18)
axs[1].set_xticklabels(axs[1].get_xticklabels(),fontsize=17)
handles, labels = axs[0].get_legend_handles_labels()
handles = [copy.copy(ha) for ha in handles ]
# set the linewidths to the copies
[ha.set_linewidth(3) for ha in handles ]
axs[0].legend(handles, labels, loc='upper center',ncols=len(TSarea),bbox_to_anchor=(0.5,1.4), prop={'size': 18})
handles, labels = axs[1].get_legend_handles_labels()
handles = [copy.copy(ha) for ha in handles ]
# set the linewidths to the copies
[ha.set_linewidth(3) for ha in handles ]
axs[1].legend(handles, labels, loc='upper center',ncols=len(TMarea), bbox_to_anchor=(0.5,1.4), prop={'size': 18})
axs[1].text(-0.12, 1.5,'Area Affected (%)',fontsize=18,transform=axs[1].transAxes,rotation='vertical',va='center')
fig.suptitle(f'Nearshore CCLME ', fontsize=18)
outfile=f'SpatialExtent_CCLME_nearshore.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')


# Nearshore CCLME 

TSarea75300=[Tlme75300,Clme75300,Hlme75300]
TMarea75300=[TClme75300,HClme75300,THlme75300,THClme75300]

fig, axs = plt.subplots(nrows=2,ncols=1,
                        figsize=(12,8),num=2,clear=True)
fig.subplots_adjust(hspace=.5,wspace=.2,top=0.8)
axs=axs.flatten()
for iarea in range(0,len(TSarea75)):
  axs[0].plot(year,TSarea75300[iarea],color=Scolors[iarea],linewidth=.75,label=f'{STtitle[iarea]}')
for iarea in range(0,len(TMarea75)):
  axs[1].plot(year,TMarea75300[iarea],color=Mcolors[iarea],linewidth=.75,label=f'{MTtitle[iarea]}')
axs[0].set_ylim(0,100)
axs[1].set_ylim(0,60)
for ix in range(0,2):
  axs[ix].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix].grid()
  axs[ix].set_yticklabels(axs[ix].get_yticklabels(),fontsize=17)
  axs[ix].set_xlim(year[0],year[-1])
  axs[ix].set_ylabel('',fontsize=18)
axs[0].set_xticklabels('',fontsize=18)
axs[1].set_xticklabels(axs[1].get_xticklabels(),fontsize=17)
handles, labels = axs[0].get_legend_handles_labels()
handles = [copy.copy(ha) for ha in handles ]
# set the linewidths to the copies
[ha.set_linewidth(3) for ha in handles ]
axs[0].legend(handles, labels, loc='upper center',ncols=len(TSarea),bbox_to_anchor=(0.5,1.4), prop={'size': 18})
handles, labels = axs[1].get_legend_handles_labels()
handles = [copy.copy(ha) for ha in handles ]
# set the linewidths to the copies
[ha.set_linewidth(3) for ha in handles ]
axs[1].legend(handles, labels, loc='upper center',ncols=len(TMarea), bbox_to_anchor=(0.5,1.4), prop={'size': 18})
axs[1].text(-0.12, 1.5,'Area Affected (%)',fontsize=18,transform=axs[1].transAxes,rotation='vertical',va='center')
fig.suptitle(f'Offshore CCLME ', fontsize=18)
outfile=f'SpatialExtent_CCLME_offshore.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
