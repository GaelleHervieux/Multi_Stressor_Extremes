import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import pandas as pd

dirout=''
dirdata=''
### ***********
### READ FILES
### ***********
filedepth=f'{dirdata}/GLOBAL_REANALYSIS_BIO_001_029_mask.wc.nc'
DSdepth=xr.open_dataset(filedepth)
deptho=DSdepth['deptho']
#
#####
ncname=f'{dirdata}/Diags_HLchlIntV_Surface_map.nc'
MHW=xr.open_dataset(ncname)
nbHC=MHW['Events'].sum('time')
nbHCmax=nbHC
nbHC=xr.concat([nbHC,nbHC,nbHC,nbHC,nbHC], pd.Index([0,100,200,350,400], name="depth"))
#
ncname=f'{dirdata}/Diags_votemperHLchlIntV_Surface_map.nc'
MHW=xr.open_dataset(ncname)
nbTHC000=MHW['Events'].sum('time')
ncname=f'{dirdata}/Diags_bottomTHLchlIntV_bottom_map.nc'
MHW=xr.open_dataset(ncname)
nbTHCbot=MHW['Events'].sum('time').where(deptho<=1000)
nbTHCbot=nbTHCbot.assign_coords({'depth':1000})
nbTHC=xr.concat([nbTHC000,nbTHCbot],pd.Index([0,1000], name="depth"))
#
ncname=f'{dirdata}/Diags_votemperHL_Surface_map.nc'
MHW=xr.open_dataset(ncname)
nbTH000=MHW['Events'].sum('time')
ncname=f'{dirdata}/Diags_bottomTHL_bottom_map.nc'
MHW=xr.open_dataset(ncname)
nbTHbot=MHW['Events'].sum('time').where(deptho<=1000)
nbTHbot=nbTHbot.assign_coords({'depth':1000})
nbTH=xr.concat([nbTH000,nbTHbot],pd.Index([0,1000], name="depth"))
#
ncname=f'{dirdata}/Diags_votemperchlIntV_Surface_map.nc'
MHW=xr.open_dataset(ncname)
nbTC000=MHW['Events'].sum('time')
ncname=f'{dirdata}/Diags_bottomTchlIntV_bottom_map.nc'
MHW=xr.open_dataset(ncname)
nbTCbot=MHW['Events'].sum('time').where(deptho<=1000)
nbTCbot=nbTCbot.assign_coords({'depth':1000})
nbTC=xr.concat([nbTC000,nbTC100,nbTC200,nbTC350,nbTCbot],pd.Index([0,1000], name="depth"))
#

MLa=xr.ones_like(nbTHC)
MLa=np.where((nbTC>=nbTH) & (nbTC>=nbHC),25,MLa)
MLa=np.where((nbTH>=nbTC) & (nbTH>=nbHC),35,MLa)
MLa=np.where((nbHC>nbTC) & (nbHC>nbTH) ,15,MLa)
MLa=np.where((nbTHC==nbTH)&(MLa==35),45,MLa)
MLa=np.where((nbTHC==nbTC)&(MLa==25),45,MLa)
MLa=np.where((nbTHC==0)&(nbTH==0)&(nbTC==0)&(nbHC==0),np.NaN,MLa)
MLa=xr.DataArray(MLa, dims=nbTH.dims, coords=nbTH.coords)
MLa=MLa.where(MLa>1)

### ***********
### PLOT
### ***********
levels=np.array([10,20,30,40])
pal_norm = colors.BoundaryNorm(np.array([10,20,30,40]),ncolors=4, clip = False)
cmap= ListedColormap(['indigo','sienna', 'teal'])

### PLOT SURFACE

fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()})
cc=MLa.sel(depth=0).plot(ax=axs,cmap = cmap, levels=levels,add_colorbar = False,alpha=0.75)
axs.coastlines()
axs.set_extent([227,252,20,48],ccrs.PlateCarree())
outfile=f'PLOTS/Figure8a.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

### PLOT BOTTOM

fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()})
cc=MLa.sel(depth=1000).plot(ax=axs,cmap = cmap, levels=levels,add_colorbar = False,alpha=0.75)
axs.coastlines()
axs.set_extent([227,252,20,48],ccrs.PlateCarree())
outfile=f'PLOTS/Figure8b.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
