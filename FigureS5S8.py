import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.lines import Line2D

dirout=''
dirdata=''


## ###############################
##  OPEN DATASETS
## ###############################
# -------------------------------
# loop Zones
# -------------------------------
SSTz={}
SSTclimEz={}
SST90thEz={}
chlz={}
chlclimEz={}
chl10thEz={}
o2z={}
o2climEz={}
o210thEz={}
Tz={}
TclimEz={}
T90thEz={}

for izone in range(0,4):
  DS=xr.open_dataset(f'{dirdata}/Diags_timeseries_{Tzone[izone]}.nc')
  SSTz[f'SST{izone+1}']=DS['SST']
  SSTclimEz[f'SSTclimE{izone+1}']=DS['SST'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  SST90thEz[f'SST90thE{izone+1}']=DS['sst90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  chlz[f'chl{izone+1}']=DS['chl']
  chlclimEz[f'chlclimE{izone+1}']=DS['chl'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  chl10thEz[f'chl10thE{izone+1}']=DS['chl10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  o2z[f'o2{izone+1}']=DS['HLD']
  o2climEz[f'o2climE{izone+1}']=DS['HLD'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  o210thEz[f'o210thE{izone+1}']=DS['HLD10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  Tz[f'T{izone+1}']=DS['botT']
  TclimEz[f'TclimE{izone+1}']=DS['botT'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
  T90thEz[f'T90thE{izone+1}']=DS['botT90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
  year=DS.indexes['time'].to_datetimeindex()
  yeare=year[0]
  yearb=year[-1]


############################
# PLOT SST
############################
fig, axs = plt.subplots(nrows=4,ncols=1)
#
for ib in range(3,-1,-1):
  axs[ib].plot(year,SSTz[f'SST{4-ib}'],color='red',linewidth=.75,label='daily')
  axs[ib].plot(year,SSTclimEz[f'SSTclimE{4-ib}'],color='red',linestyle='dotted',linewidth=.45,label='seasonal')
  axs[ib].plot(year,SST90thEz[f'SST90thE{4-ib}'],color='red',linestyle='dashed',linewidth=.45,label='percentile threshold')
#
outfile=f'{dirout}/FigureS5.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

############################
# PLOT chl
############################
fig, axs = plt.subplots(nrows=4,ncols=1)
#
for ib in range(3,-1,-1):
  axs[ib].plot(year,chlz[f'chl{4-ib}'],color='green',linewidth=.75,label='daily')
  axs[ib].plot(year,chlclimEz[f'chlclimE{4-ib}'],color='green',linestyle='dotted',linewidth=.45,label='seasonal')
  axs[ib].plot(year,chl10thEz[f'chl10thE{4-ib}'],color='green',linestyle='dashed',linewidth=.45,label='percentile threshold')
#  
outfile=f'{dirout}/FigureS6.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

############################
# PLOT HLD
############################
fig, axs = plt.subplots(nrows=4,ncols=1)
#
for ib in range(3,-1,-1):
  axs[ib].plot(year,-o2z[f'o2{4-ib}'],color='blue',linewidth=.75,label='daily')
  axs[ib].plot(year,-o2climEz[f'o2climE{4-ib}'],color='blue',linestyle='dotted',linewidth=.45,label='seasonal')
  axs[ib].plot(year,-o210thEz[f'o210thE{4-ib}'],color='blue',linestyle='dashed',linewidth=.45,label='percentile threshold')
#
outfile=f'{dirout}/FigureS7.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

############################
# PLOT Bottom Temp
############################

fig, axs = plt.subplots(nrows=4,ncols=1)
#
for ib in range(3,-1,-1):
  axs[ib].plot(year,Tz[f'T{4-ib}'],color='k',linewidth=.75,label='daily')
  axs[ib].plot(year,TclimEz[f'TclimE{4-ib}'],color='k',linestyle='dotted',linewidth=.45,label='seasonal')
  axs[ib].plot(year,T90thEz[f'T90thE{4-ib}'],color='k',linestyle='dashed',linewidth=.45,label='percentile threshold')
#
outfile=f'{dirout}/FigureS8.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
