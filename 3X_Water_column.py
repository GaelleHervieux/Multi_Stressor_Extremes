# Created by Gaelle Hervieux
#
# Generate Example of a triple extreme in the water column figure

# Figure 2: Example of a triple extreme in the water column. Snapshot of the upper 370 m \
# water column on May 4, 2005 during a triple extreme event identified off the southwest coast of \
# Oregon (43.25oN, 125oW) that began on May 4 and ended on May 8. The solid contours represent the \
# daily (May 4) climatological mean vertical profiles of temperature (orange) and chlorophyll (green) \
# and dissolved oxygen (blue) concentration. The corresponding dashed contours indicate the instantaneous \
# or extreme profile of these properties when a concurrent SMHW (P90 = 13.1oC), LCX (P10 = 31.7 mg m-2), and \
# SHX (P10 = 159.6 m) was identified on May 4, 2005. The climatological (solid green bracket) and \
# instantaneous (dashed green bracket) vertically-integrated (0-100 m; light green shading) chlorophyll \
# concentration values are annotated. Waters below the HLD (blue stars) are hypoxic (light blue shading); \
# the carrot along the x-axis of dissolved oxygen marks the hypoxia threshold of 62.5 mmol m-3.

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1 - Read Data

ds=xr.open_dataset('../DATA/3X_Water_column.nc')
Tm=ds['Tm']
Cm=ds['chlm']
Om=ds['o2m']
T=ds['T']
chl=ds['chl']
o2=ds['o2']
lon=ds['longitude']
lat=ds['latitude']
hld=ds['hld']
hldm=ds['hldm']
hld10th=ds['hld10th']
chlIntV=ds['chlIntV']
chlIntVm=ds['chlIntVm']

# 2 - Plot

Tdate='2005-05-04'
Tlon='235'
Tlat='43.25'
yminT=5.5;ymaxT=16
yminO=0;ymaxO=300
yminC=0;ymaxC=3.1
tkw = dict(labelsize=14,width=1.5)
yyy=xr.zeros_like(Tm)
yy=xr.ones_like(Tm)


fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(6,8),num=2,clear=True)
fig.subplots_adjust(bottom=0.25, top=0.8,left=0.2)
twin1 = axs.twiny()
twin2 = axs.twiny()
twin1.spines.top.set_position(("axes", -.25))
yyy.plot(ax=axs,y='depth',yincrease=False,color='dimgrey',lw=1.5,ls='--')
#
Tm.plot(ax=axs,y='depth',yincrease=False,color='xkcd:burnt orange',lw=1.5,label=f'Temp')
Om.plot(ax=twin1,y='depth',yincrease=False,color='blue',lw=1.5,label=f'o2')
Cm.plot(ax=twin2,y='depth',yincrease=False,color='green',lw=1.5,label=f'chl')
#
axs.fill_between(np.linspace(yminT,ymaxT,37),370*yy,hldm*yy,color='xkcd:cornflower',alpha=0.25)
#
T.plot(ax=axs,y='depth',yincrease=False,color='xkcd:burnt orange',lw=1.5,ls='--',label=f'Temp')
o2.plot(ax=twin1,y='depth',yincrease=False,color='blue',lw=1.5,ls='--',label=f'o2')
chl.plot(ax=twin2,y='depth',yincrease=False,color='green',lw=1.5,ls='--',label=f'chl')
#
axs.fill_between(np.linspace(yminT,ymaxT,37),0*yy,100*yy,color='xkcd:light sage',alpha=0.25)
axs.fill_between(np.linspace(yminT,ymaxT,37),370*yy,hld*yy,color='xkcd:periwinkle blue',alpha=0.25)
#
twin1.scatter(62.5,hldm,s=60,zorder=100,color='xkcd:dark blue',marker='*')
twin1.scatter(62.5,hld,s=60,zorder=101,color='xkcd:dark blue',marker='*')
twin1.text(62.5, -.25, "$\Lambda$", color='xkcd:dark blue',transform=twin1.get_xaxis_transform(),weight='bold',ha='center', va='top')
twin2.text(chlIntV.data, 1.05, "$\Lambda$", color='xkcd:dark green',transform=twin2.get_xaxis_transform(),weight='bold',ha='center', va='top')
twin2.text(chlIntVm.data, 1.05, "$\Lambda$", color='xkcd:green',transform=twin2.get_xaxis_transform(),weight='bold',ha='center', va='top')
axs.set_ylim(370.,0)
axs.set_xlim(yminT,ymaxT)
twin1.set_xlim(yminO,ymaxO)
twin2.set_xlim(yminC,ymaxC)
axs.set_ylabel(f'depth (m)',fontsize=16)
axs.set_title(f'')
twin1.set_title(f'')
twin2.set_title(f'')
axs.set_xlabel(f'')
twin1.set_xlabel(f'')
twin2.set_xlabel(f'')
axs.tick_params(axis='y',color='k',labelcolor='k', **tkw)
axs.tick_params(axis='x',color='xkcd:burnt orange',labelcolor='xkcd:burnt orange', **tkw)
twin1.tick_params(axis='x',color='blue',labelcolor='blue',  **tkw)
twin2.tick_params(axis='x',color='green', labelcolor='green', **tkw)
axs.text(0.5, -0.11, 'temperature ($\degree$C)',color='xkcd:burnt orange',transform=axs.transAxes,fontsize=16, va='center',ha='center')
twin2.text(0.5,1.11,'chlorophyll ($mg$ $m^{-3}$)',color='green',transform=twin2.transAxes,fontsize=16, va='center',ha='center')
twin1.text(0.5, -0.31,'dissolved oxygen ($mmol$ $m^{-3}$)',color='blue',transform=twin1.transAxes,fontsize=16,va='center' ,ha='center')
#
fig.suptitle(f'Vertical Profile during NHW & LHl & LChl')
outfile=f'3X_Water_column.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')


