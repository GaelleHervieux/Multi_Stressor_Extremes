# Created by Gaelle Hervieux
#
# Generate Maps of compound extreme characteristics over the study
# period (1996-2019) figure

# Figure 5: Maps of compound extreme characteristics over the study 
# period (1996-2019). Frequency (top row), mean intensity (middle row; 
# standardized and expressed in sigma units (𝛹′)), and mean duration 
# (bottom row) of compound SMHW-LCX (surface MHW; first column), 
# LCX-SHX (second column), SMHW-SHX (third column), and SMHW-LCX-SHX 
# (fourth column). The black contour marks the boundary of the CCLME.

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
import cartopy
import cartopy.crs as ccrs
import cmocean
import cmaps

# 1 - Read Data

ds=xr.open_dataset('../DATA/MultiEvents_map.nc')
TCfreq=ds['TCfreq']
TCDuration=ds['TCDuration']
TCintensity=ds['TCintensity']
CHfreq=ds['CHfreq']
CHDuration=ds['CHDuration']
CHintensity=ds['CHintensity']
THfreq=ds['THfreq']
THDuration=ds['THDuration']
THintensity=ds['THintensity']
TCHfreq=ds['TCHfreq']
TCHDuration=ds['TCHDuration']
TCHintensity=ds['TCHintensity']

dsM=xr.open_dataset('../DATA/mask_GLORYSBGC.nc')
maskLME=dsM['mask_CCLME']

# 2 - Plot


## Get LME contour
fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},
                        figsize=(6,6),num=1,clear=True)
CM=maskLME.plot.contour(ax=axs,kwargs=dict(inline=True),colors='magenta', add_colorbar = False,linewidths=.5)
p = CM.collections[0].get_paths()[0]
v = p.vertices
x = v[:,0]
y = v[:,1]


state_borders = cartopy.feature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')


Tvar=['SMHW-LCX','LCX-SHX','SMHW-SHX','SMHW-LCX-SHX']
Ttitle=['Frequency','Mean Intensity','Mean Duration']

fig, axs = plt.subplots(nrows=3,ncols=4,subplot_kw={'projection': ccrs.PlateCarree()},
                      figsize=(10,10),num=3,clear=True)
fig.subplots_adjust(bottom=0.1,\
        top=0.9,hspace=-0.4,wspace=0.05,right=0.9,left=0.12)
axs=axs.flatten()
###
cc=TCfreq.plot(ax=axs[0],cmap='turbo',vmin=0.,vmax=1.25,add_colorbar=False)
CHfreq.plot(ax=axs[1],cmap='turbo',vmin=0.,vmax=1.25,add_colorbar=False)
THfreq.plot(ax=axs[2],cmap='turbo',vmin=0.,vmax=1.25,add_colorbar=False)
TCHfreq.plot(ax=axs[3],cmap='turbo',vmin=0.,vmax=1.25,add_colorbar=False)
p0 = axs[3].get_position().get_points().flatten()
ax_cbar = fig.add_axes([0.91, p0[1], 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar,\
        shrink=0.65,location='right',extend='max',\
        orientation='vertical',ticks=[0.25,0.5,0.75,1.])
cbar.set_label(label=f'Annual Events',fontsize=14)
cbar.ax.tick_params(labelsize=14)
###
cc=TCintensity.plot(ax=axs[4],cmap='plasma',vmin=0.5,vmax=4.5,add_colorbar=False)
CHintensity.plot(ax=axs[5],cmap='plasma',vmin=0.5,vmax=4.5,add_colorbar=False)
THintensity.plot(ax=axs[6],cmap='plasma',vmin=0.5,vmax=4.5,add_colorbar=False)
TCHintensity.plot(ax=axs[7],cmap='plasma',vmin=0.5,vmax=4.5,add_colorbar=False)
p0 = axs[7].get_position().get_points().flatten()
ax_cbar = fig.add_axes([0.91, p0[1], 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar, shrink=0.65, location='right',\
        extend='max',orientation='vertical',label=f'$\sigma$')
cbar.set_label(label=f'$\sigma$',fontsize=14)
cbar.ax.tick_params(labelsize=14)
###
cc=TCDuration.plot(ax=axs[8],cmap='viridis',vmin=5,vmax=130,add_colorbar=False)
CHDuration.plot(ax=axs[9],cmap='viridis',vmin=5,vmax=130,add_colorbar=False)
THDuration.plot(ax=axs[10],cmap='viridis',vmin=5,vmax=130,add_colorbar=False)
TCHDuration.plot(ax=axs[11],cmap='viridis',vmin=5,vmax=130,add_colorbar=False)
p0 = axs[11].get_position().get_points().flatten()
ax_cbar = fig.add_axes([0.91, p0[1], 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar, shrink=0.65, location='right',\
        extend='max',orientation='vertical',label=f'days')
cbar.set_label(label=f'days',fontsize=14)
cbar.ax.tick_params(labelsize=14)
###
for iii in range(0,12):
  axs[iii].plot(x[:29],y[:29],color='k',transform=ccrs.PlateCarree())
  axs[iii].plot(x[210::],y[210::],color='k',transform=ccrs.PlateCarree())
  axs[iii].set_title(f'')
  axs[iii].set_ylabel(f'')
  axs[iii].set_xlabel(f'')
  axs[iii].coastlines()
  axs[iii].set_extent([227,252,21,48],ccrs.PlateCarree())
  axs[iii].add_feature(cartopy.feature.LAND, zorder=10, color='grey')
  axs[iii].add_feature(state_borders,zorder=100,linewidth=0.25,edgecolor='k')
  axs[iii].grid(color='gray', alpha=0.5, linestyle='--')
  axs[iii].set_xticks([-130,-115],crs=ccrs.PlateCarree())
  axs[iii].set_yticks([25,35,45],crs=ccrs.PlateCarree())
  axs[iii].tick_params(axis='both',direction='out',width=1.5,length=4)
  if iii>=8:
    axs[iii].set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs[iii].get_xticks()],size=16)
  else:
    axs[iii].set_xticklabels('')
  if (iii==8)|(iii==4)|(iii==0):
    axs[iii].set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs[iii].get_yticks()],size=16)
  else:
    axs[iii].set_yticklabels('')
for ip in range(0,3):
  axs[4*ip].text(-0.4, 0.5, f' {Ttitle[ip]}', transform=axs[4*ip].transAxes, \
        fontsize=18,weight='bold', va='center' ,ha='right',rotation='vertical')
for ip in range(0,4):
  axs[ip].set_title(f'{Tvar[ip]}',fontsize=18)
plt.suptitle(f'')
outfile=f'MultiEvents_map.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
