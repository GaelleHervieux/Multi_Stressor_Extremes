import xarray as xr
import numpy as np
import numpy.ma as ma

dirout=''
dirdata=''


## ###############################
## 2d map
## ###############################
############  OPEN DATASETS
filename=f'{dirdata}/FigureS1a.nc'
ds=xr.open_dataset(filename)
############
fig, axs = plt.subplots(nrows=1,ncols=1,
                        subplot_kw={'projection': ccrs.PlateCarree()})
#
data=ds['POD']*100.
cs=axs.contourf(ds['longitude'],ds['latitude'],data,np.arange(20,100,10),
                           transform = ccrs.PlateCarree(),
                           cmap='turbo',extend='both')
axs.coastlines()
outfile=f'{dirout}/FIgureS1a.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

## ###############################
##  OPEN DATASETS
## ###############################
filename=f'{dirdata}/FigureS1b.nc'
ds=xr.open_dataset(filename)
T=ds['SST_OISSTv2']
TG=ds['SST_G']
TG90thE=ds['SST90th_G']
T90thE=ds['SST90th_OISSTv2']
TperG=np.where(TG>TG90thE,1,0)
TperT=np.where(T>TG90thE,1,0)
Tper=xr.where((TperG==1)&(TperT==1),1,0)
# Define the figure object and primary axes
year = ds.indexes['time'].to_datetimeindex()
pod=ds['POD']
label="POD = %.2f" % pod

############ PLOT
fig, axs = plt.subplots(nrows=2,ncols=1)
fig.subplots_adjust(hspace=.05,wspace=.2,top=0.8)
axs[0].plot(year,TG,color='black',linewidth=1.,label='GLORYS')
axs[0].plot(year,TG90thE, color='black',linestyle='dashed',linewidth=.5,label='90th of Temp')
axs[1].plot(year,T,color='red',linewidth=1.,label='OISSTv2')
axs[1].plot(year,T90thE, color='red',linestyle='dashed',linewidth=.5,label='90th of Temp')
outfile=f'{dirout}/FigureS1b.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
