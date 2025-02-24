import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

dirout=''
dirdata=''


## ###############################
##  OPEN DATASETS
## ###############################
DS=xr.open_dataset(f'{dirdata}/FigureS4.nc')
SSTz=DS['SST']
SSTc=DS['SST'].groupby('time.dayofyear').mean('time')
SSTclimEz=DS['SST'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
SST90thEz=DS['sst90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
chlz=DS['chl']
chlc=DS['chl'].groupby('time.dayofyear').mean('time')
chlclimEz=DS['chl'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
chl10thEz=DS['chl10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
o2z=-DS['HLD']
o2c=-DS['HLD'].groupby('time.dayofyear').mean('time')
o2climEz=-DS['HLD'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
o210thEz=-DS['HLD10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)
year=DS.indexes['time'].to_datetimeindex()
yeare=year[0]
yearb=year[-1]

## ###############################
## PLOT
## ###############################
Tlabel1=['SST','chlIntV : chl (0-100m)','Hypoxic Layer']
Tlabel2=['90th percentile','10th percentile','10th percentile']
Tcolors1=['red','green','blue']
T=[SSTz,chlz,o2z]
T90=[SST90thEz,chl10thEz,o210thEz]
Tclim=[SSTclimEz,chlclimEz,o2climEz]

fig, axs = plt.subplots(nrows=3,ncols=1)
axs=axs.flatten()
#
for ix in range(0,3):
  axs[ix*2].plot(year,T[ix],color=Tcolors1[ix],linewidth=.8,label=Tlabel1[ix])
  axs[ix*2].plot(year,T90[ix],color=Tcolors1[ix],linestyle='--',linewidth=.45,label=Tlabel2[ix])
  axs[ix*2].plot(year,Tclim[ix],Tcolors1[ix],linestyle='-.',linewidth=.45,label='Seasonal Cycle')
#

outfile=f'{dirout}/FigureS4}.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
