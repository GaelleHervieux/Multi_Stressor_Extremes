import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
import matplotlib.colors as colors
from matplotlib import cm
import cartopy
import cartopy.crs as ccrs

dirout=''
dirdata=''

#### Read Mask
DSmask=xr.open_dataset('/data/ghervieux/GLORYS_BGC/mask_GLORYSBGC_Newzones.nc')
maskA=DSmask['mask_zoneA']
maskB=DSmask['mask_zoneB']
maskC=DSmask['mask_zoneC']
maskD=DSmask['mask_zoneD']
maskE=DSmask['mask_zoneE']
maskF=DSmask['mask_zoneF']
maskG=DSmask['mask_zoneG']
maskH=DSmask['mask_zoneH']
Tmask=[maskA,maskB,maskC,maskD,maskE,maskF,maskG,maskH]
Tzone=['ZoneA','ZoneB','ZoneC','ZoneD','ZoneE','ZoneF','ZoneG','ZoneH']
mask=xr.zeros_like(maskA)
for izone in range(0,len(Tmask)):
  mask=xr.where(Tmask[izone]==1,izone+1,mask)
mask=mask.where(mask>0)

colors=['xkcd:sandy','xkcd:saffron','xkcd:pumpkin','xkcd:burnt umber',\
        'xkcd:robin egg blue','xkcd:sea','xkcd:azure','xkcd:sapphire']
fig, axs = plt.subplots(nrows=1,ncols=1,subplot_kw={'projection': ccrs.PlateCarree()})
mask.plot(ax=axs,colors=colors,levels=np.arange(1,len(Tmask)+2),add_colorbar = False)
outfile=f'{dirout}/Figure1.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
