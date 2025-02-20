import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dirout=''
dirdata=''

## ###############################
##  OPEN DATASETS
## ###############################
DS=xr.open_dataset(f'{dirdata}/Diags_VerticalProfile_2005-05-04_235.0_43.25.nc')
Tm=DS['Tm']
Cm=DS['chlm']
Om=DS['o2m']
T=DS['T']
chl=DS['chl']
o2=DS['o2']
lon=DS['longitude']
lat=DS['latitude']

#############
## begin plot
#############
Tdate='2005-05-04'
Tlon='235'
Tlat='43.25'
yminT=5.5;ymaxT=16
yminO=0;ymaxO=300
yminC=0;ymaxC=3.1

# ---------
fig, axs = plt.subplots(nrows=1,ncols=1)
twin1 = axs.twiny()
twin2 = axs.twiny()
#
Tm.plot(ax=axs,y='depth',yincrease=False,color='xkcd:burnt orange',lw=1.5,label=f'Temp')
Om.plot(ax=twin1,y='depth',yincrease=False,color='blue',lw=1.5,label=f'o2')
Cm.plot(ax=twin2,y='depth',yincrease=False,color='green',lw=1.5,label=f'chl')
#
T.plot(ax=axs,y='depth',yincrease=False,color='xkcd:burnt orange',lw=1.5,ls='--',label=f'Temp')
o2.plot(ax=twin1,y='depth',yincrease=False,color='blue',lw=1.5,ls='--',label=f'o2')
chl.plot(ax=twin2,y='depth',yincrease=False,color='green',lw=1.5,ls='--',label=f'chl')
#
axs.set_ylim(370.,0)
axs.set_xlim(yminT,ymaxT)
twin1.set_xlim(yminO,ymaxO)
twin2.set_xlim(yminC,ymaxC)
axs.set_ylabel(f'depth (m)')
outfile=f'{dirout}/Figure2.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
