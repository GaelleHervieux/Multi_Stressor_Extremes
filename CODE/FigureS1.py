# Created by Gaelle Hervieux
#
# Generate figure S1.

# S1 Figure (a-b) Time series of daily CCLME-averaged SST (solid contour) and 90th percentile 
# (dotted) from (b) GLORYS-BGC (black) and (c) OISSTv2 (red) from 1996 to 2019. Surface 
# MHWs (SMHWs) in (a) and (b) are indicated by under-the-curve and vertical gray shading; any 
# simulated SMHWs that were not also observed (‘missed’) are indicated by red vertical shading 
# in (a). The POD of SMHWs identified from CCLME-average SSTs is 82%. (c) Probability (%; 
# color) of SMHW detection (POD) at each GLORYS-BGC grid point within the CCLME over 
# the study period.
 

import xarray as xr
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import cartopy
import cartopy.crs as ccrs

# 1 - Read Data
# 
# Timeseries
ds=xr.open_dataset('../DATA/Timeseries_POD_SST.nc')
T=ds['SST_OISSTv2']
TG=ds['SST_G']
TG90thE=ds['SST90th_G']
T90thE=ds['SST90th_OISSTv2']
sMHWT=ds['sMHW']
sMHWG=ds['sMHWG']
sMHW=xr.where((sMHWG==1)&(sMHWT==1),1,0)
# Define the figure object and primary axes
year = ds.indexes['time'].to_datetimeindex()
pod=ds['POD']
label="POD = %.2f" % pod
year=ds.indexes['time'].to_datetimeindex()

# 2d map

ds=xr.open_dataset('../DATA/2dmap_POD_SST.nc')
POD=ds['POD']

# 2 - Plot

# Timeseries

fig, axs = plt.subplots(nrows=2,ncols=1,figsize=(12,6),num=4,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.2,top=0.8)
axs[0].plot(year,TG,color='black',linewidth=1.,label='GLORYS-BGC')
axs[0].plot(year,TG90thE, color='black',linestyle='dashed',linewidth=.5,label='90th of SST')
axs[0].fill_between(year,TG,TG90thE,np.where(sMHWG==1,True,False),color='darkgrey',alpha=0.5)
axs[0].grid()
axs[0].set_ylabel(r'$\degree$C',fontsize=16)
axs[0].set_xlim(year[0],year[-1])
axs[0].set_xticklabels([])
axs[0].set_ylim(axs[0].get_ylim()[0],axs[0].get_ylim()[1])
axs[0].set_yticklabels([round(ix) for ix in axs[0].get_yticks()],fontsize=16)
axs[0].fill_between(year,axs[0].get_ylim()[0],axs[0].get_ylim()[1],np.where(sMHWG==1,True,False),color='darkgrey',\
        alpha=0.5,label='Detected SMHW')
axs[0].fill_between(year,axs[0].get_ylim()[0],axs[0].get_ylim()[1],np.where(((sMHWT==1)&(sMHWG==0)),True,False),\
        color='red', alpha=0.5,label='Missed SMHW')
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left',ncol=2,
        bbox_to_anchor=(0.115,0.93), prop={'size': 14})
axs[1].plot(year,T,color='red',linewidth=1.,label='OISSTv2')
axs[1].plot(year,T90thE, color='red',linestyle='dashed',linewidth=.5,label='90th of SST')
axs[1].fill_between(year,T,T90thE,np.where(sMHWT==1,True,False),color='darkgrey',alpha=0.5)
axs[1].grid()
axs[1].set_ylabel(r'$\degree$C',fontsize=16)
axs[1].set_xlim(year[0],year[-1])
axs[1].set_ylim(axs[1].get_ylim()[0],axs[1].get_ylim()[1])
axs[1].set_yticklabels([round(ix) for ix in axs[1].get_yticks()],fontsize=16)
axs[1].fill_between(year,axs[1].get_ylim()[0],axs[1].get_ylim()[1],np.where(sMHWT==1,True,False),color='darkgrey',\
        alpha=0.5)
handles, labels = axs[1].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left',ncol=1,
        bbox_to_anchor=(0.55,.93), prop={'size': 14})
axs[1].set_xlim(year[0],year[-1])
axs[1].set_xticklabels([ix.get_text() for ix in axs[1].get_xticklabels()],fontsize=16)
plt.xlabel('Time',fontsize=16)
outfile=f'timeseries_SST_GLORYS-BGC_OISSTv2.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

# 2d map

state_borders = cartopy.feature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')
############
fig, axs = plt.subplots(nrows=1,ncols=1,
                        subplot_kw={'projection': ccrs.PlateCarree()},
                        figsize=(10,10),num=3,clear=True)
#
fig.subplots_adjust(bottom=0.2, top=0.95)
data=POD*100.
cs=axs.contourf(ds['longitude'],ds['latitude'],data,np.arange(20,100,10),
                           transform = ccrs.PlateCarree(),
                           cmap='turbo',extend='both')
axs.coastlines()
axs.set_xlabel('')
axs.set_ylabel('')
axs.coastlines()
axs.set_extent([227,252,20,48],ccrs.PlateCarree())
axs.add_feature(cartopy.feature.LAND, zorder=10, color='grey')
axs.add_feature(state_borders,zorder=100,linewidth=0.25,edgecolor='k')
gr=axs.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--',draw_labels=False)
axs.set_xticks(axs.get_xticks()[1:-1:2],crs=ccrs.PlateCarree())
axs.set_yticks(axs.get_yticks()[1:-1],crs=ccrs.PlateCarree())
axs.set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs.get_xticks()],size=24)
axs.set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs.get_yticks()],size=24)
axs.tick_params(axis='both',direction='out',width=1.5,length=4)
cbar_ax = fig.add_axes([0.2, 0.08, 0.6, 0.02])
cbar=fig.colorbar(cs, cax=cbar_ax,orientation='horizontal',label='%')
cbar.ax.tick_params(labelsize=24)
cbar.set_label(label=f'%',fontsize=24)
outfile=f'2dmap_SST_GLORYS-BGC_OISSTv2.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
