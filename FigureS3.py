import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#
dirdata=''
dirout=''

### READ DATA
DS=xr.open_dataset(f'{dirdata}/FigureS2.nc')
sstG75300=DS['sstG75300']
sstG075=DS['sstG075']
hldG75300=DS['hldG75300']
hldG075=DS['hldG075']
chlG75300=DS['chlG75300']
chlG075=DS['chlG075']
sst75300=DS['sst75300']
sst075=DS['sst075']
hld75300=DS['hld75300']
hld075=DS['hld075']
chl75300=DS['chl75300']
chl075=DS['chl075']



#####################################

fig, axs = plt.subplots(nrows=3,ncols=2)
axs=axs.flatten()
###
axs[0].scatter(sst75300,sstG75300, c='w' ,s=60,linewidth=2.0,edgecolors='black')
axs[1].scatter(sst075,sstG075, c='w' ,s=60,edgecolors='black',linewidth=2.0)
axs[2].scatter(chl75300,chlG75300, c='w' ,s=60,linewidth=2.0,edgecolors='black')
axs[3].scatter(chl075,chlG075, c='w' ,s=60,linewidth=2.0,edgecolors='black')
axs[4].scatter(hld75300,hldG75300, c='w' ,s=60,linewidth=2.0,ec='black')
axs[5].scatter(hld075,hldG075, c='w' ,s=60,linewidth=2.0,edgecolors='black')
outfile=f'{dirout}/FigureS3.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
