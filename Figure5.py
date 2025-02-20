import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
import cartopy
import cartopy.crs as ccrs
import cmocean

dirout=''
dirdata=''
#
## ###############################
##  OPEN DATASETS
## ###############################
#
#####
## MHW
ncname=f'{dirdata}/Diags_2d_sMHW.nc'
MHW=xr.open_dataset(ncname)
T1st=MHW['nbEvents']
T2nd=MHW['IntensitySTDR']
T3rd=MHW['Duration']

## LCX
ncname=f'{dirdata}/Diags_2d_LCX.nc'
MHW=xr.open_dataset(ncname)
C1st=MHW['nbEvents']
C2nd=MHW['IntensitySTDR']
C3rd=MHW['Duration']

## SHX
ncname=f'{dirdata}/Diags_2d_SHX.nc'
MHW=xr.open_dataset(ncname)
H1st=MHW['nbEvents']
H2nd=MHW['IntensitySTDR']
H3rd=MHW['Duration']

#
#*****************
#*** PLOTS
#*****************
fig, axs = plt.subplots(nrows=3,ncols=3,subplot_kw={'projection': ccrs.PlateCarree()})
axs=axs.flatten()
###
T1st.plot(ax=axs[0],cmap='turbo',vmin=400,vmax=850,add_colorbar=False)
C1st.plot(ax=axs[1],cmap='turbo',vmin=400,vmax=850,add_colorbar=False)
H1st.plot(ax=axs[2],cmap='turbo',vmin=400,vmax=850,add_colorbar=False)
###
T2nd.plot(ax=axs[3],cmap='plasma',add_colorbar=False)
C2nd.plot(ax=axs[4],cmap='plasma',add_colorbar=False)
H2nd.plot(ax=axs[5],cmap='plasma',add_colorbar=False)
###
T3rd.plot(ax=axs[6],cmap='viridis',vmin=10,vmax=300,add_colorbar=False)
C3rd.plot(ax=axs[7],cmap='viridis',vmin=10,vmax=300,add_colorbar=False)
H3rd.plot(ax=axs[8],cmap='viridis',vmin=10,vmax=300,add_colorbar=False)
outfile=f'{dirout}/Figure5.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
