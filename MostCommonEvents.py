# Created by Gaelle Hervieux
#
# Generate The most common compound extremes over the study period (1996–2019) figure.

# Figure 7: The most common compound extremes over the study period (1996–2019). 
# Maps of the most common compound extreme, defined as the highest number of extreme event 
# days, from a surface (left) and bottom (right) ocean perspective (see respective keys): 
# MHW-LCX (brown), LCX-SHX (purple), MHW-SHX (teal). Light gray contours outline the CCLME, 
# offshore, and nearshore boundaries (see Figure 1 for reference). The maps on the right are 
# regions isolated from the black open squares indicated on the left, delineated by zone 1-4 
# latitudes; here, only locations found within the CCLME where the ocean bottom is 1000 m or 
# shallower are shown. 

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
import cartopy
import cartopy.crs as ccrs
from matplotlib.colors import ListedColormap
import pandas as pd
import cmaps

# 1 - Read Data 

ds=xr.open_dataset('../DATA/Most_Common_Events.nc')
MLa=ds['MLa']

dsM=xr.open_dataset('../DATA/mask_GLORYSBGC.nc')
maskLME=dsM['mask_CCLME']
mask75=xr.where((dsM['mask75']==1) & (maskLME==1),1,0)
mask300=xr.where((dsM['mask300']==1) & (maskLME==1),1,0)

# 2 - Plot

## Get LME contour
fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},
                        figsize=(6,6),num=1,clear=True)
CM=maskLME.plot.contour(ax=axs,kwargs=dict(inline=True),colors='magenta', add_colorbar = False,linewidths=.5)
p = CM.collections[0].get_paths()[0]
v = p.vertices
x = v[:,0]
y = v[:,1]
C75=mask75.plot.contour(ax=axs,colors='black', add_colorbar = False,linewidths=.5)
p75 = C75.collections[0].get_paths()[0]
v75 = p75.vertices
x75 = v75[:,0]
y75 = v75[:,1]
C300=mask300.plot.contour(ax=axs,colors='red', add_colorbar = False,linewidths=.5)
p300 = C300.collections[0].get_paths()[0]
v300 = p300.vertices
x300 = v300[:,0]
y300 = v300[:,1]

levels=np.array([10,20,30,40])
pal_norm = colors.BoundaryNorm(np.array([10,20,30,40]),ncolors=4, clip = False)
cmap= ListedColormap(['indigo','sienna', 'teal'])

## Surface

fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},\
                        figsize=(7.5,7.),num=3,clear=True)
fig.subplots_adjust(bottom=0.15,top=0.95)
cc=MLa.isel(depth=0).plot(ax=axs,cmap = cmap, levels=levels,add_colorbar = False,alpha=0.75)
axs.plot(x[:29],y[:29],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
axs.plot(x[210::],y[210::],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
axs.plot(x75[:5],y75[:5],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
axs.plot(x75[180::],y75[180::],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
axs.plot(x300[8:20],y300[8:20],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
axs.plot(x300[197:],y300[197:],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
axs.set_xlabel('')
axs.set_ylabel('')
axs.coastlines()
axs.set_extent([227,252,20,48],ccrs.PlateCarree())
axs.add_feature(cartopy.feature.LAND, zorder=10, color='grey')
state_borders = cartopy.feature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')
axs.add_feature(state_borders,\
          zorder=100,edgecolor='k',linewidth=0.25)
gr=axs.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--',draw_labels=False)
axs.set_xticks(axs.get_xticks()[1:-1:2],crs=ccrs.PlateCarree())
axs.set_yticks(axs.get_yticks()[1:-1],crs=ccrs.PlateCarree())
axs.set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs.get_xticks()],size=18)
axs.set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs.get_yticks()],size=18)
axs.tick_params(axis='both',direction='out',width=1.5,length=4)
cbar1 = plt.colorbar(cc,cax=fig.add_axes([0.25,0.05,0.5,0.02]), orientation='horizontal')
cbar1.set_ticks([15,25,35])
cbar1.set_ticklabels(['LHl & LChl','MHW & LChl','MHW & LHl'],fontsize=16)
axs.set_title(f'surface',fontsize=16)
outfile=f'MostCommonEvents_surface.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

## Bottom

fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},\
                        figsize=(7.5,7),num=3,clear=True)
fig.subplots_adjust(bottom=0.15,top=0.95)
cc=MLa.isel(depth=1).where(maskLME==1).plot(ax=axs,cmap = cmap, levels=levels,add_colorbar = False,alpha=0.75)
axs.plot(x[:29],y[:29],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
axs.plot(x[210::],y[210::],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
axs.plot(x75[:5],y75[:5],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
axs.plot(x75[180::],y75[180::],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
axs.plot(x300[8:20],y300[8:20],color='silver',transform=ccrs.PlateCarree(),lw=1.5,zorder=20)
axs.plot(x300[197:],y300[197:],color='silver',transform=ccrs.PlateCarree(),lw=1.5,zorder=20)
axs.set_xlabel('')
axs.set_ylabel('')
cbar1 = plt.colorbar(cc,cax=fig.add_axes([0.15,0.05,0.7,0.02]), orientation='horizontal')
cbar1.set_ticks([15,25,35])
cbar1.set_ticklabels(['LHl & LChl','MHW & LChl','MHW & LHl'],fontsize=16)
axs.coastlines()
axs.set_extent([234,250,20,48],ccrs.PlateCarree())
axs.add_feature(cartopy.feature.LAND, zorder=10, color='grey')
state_borders = cartopy.feature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')
axs.add_feature(state_borders, zorder=100,linewidth=0.25,edgecolor='k')
gr=axs.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--',draw_labels=False)
axs.set_xticks([-122,-115],crs=ccrs.PlateCarree())
axs.set_yticks([25,35,45],crs=ccrs.PlateCarree())
axs.set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs.get_xticks()],size=18)
axs.set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs.get_yticks()],size=18)
axs.tick_params(axis='both',direction='out',width=1.5,length=4)
#
axs.set_title(f'bottom',fontsize=16)
outfile=f'MostCommonEvents_bottom.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
