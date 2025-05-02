# Created by Gaelle Hervieux
#
# Generate S5 figure.

# S5 Figure The likelihood multiplication factor (LMF; color) for each compound extreme 
# (columns) from a surface (first row) and bottom (second row) ocean perspective: (columns) 
# from left to right, MHW-LCX, LCX-SHX, MHW-SHX, and MHW-LCX-SHX, respectively. By 
# definition, an LMF = 1 indicates the two or more extremes are statistically independent. For a 
# given compound extreme, the absence of color (white) indicates no event has been identified 
# over the study period (LMF = 0). (second row) Only locations found within the CCLME (black 
# contour) where the ocean bottom is 1000 m or shallower are shown.  

import xarray as xr
import numpy as np
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

# 1 - Read Data 

ds=xr.open_dataset('../DATA/LMF.nc')
# surface
LMFTHs=ds['LMFTHs']
LMFTCs=ds['LMFTCs']
LMFHCs=ds['LMFHCs']
LMFTHCs=ds['LMFTHCs']
# bottom
LMFTHb=ds['LMFTHb']
LMFTCb=ds['LMFTCb']
LMFHCb=ds['LMFHCb']
LMFTHCb=ds['LMFTHCb']

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

## Build colorbat
cmap = cm.get_cmap('Blues_r', 55)
cmaplist = [cmap(i) for i in range(0,cmap.N-5)]
cmap2 = cm.get_cmap('YlOrRd', 90)
cmaplist2 = [cmap2(i) for i in range(0,cmap2.N)]

my_cmap2 = colors.LinearSegmentedColormap.from_list('Custom cmap',\
                cmaplist+cmaplist2, len(cmaplist)+len(cmaplist2))
clev=[0.05,0.25,0.5,0.75,1,2,3,4,5,6,7,8,9]
clevs01=np.linspace(0.05,0.98,50)
clevs19=np.linspace(1,10,90)
clevs=np.concatenate((clevs01,clevs19))

## 

Tvar=['MHW-LCX','LCX-SHX','MHW-SHX','MHW-LCX-SHX']
Ttitle=['Surface','Bottom']

fig, axs = plt.subplots(nrows=2,ncols=4,subplot_kw={'projection': ccrs.PlateCarree()},
                      figsize=(11,8),num=4,clear=True)
fig.subplots_adjust(bottom=0.05, top=0.95,hspace=-0.1,wspace=0.05,right=0.9,left=0.1)
axs=axs.flatten()
### Surface
cc=LMFTCs.plot(ax=axs[0],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
LMFHCs.plot(ax=axs[1],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
LMFTHs.plot(ax=axs[2],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
LMFTHCs.plot(ax=axs[3],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
p0 = axs[3].get_position().get_points().flatten()
axs[0].contourf(LMFTCs.where(LMFTCs==1),color='m',level=[1.])
axs[1].contourf(LMFHCs.where(LMFHCs==1),color='m',level=[1.])
axs[2].contourf(LMFTHs.where(LMFTHs==1),color='m',level=[1.])
axs[3].contourf(LMFTHCs.where(LMFTHCs==1),color='m',level=[1.])
#ax_cbar = fig.add_axes([0.91, p0[1], 0.01, p0[3]-p0[1]])
#cbar=fig.colorbar(cc,cax=ax_cbar, ticks=clev[::2],shrink=0.8,location='right',orientation='vertical',label=f'#')
#cbar.set_label(label=f'',fontsize=14)
#cbar.ax.minorticks_off()
#cbar.ax.tick_params(labelsize=14)
for iii in range(0,4):
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
  axs[iii].set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs[iii].get_xticks()],size=16)
  if (iii==0):
    axs[iii].set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs[iii].get_yticks()],size=16)
  else:
    axs[iii].set_yticklabels('')
### Bottom
cc=LMFTCb.where(maskLME==1).plot(ax=axs[4],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
LMFHCb.where(maskLME==1).plot(ax=axs[5],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
LMFTHb.where(maskLME==1).plot(ax=axs[6],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
LMFTHCb.where(maskLME==1).plot(ax=axs[7],cmap=my_cmap2,levels=clevs,extend='max',add_colorbar=False)
p0 = axs[7].get_position().get_points().flatten()
axs[4].contourf(LMFTCb.where(LMFTCs==1),color='m',level=[1.])
axs[5].contourf(LMFHCb.where(LMFHCs==1),color='m',level=[1.])
axs[6].contourf(LMFTHb.where(LMFTHs==1),color='m',level=[1.])
axs[7].contourf(LMFTHCb.where(LMFTHCs==1),color='m',level=[1.])
ax_cbar = fig.add_axes([0.91, .4, 0.01, p0[3]-p0[1]])
cbar=fig.colorbar(cc,cax=ax_cbar, ticks=clev[::2],shrink=0.8,location='right',orientation='vertical',label=f'#')
cbar.set_label(label=f'',fontsize=14)
cbar.ax.minorticks_off()
cbar.ax.tick_params(labelsize=14)
for iii in range(4,8):
  axs[iii].plot(x[:29],y[:29],color='k',transform=ccrs.PlateCarree())
  axs[iii].plot(x[210::],y[210::],color='k',transform=ccrs.PlateCarree())
  axs[iii].set_title(f'')
  axs[iii].set_ylabel(f'')
  axs[iii].set_xlabel(f'')
  axs[iii].coastlines()
  axs[iii].set_extent([234,250.5,22,48],ccrs.PlateCarree())
  axs[iii].add_feature(cartopy.feature.LAND, zorder=10, color='grey')
  axs[iii].add_feature(state_borders,zorder=100,linewidth=0.25,edgecolor='k')
  axs[iii].grid(color='gray', alpha=0.5, linestyle='--')
  axs[iii].set_xticks([-122,-115],crs=ccrs.PlateCarree())
  axs[iii].set_yticks([25,35,45],crs=ccrs.PlateCarree())
  axs[iii].tick_params(axis='both',direction='out',width=1.5,length=4)
  axs[iii].set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs[iii].get_xticks()],size=16)
  if (iii==4):
    axs[iii].set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs[iii].get_yticks()],size=16)
  else:
    axs[iii].set_yticklabels('')
for ip in range(0,2):
  axs[4*ip].text(-0.33, 0.5, f' {Ttitle[ip]}', transform=axs[4*ip].transAxes, \
        fontsize=18,weight='bold', va='center' ,ha='right',rotation='vertical')
for ip in range(0,4):
  axs[ip].set_title(f'{Tvar[ip]}',fontsize=18)
plt.suptitle(f'')
outfile=f'PLOTS/LMF_map.png'
