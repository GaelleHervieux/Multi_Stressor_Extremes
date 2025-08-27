# Created by Gaelle Hervieux
#
# Generate S4 figure.

# S4 Figure Maps of the number of compound extreme days (color; minimum of five days, by 
# definition) identified over the study period (1996–2019) from a surface (first row) and bottom 
# (second row) ocean perspective: (columns) from left to right, MHW-LCX, LCX-SHX, 
# MHW-SHX, and MHW-LCX-SHX, respectively. Light gray contours outline the CCLME, 
# offshore, and nearshore boundaries (see Fig 1 for reference). (second row) Only locations found 
# within the CCLME (black contour) where the ocean bottom is 1000 m or shallower are shown. 

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
nbTC=ds['nbTC']
nbHC=ds['nbHC']
nbTH=ds['nbTH']
Tnb=[nbTC,nbHC,nbTH]

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

state_borders = cartopy.feature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')

## Surface

Tlabel=['SMHW-LCX','LCX-SHX','SMHW-SHX']

fig, axs = plt.subplots(nrows=1,ncols=3,subplot_kw={'projection':ccrs.PlateCarree()},figsize=(12,6),num=4,clear=True)
axs=axs.flatten()
#
for ix in range(0,3):
  cc=Tnb[ix].where(Tnb[ix]>0).isel(depth=0).plot(ax=axs[ix],cmap='turbo',vmin=5,vmax=600,extend='max',add_colorbar=False)
  axs[ix].plot(x[:29],y[:29],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
  axs[ix].plot(x[210::],y[210::],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
  axs[ix].plot(x75[:5],y75[:5],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].plot(x75[180::],y75[180::],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].plot(x300[8:20],y300[8:20],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].plot(x300[197:],y300[197:],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].set_xlabel('')
  axs[ix].set_ylabel('')
  axs[ix].coastlines()
  axs[ix].set_extent([227,252,20,48],ccrs.PlateCarree())
  axs[ix].add_feature(cartopy.feature.LAND, zorder=10, color='grey')
  axs[ix].add_feature(state_borders, zorder=100,linewidth=0.25,edgecolor='k')
  gr=axs[ix].gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--',draw_labels=False)
  axs[ix].set_xticks(axs[ix].get_xticks()[1:-1:2],crs=ccrs.PlateCarree())
  axs[ix].set_yticks(axs[ix].get_yticks()[1:-1],crs=ccrs.PlateCarree())
  axs[ix].set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs[ix].get_xticks()],size=18)
  if ix==0:
    axs[ix].set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs[ix].get_yticks()],size=18)
  else:
    axs[ix].set_yticklabels([f'' for ix in axs[ix].get_yticks()],size=18)
  axs[ix].tick_params(axis='both',direction='out',width=1.5,length=4)
  axs[ix].set_title(f'{Tlabel[ix]}',fontsize=18)
cbar_ax = fig.add_axes([0.2, 0.12, 0.6, 0.02])
cbar=fig.colorbar(cc,cax=cbar_ax,orientation='horizontal',ticks=[5,100,200,300,400,500,600],extend='max')
cbar.set_label(label=f'# Days of Events',fontsize=16)
cbar.ax.tick_params(labelsize=16)
plt.suptitle(f'surface',fontsize=16)
outfile=f'NbDays_Events_surface.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

## Bottom

Tlabel=['BMHW-LCX','LCX-SHX','BMHW-SHX']

fig, axs = plt.subplots(nrows=1,ncols=3,subplot_kw={'projection':ccrs.PlateCarree()},figsize=(12,6),num=4,clear=True)
axs=axs.flatten()
fig.subplots_adjust(bottom=0.2, top=0.9)
for ix in range(0,3):
  cc=Tnb[ix].isel(depth=1).where(maskLME==1).plot(ax=axs[ix],cmap='turbo',vmin=5,vmax=600,extend='max',add_colorbar=False)
  axs[ix].plot(x[:29],y[:29],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
  axs[ix].plot(x[210::],y[210::],color='silver',transform=ccrs.PlateCarree(),lw=2.5)
  axs[ix].plot(x75[:5],y75[:5],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].plot(x75[180::],y75[180::],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].plot(x300[8:20],y300[8:20],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].plot(x300[197:],y300[197:],color='silver',transform=ccrs.PlateCarree(),lw=1.5)
  axs[ix].set_xlabel('')
  axs[ix].set_ylabel('')
  axs[ix].coastlines()
  axs[ix].set_extent([234,250.5,22,48],ccrs.PlateCarree())
  axs[ix].add_feature(cartopy.feature.LAND, zorder=10, color='grey')
  axs[ix].add_feature(state_borders,zorder=100,linewidth=0.25,edgecolor='k')
  axs[ix].grid(color='gray', alpha=0.5, linestyle='--')
  axs[ix].set_xticks([-122,-115],crs=ccrs.PlateCarree())
  axs[ix].set_yticks([25,35,45],crs=ccrs.PlateCarree())
  axs[ix].set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs[ix].get_xticks()],size=18)
  if ix==0:
    axs[ix].set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs[ix].get_yticks()],size=18)
  else:
    axs[ix].set_yticklabels([f'' for ix in axs[ix].get_yticks()],size=18)
  axs[ix].tick_params(axis='both',direction='out',width=1.5,length=4)
  axs[ix].set_title(f'{Tlabel[ix]}',fontsize=18)
cbar_ax = fig.add_axes([0.2, 0.12, 0.6, 0.02])
cbar=fig.colorbar(cc,cax=cbar_ax,orientation='horizontal',ticks=[5,100,200,300,400,500,600],extend='max')
cbar.set_label(label=f'# Days of Events',fontsize=16)
plt.suptitle(f'bottom',fontsize=16)
outfile=f'NbDays_Events_bottom.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')