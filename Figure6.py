import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs

dirplots=''
dirdata=''
#
## ###############################
##  OPEN DATASETS
## ###############################
#
#####
## sMHW - LCX
ncname=f'{dirdata}/Diags_2d_sMHW_LCX.nc'
MHW=xr.open_dataset(ncname)
TC1st=MHW['nbEvents']
TC2nd=MHW['IntensitySTDR']
TC3rd=MHW['Duration']

## LCX - SHX
ncname=f'{dirdata}/Diags_2d_LCX_SHX.nc'
MHW=xr.open_dataset(ncname)
CH1st=MHW['nbEvents']
CH2nd=MHW['IntensitySTDR']
CH3rd=MHW['Duration']

## sMHW - SHX
ncname=f'{dirdata}/Diags_2d_sMHW_SHX.nc'
MHW=xr.open_dataset(ncname)
TH1st=MHW['nbEvents']
TH2nd=MHW['IntensitySTDR']
TH3rd=MHW['Duration']
#
## sMHW - LCX - SHX
ncname=f'{dirdata}/Diags_2d_sMHW_LCX_SHX.nc'
MHW=xr.open_dataset(ncname)
THC1st=MHW['nbEvents']
THC2nd=MHW['IntensitySTDR']
THC3rd=MHW['Duration']

#***
#*** PLOTS PAPER
#***

fig, axs = plt.subplots(nrows=3,ncols=4,subplot_kw={'projection': ccrs.PlateCarree()},
                      figsize=(11.5,10),num=4,clear=True)
axs=axs.flatten()
###
TC1st.plot(ax=axs[0],cmap='turbo',vmin=1,vmax=30)
CH1st.plot(ax=axs[1],cmap='turbo',vmin=1,vmax=30)
TH1st.plot(ax=axs[2],cmap='turbo',vmin=1,vmax=30)
THC1st.plot(ax=axs[3],cmap='turbo',vmin=1,vmax=30)
###
TC2nd.plot(ax=axs[4],cmap='plasma',vmin=0.5,vmax=3.5)
CH2nd.plot(ax=axs[5],cmap='plasma',vmin=0.5,vmax=3.5)
TH2nd.plot(ax=axs[6],cmap='plasma',vmin=0.5,vmax=3.5)
THC2nd.plot(ax=axs[7],cmap='plasma',vmin=0.5,vmax=3.5)
###
TC3rd.plot(ax=axs[8],cmap='viridis',vmin=5,vmax=130)
CH3rd.plot(ax=axs[9],cmap='viridis',vmin=5,vmax=130)
TH3rd.plot(ax=axs[10],cmap='viridis',vmin=5,vmax=130)
THC3rd.plot(ax=axs[11],cmap='viridis',vmin=5,vmax=130)
outfile=f'{dirplots}/Figure6.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
