import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

dirout=''
dirdata=''


## ##############################
##  OPEN DATASETS
## ##############################
DS=xr.open_dataset(f'{dirdata}/Figure3.nc')

SST=DS['SST']
SSTclimE=DS['SST'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
SST90thE=DS['sst90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)

chl=DS['chl']
chlclimE=DS['chl'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
chl10thE=DS['chl10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)

o2c=-DS['HLD'].groupby('time.dayofyear').mean('time')
o2climE=-DS['HLD'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
o210thE-DS['HLD10th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)

T=DS['botT']
TclimE=DS['botT'].groupby('time.dayofyear').mean('time').sel(dayofyear=DS['SST'].time.dt.dayofyear)
T90thE=DS['botT90th'].sel(dayofyear=DS['SST'].time.dt.dayofyear)

SSTper=np.where(SST>=SST90thE,1,0)
Tper=np.where(T>=T90thE,1,0)
chlper=np.where(chl<=chl10thE,1,0)
o2per=np.where(o2>=o210thE,1,0)

year=DS.indexes['time'].to_datetimeindex()

# ###############################
# PLOTS
# ###############################

fig, axs = plt.subplots(nrows=4,ncols=1)
#
axs[0].plot(year,SST,color='red',linewidth=.8,label='SST')
axs[0].plot(year,SSTclimE,color='red',linestyle='-.',linewidth=.45,label='Seasonal Cycle')
axs[0].plot(year,SST90thE, color='red',linestyle='--',linewidth=.45,label='90th percentile of SST')
#
axs[1].plot(year,chl,color='green',linewidth=.75,label='chlIntV : chl (0-100m)')
axs[1].plot(year,chlclimE,color='green',linestyle='-.',linewidth=.45,label='Seasonal Cycle')
axs[1].plot(year,chl10thE, color='green',linestyle='--',linewidth=.45,label='10th percentile of chlIntV')
#
axs[2].plot(year,-o2,color='blue',linewidth=.75,label='Hypoxic Layer')
axs[2].plot(year,-o2climE,color='blue',linestyle='-.',linewidth=.45,label='Seasonal Cycle')
axs[2].plot(year,-o210thE, color='blue',linestyle='--',linewidth=.45,label='10th percentile of HL')
#
axs[3].plot(year,T,color='black',linewidth=.75,label='Bottom Temp')
axs[3].plot(year,TclimE,color='black',linestyle='-.',linewidth=.45,label='Seasonal Cycle')
axs[3].plot(year,T90thE,color='black',linestyle='-.',linewidth=.45,label='90th percentile of botT')
#
outfile=f'{dirout}/Figure3.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
