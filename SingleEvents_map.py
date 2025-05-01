# Created by Gaelle Hervieux
#
# Generate  Maps of single extreme characteristics over the study period (1996–2019) figure.

# Figure 3: Maps of single extreme characteristics over the study period (1996–2019). Frequency 
# (top row), mean intensity (middle row; mean z-score (𝑍), expressed in sigma units), and mean 
# duration (bottom row; days) of SMHWs (left column), LCXs (middle column), and SHXs (right column). 
# The black contour marks the boundary of the CCLME. 

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

ds=xr.open_dataset('../DATA/SingleEvents_map.nc')
Tfreq=ds['Tfreq']
TDuration=ds['TDuration']
Tintensity=ds['Tintensity']
Cfreq=ds['Cfreq']
CDuration=ds['CDuration']
Cintensity=ds['Cintensity']
Hfreq=ds['Hfreq']
HDuration=ds['HDuration']
Hintensity=ds['Hintensity']

dsM=xr.open_dataset('../DATA/mask_GLORYSBGC.nc')
maskLME=dsM['mask_CCLME']

# 2 - Plot

Tvar=['SMHW','LCX','SHX']
Ttitle=['Frequency','Mean Intensity','Mean Duration']

state_borders = cartopy.feature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')

## Get LME contour
fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},
                        figsize=(6,6),num=1,clear=True)
CM=maskLME.plot.contour(ax=axs,kwargs=dict(inline=True),colors='magenta', add_colorbar = False,linewidths=.5)
p = CM.collections[0].get_paths()[0]
v = p.vertices
x = v[:,0]
y = v[:,1]


fig, axs = plt.subplots(nrows=3,ncols=3,subplot_kw={'projection': ccrs.PlateCarree()},
                      figsize=(11.5,10),num=4,clear=True)
fig.subplots_adjust(bottom=0.1,top=0.9,hspace=0.1,wspace=0.05,right=0.9,left=0.06)
axs=axs.flatten()
###
cc=Tfreq.plot(ax=axs[0],cmap='turbo',vmin=0.2,vmax=3.4,add_colorbar=False)
Cfreq.plot(ax=axs[1],cmap='turbo',vmin=0.2,vmax=3.4,add_colorbar=False)
Hfreq.plot(ax=axs[2],cmap='turbo',vmin=0.2,vmax=3.4,add_colorbar=False)
p0 = axs[2].get_position().get_points().flatten()
ax_cbar = fig.add_axes([p0[2]-0.015, p0[1], 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar, shrink=0.65, location='right',orientation='vertical',label=f'#')
cbar.set_label(label=f'Annual Events',fontsize=14)
cbar.ax.tick_params(labelsize=14)
###
cc=Tintensity.plot(ax=axs[3],cmap='plasma',vmin=0.5,vmax=3.5,add_colorbar=False)
Cintensity.plot(ax=axs[4],cmap='plasma',vmin=0.5,vmax=3.5,add_colorbar=False)
Hintensity.plot(ax=axs[5],cmap='plasma',vmin=0.5,vmax=3.5,add_colorbar=False)
p0 = axs[5].get_position().get_points().flatten()
ax_cbar = fig.add_axes([p0[2]-0.015, p0[1], 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar, shrink=0.65,
        location='right',ticks=[1,2,3],
        extend='max',orientation='vertical',label=f'#')
cbar.set_label(label=f'$\sigma$',fontsize=14)
cbar.ax.tick_params(labelsize=14)
###
cc=TDuration.plot(ax=axs[6],cmap='viridis',vmin=10,vmax=300,add_colorbar=False)
CDuration.plot(ax=axs[7],cmap='viridis',vmin=10,vmax=300,add_colorbar=False)
HDuration.plot(ax=axs[8],cmap='viridis',vmin=10,vmax=300,add_colorbar=False)
p0 = axs[8].get_position().get_points().flatten()
ax_cbar = fig.add_axes([p0[2]-0.015, p0[1], 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar, shrink=0.55,extend='both', location='right',orientation='vertical')
cbar.set_label(label=f'days',fontsize=14)
cbar.ax.tick_params(labelsize=14)
###
for iii in range(0,9):
  axs[iii].plot(x[:29],y[:29],color='silver',transform=ccrs.PlateCarree())
  axs[iii].plot(x[210::],y[210::],color='silver',transform=ccrs.PlateCarree())
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
  if iii>=6:
    axs[iii].set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs[iii].get_xticks()],size=16)
  else:
    axs[iii].set_xticklabels('')
  if (iii==6)|(iii==3)|(iii==0):
    axs[iii].set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs[iii].get_yticks()],size=16)
  else:
    axs[iii].set_yticklabels('')
for ip in range(0,3):
  axs[3*ip].text(-0.33, 0.5, f' {Ttitle[ip]}', transform=axs[3*ip].transAxes, \
        fontsize=18,weight='bold', va='center' ,ha='right',rotation='vertical')
  axs[ip].set_title(f'{Tvar[ip]}',fontsize=20)
plt.suptitle(f'')
outfile=f'SingleEvents_map.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

