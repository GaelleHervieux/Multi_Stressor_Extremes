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

Tzone=['zoneA','zoneB','zoneC','zoneD','zoneE','zoneF','zoneG','zoneH']
# -------------------------------
# loop Zones
# -------------------------------
SSTz={}
SSTcz={}
SSTclimEz={}
SST90thEz={}
chlz={}
chlcz={}
chlclimEz={}
chl10thEz={}
hldz={}
hldcz={}
hldclimEz={}
hld10thEz={}
Tz={}
Tcz={}
TclimEz={}
T90thEz={}
SSTperz={}
Tperz={}
chlperz={}
hldperz={}
for izone in range(0,4):
  DS=xr.open_dataset(f'../DATA/Diags_timeseries_{Tzone[izone]}.nc')
  SSTz[f'SST{izone+1}']=DS['SST']
  SSTcz[f'SSTc{izone+1}']=DS['SST'].groupby('time.dayofyear').mean('time')
  SSTclimEz[f'SSTclimE{izone+1}']=DS['SST'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  SST90thEz[f'SST90thE{izone+1}']=DS['sst90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  SSTperz[f'SSTper{izone+1}']=DS['sMHW']
  chlz[f'chl{izone+1}']=DS['chl']
  chlcz[f'chlc{izone+1}']=DS['chl'].groupby('time.dayofyear').mean('time')
  chlclimEz[f'chlclimE{izone+1}']=DS['chl'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  chl10thEz[f'chl10thE{izone+1}']=DS['chl10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  chlperz[f'chlper{izone+1}']=DS['LCX']
  hldz[f'hld{izone+1}']=-DS['HLD']
  hldcz[f'hldc{izone+1}']=-DS['HLD'].groupby('time.dayofyear').mean('time')
  hldclimEz[f'hldclimE{izone+1}']=-DS['HLD'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  hld10thEz[f'hld10thE{izone+1}']=-DS['HLD10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  hldperz[f'hldper{izone+1}']=DS['SHX']
  Tz[f'T{izone+1}']=DS['botT']
  Tcz[f'Tc{izone+1}']=DS['botT'].groupby('time.dayofyear').mean('time')
  TclimEz[f'TclimE{izone+1}']=DS['botT'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  T90thEz[f'T90thE{izone+1}']=DS['botT90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  Tperz[f'Tper{izone+1}']=DS['bMHW']
  year=DS.indexes['time'].to_datetimeindex()
  nino34=DS['nino34']

unitssst='$\degree$C'
unitsT='$\degree$C'
unitschl='$mg$ $m^{-2}$'
unitshld='$m$'
Tvar=['SST','chl','HLD','botT']
Tunits=['$\degree$C','$mg$ $m^{-2}$','$m$','$\degree$C']
day2month=[0,31,59,90,120,151,181,212,243,273,304,334]
Nmonth=['J','F','M','A','M','J','J','A','S','O','N','D']


Tbox=[4,3,2,1]
widths = [4,0.25]
heights = [4,4, 4, 4,0.2]

# 2 - Plot

# SST
fig, axs = plt.subplots(nrows=5,ncols=2,gridspec_kw={'height_ratios':heights,'width_ratios':widths},
                        figsize=(16,8),num=2,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.02,top=0.85,left=0.2,right=0.95)
#
axs=axs.flatten()
for ix in range(0,4):
  axs[ix*2].plot(year,SSTz[f'SST{Tbox[ix]}'],color='red',linewidth=.75,label='daily')
  axs[ix*2].plot(year,SSTclimEz[f'SSTclimE{Tbox[ix]}'],color='red',linestyle='-.',linewidth=.45,label='climatology')
  axs[ix*2].plot(year,SST90thEz[f'SST90thE{Tbox[ix]}'],color='red',linestyle='dashed',linewidth=.45,label='percentile threshold')
  axs[ix*2].fill_between(year,SSTz[f'SST{Tbox[ix]}'],SST90thEz[f'SST90thE{Tbox[ix]}'],np.where(SSTperz[f'SSTper{Tbox[ix]}'],True,False),color='magenta', alpha=0.75)
  axs[ix*2].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix*2].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix*2].grid()
  axs[ix*2].set_yticklabels(axs[ix*2].get_yticklabels(),fontsize=17)
  axs[ix*2].text(-0.11, 0.5,unitsT,fontsize=17,transform=axs[ix*2].transAxes,rotation='vertical',va='center')
  axs[ix*2].text(-0.24,0.5,f'Zone {Tbox[ix]}',fontsize=20,transform=axs[ix*2].transAxes,rotation='horizontal',va='center')
  axs[ix*2].set_xlim(year[0],year[-1])
  axs[ix*2].set_xticklabels([])
  axs[ix*2].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  #axs[ib].set_ylim(6,27)
  f1=axs[ix*2].fill_between(year,axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1],np.where(SSTperz[f'SSTper{Tbox[ix]}']==1,True,False),\
          color='magenta', alpha=0.2,edgecolor=None,label='extreme event')
#
for ix in range(0,4):
  axs[ix*2+1].plot(np.arange(0,365),SSTcz[f'SSTc{Tbox[ix]}'],color='red',linestyle='-.',linewidth=.8)
  axs[ix*2+1].grid(color='silver',alpha=0.5)
  axs[ix*2+1].set_xlim(0,364)
  axs[ix*2+1].set_yticklabels('')
  axs[ix*2+1].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  axs[ix*2+1].set_xticks(day2month[1::2])
  if ix==3:
    axs[ix*2+1].set_xticklabels(Nmonth[1::2],fontsize=14)
  else:
    axs[ix*2+1].set_xticklabels([])#
axs[8].fill_between(year,0,0.1,np.where(nino34>1,True,False),color='sienna',alpha=0.75,label='El Ni\xf1o')
axs[8].fill_between(year,0,0.1,np.where(nino34<-1,True,False),color='teal',alpha=0.75,label='La Ni\xf1a')
axs[8].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
axs[8].xaxis.set_minor_formatter(plt.NullFormatter())
axs[8].grid()
axs[8].set_ylim(0,0.1)
axs[8].set_xticklabels(axs[8].get_xticklabels(),fontsize=17)
axs[8].set_xlim(year[0],year[-1])
axs[8].set_yticklabels([])
axs[8].set_yticks([])
plt.xlabel('')
axs[9].axis('off')
handles1, labels1 = axs[0].get_legend_handles_labels()
handles2, labels2 = axs[8].get_legend_handles_labels()
handles=handles1+handles2
labels=labels1+labels2
fig.legend(handles, labels, loc='upper right',ncol=6,bbox_to_anchor=(0.95,0.94),prop={'size': 16})
fig.suptitle(f'SST',fontsize=20)
outfile=f'Timeseries_SST_zones1234.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

# ∫chl

fig, axs = plt.subplots(nrows=5,ncols=2,gridspec_kw={'height_ratios':heights,'width_ratios':widths},
                        figsize=(16,8),num=2,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.02,top=0.85,left=0.2,right=0.95)
#
axs=axs.flatten()
for ix in range(0,4):
  axs[ix*2].plot(year,chlz[f'chl{Tbox[ix]}'],color='green',linewidth=.75,label='daily')
  axs[ix*2].plot(year,chlclimEz[f'chlclimE{Tbox[ix]}'],color='green',linestyle='-.',linewidth=.45,label='climatology')
  axs[ix*2].plot(year,chl10thEz[f'chl10thE{Tbox[ix]}'],color='green',linestyle='dashed',linewidth=.45,label='percentile threshold')
  axs[ix*2].fill_between(year,chlz[f'chl{Tbox[ix]}'],chl10thEz[f'chl10thE{Tbox[ix]}'],np.where(chlperz[f'chlper{Tbox[ix]}'],True,False),\
          color='darkorange', alpha=0.75)
  axs[ix*2].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix*2].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix*2].grid()
  axs[ix*2].set_yticklabels(axs[ix*2].get_yticklabels(),fontsize=17)
  axs[ix*2].text(-0.11,0.5,unitschl,fontsize=17,transform=axs[ix*2].transAxes,rotation='vertical',va='center')
  axs[ix*2].text(-0.24,0.5,f'Zone {Tbox[ix]}',fontsize=20,transform=axs[ix*2].transAxes,rotation='horizontal',va='center')
  axs[ix*2].set_xlim(year[0],year[-1])
  axs[ix*2].set_xticklabels([])
  axs[ix*2].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  #axs[ib].set_ylim(6,27)
  f1=axs[ix*2].fill_between(year,axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1],np.where(chlperz[f'chlper{Tbox[ix]}']==1,True,False),\
          color='darkorange', alpha=0.3,edgecolor=None,label='extreme event')
#
for ix in range(0,4):
  axs[ix*2+1].plot(np.arange(0,365),chlcz[f'chlc{Tbox[ix]}'],color='green',linestyle='-.',linewidth=.8)
  axs[ix*2+1].grid(color='silver',alpha=0.5)
  axs[ix*2+1].set_xlim(0,364)
  axs[ix*2+1].set_yticklabels('')
  axs[ix*2+1].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  axs[ix*2+1].set_xticks(day2month[1::2])
  if ix==3:
    axs[ix*2+1].set_xticklabels(Nmonth[1::2],fontsize=14)
  else:
    axs[ix*2+1].set_xticklabels([])
axs[8].fill_between(year,0,0.1,np.where(nino34>1,True,False),color='sienna',alpha=0.75,label='El Ni\xf1o')
axs[8].fill_between(year,0,0.1,np.where(nino34<-1,True,False),color='teal',alpha=0.75,label='La Ni\xf1a')
axs[8].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
axs[8].xaxis.set_minor_formatter(plt.NullFormatter())
axs[8].grid()
axs[8].set_ylim(0,0.1)
axs[8].set_xticklabels(axs[8].get_xticklabels(),fontsize=17)
axs[8].set_xlim(year[0],year[-1])
axs[8].set_yticklabels([])
axs[8].set_yticks([])
plt.xlabel('')
axs[9].axis('off')
handles1, labels1 = axs[0].get_legend_handles_labels()
handles2, labels2 = axs[8].get_legend_handles_labels()
handles=handles1+handles2
labels=labels1+labels2
fig.legend(handles, labels, loc='upper right',ncol=6,bbox_to_anchor=(0.95,0.94),prop={'size': 16})
fig.suptitle(f'$\int$CHL',fontsize=20)
outfile=f'Timeseries_CHL_zones1234.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

# HLD

fig, axs = plt.subplots(nrows=5,ncols=2,gridspec_kw={'height_ratios':heights,'width_ratios':widths},
                        figsize=(16,8),num=2,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.02,top=0.85,left=0.2,right=0.95)
#
axs=axs.flatten()
for ix in range(0,4):
  axs[ix*2].plot(year,hldz[f'hld{Tbox[ix]}'],color='blue',linewidth=.75,label='daily')
  axs[ix*2].plot(year,hldclimEz[f'hldclimE{Tbox[ix]}'],color='blue',linestyle='-.',linewidth=.45,label='climatology')
  axs[ix*2].plot(year,hld10thEz[f'hld10thE{Tbox[ix]}'],color='blue',linestyle='dashed',linewidth=.45,label='percentile threshold')
  axs[ix*2].fill_between(year,hldz[f'hld{Tbox[ix]}'],hld10thEz[f'hld10thE{Tbox[ix]}'],np.where(hldperz[f'hldper{Tbox[ix]}'],True,False),\
          color='cyan', alpha=0.75)
  axs[ix*2].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix*2].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix*2].grid()
  axs[ix*2].set_yticklabels(axs[ix*2].get_yticklabels(),fontsize=17)
  axs[ix*2].set_yticklabels([round(-ix) for ix in axs[ix*2].get_yticks()],fontsize=17)
  axs[ix*2].text(-0.11, 0.5,unitshld,fontsize=17,transform=axs[ix*2].transAxes,rotation='vertical',va='center')
  axs[ix*2].text(-0.24,0.5,f'Zone {Tbox[ix]}',fontsize=20,transform=axs[ix*2].transAxes,rotation='horizontal',va='center')
  axs[ix*2].set_xlim(year[0],year[-1])
  axs[ix*2].set_xticklabels([])
  axs[ix*2].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  #axs[ib].set_ylim(6,27)
  f1=axs[ix*2].fill_between(year,axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1],np.where(hldperz[f'hldper{Tbox[ix]}']==1,True,False),\
          color='cyan', alpha=0.3,edgecolor=None,label='extreme event')
#
for ix in range(0,4):
  axs[ix*2+1].plot(np.arange(0,365),hldcz[f'hldc{Tbox[ix]}'],color='blue',linestyle='-.',linewidth=.8)
  axs[ix*2+1].grid(color='silver',alpha=0.5)
  axs[ix*2+1].set_xlim(0,364)
  axs[ix*2+1].set_yticklabels('')
  axs[ix*2+1].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  axs[ix*2+1].set_xticks(day2month[1::2])
  if ix==3:
    axs[ix*2+1].set_xticklabels(Nmonth[1::2],fontsize=14)
  else:
    axs[ix*2+1].set_xticklabels([])
#
axs[8].fill_between(year,0,0.1,np.where(nino34>1,True,False),color='sienna',alpha=0.75,label='El Ni\xf1o')
axs[8].fill_between(year,0,0.1,np.where(nino34<-1,True,False),color='teal',alpha=0.75,label='La Ni\xf1a')
axs[8].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
axs[8].xaxis.set_minor_formatter(plt.NullFormatter())
axs[8].grid()
axs[8].set_ylim(0,0.1)
axs[8].set_xticklabels(axs[8].get_xticklabels(),fontsize=17)
axs[8].set_xlim(year[0],year[-1])
axs[8].set_yticklabels([])
axs[8].set_yticks([])
plt.xlabel('')
axs[9].axis('off')
handles1, labels1 = axs[0].get_legend_handles_labels()
handles2, labels2 = axs[8].get_legend_handles_labels()
handles=handles1+handles2
labels=labels1+labels2
fig.legend(handles, labels, loc='upper right',ncol=6,bbox_to_anchor=(0.95,0.94),prop={'size': 16})
fig.suptitle(f'HLD',fontsize=20)
outfile=f'Timeseries_HLD_zones1234.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

# Bottom Temperature

fig, axs = plt.subplots(nrows=5,ncols=2,gridspec_kw={'height_ratios':heights,'width_ratios':widths},
                        figsize=(16,8),num=2,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.02,top=0.85,left=0.2,right=0.95)
axs=axs.flatten()
for ix in range(0,4):
  axs[ix*2].plot(year,Tz[f'T{Tbox[ix]}'],color='k',linewidth=.75,label='daily')
  axs[ix*2].plot(year,TclimEz[f'TclimE{Tbox[ix]}'],color='k',linestyle='-.',linewidth=.45,label='climatology')
  axs[ix*2].plot(year,T90thEz[f'T90thE{Tbox[ix]}'],color='k',linestyle='dashed',linewidth=.45,label='percentile threshold')
  axs[ix*2].fill_between(year,Tz[f'T{Tbox[ix]}'],T90thEz[f'T90thE{Tbox[ix]}'],np.where(Tperz[f'Tper{Tbox[ix]}'],True,False),color='red', alpha=0.75)
  axs[ix*2].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
  axs[ix*2].xaxis.set_minor_formatter(plt.NullFormatter())
  axs[ix*2].grid()
  axs[ix*2].set_yticklabels(axs[ix*2].get_yticklabels(),fontsize=17)
  axs[ix*2].text(-0.11, 0.5,unitsT,fontsize=17,transform=axs[ix*2].transAxes,rotation='vertical',va='center')
  axs[ix*2].text(-0.24,0.5,f'Zone {Tbox[ix]}',fontsize=20,transform=axs[ix*2].transAxes,rotation='horizontal',va='center')
  axs[ix*2].set_xlim(year[0],year[-1])
  axs[ix*2].set_xticklabels([])
  axs[ix*2].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  #axs[ib].set_ylim(6,27)
  f1=axs[ix*2].fill_between(year,axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1],np.where(Tperz[f'Tper{Tbox[ix]}'],True,False),\
          color='red', alpha=0.2,edgecolor=None,label='extreme event')
#

for ix in range(0,4):
  axs[ix*2+1].plot(np.arange(0,365),Tcz[f'Tc{Tbox[ix]}'],color='k',linestyle='-.',linewidth=.8)
  axs[ix*2+1].grid(color='silver',alpha=0.5)
  axs[ix*2+1].set_xlim(0,364)
  axs[ix*2+1].set_yticklabels('')
  axs[ix*2+1].set_ylim(axs[ix*2].get_ylim()[0],axs[ix*2].get_ylim()[1])
  axs[ix*2+1].set_xticks(day2month[1::2])
  if ix==3:
    axs[ix*2+1].set_xticklabels(Nmonth[1::2],fontsize=14)
  else:
    axs[ix*2+1].set_xticklabels([])
axs[8].fill_between(year,0,0.1,np.where(nino34>1,True,False),color='sienna',alpha=0.75,label='El Ni\xf1o')
axs[8].fill_between(year,0,0.1,np.where(nino34<-1,True,False),color='teal',alpha=0.75,label='La Ni\xf1a')
axs[8].xaxis.set_minor_locator(mdates.YearLocator(1, month = 1, day = 1))
axs[8].xaxis.set_minor_formatter(plt.NullFormatter())
axs[8].grid()
axs[8].set_ylim(0,0.1)
axs[8].set_xticklabels(axs[8].get_xticklabels(),fontsize=17)
axs[8].set_xlim(year[0],year[-1])
axs[8].set_yticklabels([])
axs[8].set_yticks([])
plt.xlabel('')
axs[9].axis('off')
handles1, labels1 = axs[0].get_legend_handles_labels()
handles2, labels2 = axs[8].get_legend_handles_labels()
handles=handles1+handles2
labels=labels1+labels2
fig.legend(handles, labels, loc='upper right',ncol=6,bbox_to_anchor=(0.95,0.94),prop={'size': 16})
fig.suptitle(f'Bottom Temperature',fontsize=20)
outfile=f'Timeseries_botT_zones1234.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
