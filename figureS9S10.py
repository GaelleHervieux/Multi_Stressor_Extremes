import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dirout=''
dirdata=''

## ###############################
##  OPEN DATASETS
## ###############################
varname='sMHWLCXSHX'
ncname=f'{dirdata}/DIF_{varname}.nc'
MHW=xr.open_dataset(ncname)
DIF=MHW['DIF']
if varname=='sMHWLCXSHX':
    varlabel='sMHW & LCX & SHX'
    cmap=cm.get_cmap('Greys',34)
    xrnge=np.arange(5,150,15)
    yrnge=np.arange(0,6,1)
elif varname=='sMHW':
    varlabel='sMHW'
    cmap=cm.get_cmap('copper_r',34)
    DIF=DIF/365.
    varlabel=f'{varlabel}/year'
    xrnge=np.arange(0,650,100)
    yrnge=np.arange(0,5,1)
elif varname=='LCX':
    varlabel='LCX'
    cmap=cm.get_cmap('Greens',34)
    DIF=DIF/365.
    varlabel=f'{varlabel}/year'
    xrnge=np.arange(0,650,100)
    yrnge=np.arange(0,5,1)
elif varname=='SHX':
    varlabel='SHX'
    cmap=cm.get_cmap('Purples',34)
    DIF=DIF/365.
    varlabel=f'{varlabel}/year'
    xrnge=np.arange(0,650,100)
    yrnge=np.arange(0,5,1)
elif varname=='sMHWSHX':
    varlabel='sMHW & SHX'
    cmap=cm.get_cmap('RdPu',34)
    xrnge=np.arange(5,150,15)
    yrnge=np.arange(0,6,1)
elif varname=='sMHWLCX':
    varlabel='sMHW & LCX'
    cmap=cm.get_cmap('Oranges',34)
    xrnge=np.arange(5,150,15)
    yrnge=np.arange(0,6,1)
elif varname=='LCXSHX':
    varlabel='LCX & SHX'
    cmap=cm.get_cmap('YlGn',34)
    xrnge=np.arange(5,150,15)
    yrnge=np.arange(0,6,1)


####################
#### PLOT
####################
Tbox=[8,4,7,3,6,2,5,1]
Nbox=['zone 8','zone 4','zone 7','zone 3','zone 6','zone 2','zone 5','zone 1']
vmx=round((np.nanmax(DIF.data)-np.nanmax(DIF.data)*20/100))
#
fig, axs = plt.subplots(nrows=4,ncols=2)
axs=axs.flatten()
#
for ix in range(0,8):
  data=DIF[ix,:,:].T
  sc1=data.plot(ax=axs[ix],levels=np.linspace(0,vmx,20,dtype=int),cmap=cmap)
  axs[ix].set_ylabel('')
  axs[ix].set_xlabel('')
  axs[ix].set_title('')
  axs[ix].set_xlim(5,xrnge[-1])
  axs[ix].set_ylim(yrnge[0],yrnge[-1]
#
plt.suptitle(f'{varlabel}',fontsize=26)
outfile=f'FigureS9.png'
plt.savefig(f'{dirout}/{outfile}')
