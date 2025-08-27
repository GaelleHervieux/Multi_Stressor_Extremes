# Created by Gaelle Hervieux
#
# Generate Temporal variability of nearshore ocean extremes and their relationship to ENSO phases figure.

# Figure 8: Temporal variability of nearshore ocean extremes and their relationship to ENSO phases. 
# Daily time series (1996–2019; solid contours) of (a) SST (red), (b) ∫Chl (green), (c) HLD (blue; 
# inverted y-axis), and (d) bottom temperature (BT; black) regionally-averaged over the nearshore 
# (0–75 km) coastal band (zones 1–4). Additional contours in (a)-(d) show the daily climatology (dotted-dashed) 
# and seasonally-varying percentile threshold (dashed; 90th for temperature, 10th otherwise). Extreme events 
# of each ocean variable are indicated with under-the-curve and vertical shading. The duration of simulated 
# El Niño (brown) and La Niña (teal) phases are indicated along the time (x) axis in (a)-(d), defined when 
# the GLORYS-BGC Niño 3.4 index exceeds ±1 standard deviation. (e-h) The same climatology shown in (a)-(d) 
# is presented and enlarged as a single annual cycle beginning January 1, respectively.  

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.lines import Line2D

# 1 - Read Data
# 
ds=xr.open_dataset('../DATA/Timeseries_CCLME_0-75km.nc')
SSTz=ds['SST']
SSTc=ds['SST'].groupby('time.dayofyear').mean('time')
SSTclimEz=ds['SST'].groupby('time.dayofyear').mean('time').sel(dayofyear=ds['SST'].time.dt.dayofyear)
SST90thEz=ds['sst90th'].sel(dayofyear=ds['SST'].time.dt.dayofyear)
sMHW=ds['sMHW']
chlz=ds['chl']
chlc=ds['chl'].groupby('time.dayofyear').mean('time')
chlclimEz=ds['chl'].groupby('time.dayofyear').mean('time').sel(dayofyear=ds['SST'].time.dt.dayofyear)
chl10thEz=ds['chl10th'].sel(dayofyear=ds['SST'].time.dt.dayofyear)
LCX=ds['LCX']
hldz=-ds['HLD']
hldc=-ds['HLD'].groupby('time.dayofyear').mean('time')
hldclimEz=-ds['HLD'].groupby('time.dayofyear').mean('time').sel(dayofyear=ds['SST'].time.dt.dayofyear)
hld10thEz=-ds['HLD10th'].sel(dayofyear=ds['SST'].time.dt.dayofyear)
SHX=ds['SHX']
Tz=ds['botT']
Tbc=ds['botT'].groupby('time.dayofyear').mean('time')
TclimEz=ds['botT'].groupby('time.dayofyear').mean('time').sel(dayofyear=ds['SST'].time.dt.dayofyear)
T90thEz=ds['botT90th'].sel(dayofyear=ds['SST'].time.dt.dayofyear)
bMHW=ds['bMHW']
nino34=ds['nino34']

year=ds.indexes['time'].to_datetimeindex()

unitssst='$\degree$C'
unitsT='$\degree$C'
unitschl='$mg m-2$'
unitso2='$m$'
Tvar=['SST','chl','HLD','botT']
Tunits=['$\degree$C','$mg m-2$','$m$','$\degree$C']
day2month=[0,31,59,90,120,151,181,212,243,273,304,334]
Nmonth=['J','F','M','A','M','J','J','A','S','O','N','D']
Tlabel1=['SST','chlIntV : chl (0-100m)','Hypoxic Layer','Bottom Temp']
Tlabel2=['90th percentile','10th percentile','10th percentile','90th percentile']
Tcolors1=['red','green','blue','black']
Tcolors2=['magenta','darkorange','cyan','red']
Tcolors3=['magenta','orange','cyan','red']
T=[SSTz,chlz,hldz,Tz]
Tc=[SSTc,chlc,hldc,Tbc]
T90=[SST90thEz,chl10thEz,hld10thEz,T90thEz]
Tclim=[SSTclimEz,chlclimEz,hldclimEz,TclimEz]
Tper=[sMHW,LCX,SHX,bMHW]
Tbox=[0.2,0.4,0.6,0.8]
widths = [4,0.25]
heights = [4,4, 4, 4,0.2]

# 2 - Plot

fig, axs =\
plt.subplots(nrows=5,ncols=2,gridspec_kw={'height_ratios':heights,'width_ratios':widths},
                        figsize=(16,8),num=2,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.02,top=0.8)
axs=axs.flatten()
#
for ix in range(0,4):
  axs[ix*2].plot(year,T[ix],color=Tcolors1[ix],linewidth=.8,label=Tlabel1[ix])
  axs[ix*2].plot(year,T90[ix],color=Tcolors1[ix],linestyle='--',linewidth=.45,label=Tlabel2[ix])
  axs[ix*2].plot(year,Tclim[ix],Tcolors1[ix],linestyle='-.',linewidth=.45,label='Seasonal Cycle')
  axs[ix*2].fill_between(year,T[ix],T90[ix],np.where(Tper[ix]==1,True,False),color=Tcolors2[ix], alpha=0.75)
  axs[ix*2].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix*2].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix*2].grid()
  axs[ix*2].set_yticklabels(axs[ix*2].get_yticklabels(),fontsize=17)
  axs[ix*2].text(-0.12, 0.5,Tunits[ix],fontsize=17,transform=axs[ix*2].transAxes,rotation='vertical',va='center')
  axs[ix*2].set_xlim(year[0],year[-1])
  axs[ix*2].set_xticklabels([])
  axs[ix*2].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  f1=axs[ix*2].fill_between(year,axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1],\
            np.where(Tper[ix]==1,True,False), color=Tcolors3[ix], alpha=0.2,edgecolor=None)
  handles, labels = axs[ix*2].get_legend_handles_labels()
  fig.legend(handles, labels, loc='upper center',ncol=1,bbox_to_anchor=(Tbox[ix],0.9), prop={'size': 9})
#
for ix in range(0,4):
  axs[ix*2+1].plot(np.arange(0,365),Tc[ix],color=Tcolors1[ix],linestyle='-.',linewidth=.8)
  axs[ix*2+1].grid(color='silver',alpha=0.5)
  axs[ix*2+1].set_xlim(0,364)
  axs[ix*2+1].set_yticklabels('')
  axs[ix*2+1].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  axs[ix*2+1].set_xticks(day2month[1::2])
  if ix==3:
    axs[ix*2+1].set_xticklabels('',fontsize=17)
  else:
    axs[ix*2+1].set_xticklabels([])
#
axs[8].fill_between(year,0,0.1,np.where(nino34>1,True,False),color='sienna', alpha=0.75)
axs[8].fill_between(year,0,0.1,np.where(nino34<-1,True,False),color='teal', alpha=0.75)
axs[8].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
axs[8].xaxis.set_minor_formatter(plt.NullFormatter())
axs[8].grid()
axs[8].set_xlim(9495,18261)
axs[8].set_xticklabels(axs[8].get_xticklabels(),fontsize=17)
axs[8].set_ylim(0,0.1)
axs[8].set_yticklabels([])
axs[8].set_yticks([])
axs[9].axis('off')
plt.xlabel('')
outfile=f'Timeseries_CCLME_0-75km.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
