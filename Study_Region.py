# Created by Gaelle Hervieux
#
# Generate The Study Region figure

# Figure 1: The study region. Geographic region making up the California Current \
# Large Marine Ecosystem (dark green contour). \
# The nearshore coastal band (within 0–75 km of the coast) is divided into zones 1–4 (shades of brown) \
# and the offshore coastal band (within 75–300 km of land) is divided into zones 5–8 (shades of blue). 

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
import matplotlib.colors as colors
from matplotlib import cm
import cartopy
import cartopy.crs as ccrs

# 1 - Read Data 

ds=xr.open_dataset('../DATA/mask_GLORYSBGC.nc')
mask1=ds['mask_zone1']
mask2=ds['mask_zone2']
mask3=ds['mask_zone3']
mask4=ds['mask_zone4']
mask5=ds['mask_zone5']
mask6=ds['mask_zone6']
mask7=ds['mask_zone7']
mask8=ds['mask_zone8']
maskLME=ds['mask_CCLME']

Tmask=[mask1,mask2,mask3,mask4,mask5,mask6,mask7,mask8]
Tzone=['Zone1','Zone2','Zone3','Zone4','Zone5','Zone6','Zone7','Zone8']
mask=xr.zeros_like(mask1)
for izone in range(0,len(Tmask)):
  mask=xr.where(Tmask[izone]==1,izone+1,mask)
mask=mask.where(mask>0)


## Get LME contour
fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},
                        figsize=(6,6),num=1,clear=True)
CM=maskLME.plot.contour(ax=axs,kwargs=dict(inline=True),colors='magenta', add_colorbar = False,linewidths=.5)
p = CM.collections[0].get_paths()[0]
v = p.vertices
x = v[:,0]
y = v[:,1]

# 2 - Plot

state_borders =\
cartopy.feature.NaturalEarthFeature(category='cultural',\
        name='admin_1_states_provinces_lakes', scale='50m', facecolor='grey')

colors=['xkcd:sandy','xkcd:saffron','xkcd:pumpkin','xkcd:burnt umber',\
        'xkcd:robin egg blue','xkcd:sea','xkcd:azure','xkcd:sapphire']
fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()},
                        figsize=(8,8),num=1,clear=True)
fig.subplots_adjust(bottom=0.1, top=0.9, wspace=0.05)
####
mask.plot(ax=axs,colors=colors,levels=np.arange(1,len(Tmask)+2),add_colorbar = False)
axs.set_xlabel('')
axs.set_ylabel('')
axs.coastlines()
axs.set_extent([227,252,20,48],ccrs.PlateCarree())
axs.add_feature(cartopy.feature.LAND, zorder=10, color='grey')
axs.add_feature(state_borders,zorder=100,linewidth=0.25,edgecolor='k')
gr=axs.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--',draw_labels=False)
axs.set_xticks(axs.get_xticks()[1:-1:2],crs=ccrs.PlateCarree())
axs.set_yticks(axs.get_yticks()[1:-1],crs=ccrs.PlateCarree())
axs.set_xticklabels([f'{round(ix+360)}$\degree$E' for ix in axs.get_xticks()],size=18)
axs.set_yticklabels([f'{round(ix)}$\degree$N' for ix in axs.get_yticks()],size=18)
axs.tick_params(axis='both',direction='out',width=1.5,length=4)
axs.plot(x[:29],y[:29],color='xkcd:dark teal',transform=ccrs.PlateCarree(),lw=2.5)
axs.plot(x[210::],y[210::],color='xkcd:dark teal',transform=ccrs.PlateCarree(),lw=2.5)
outfile=f'Study_Region.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
