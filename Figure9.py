import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datadir=''
dirout=''
#
### READ DATA FILE
#
ds=xr.open_dataset(f'{datadir}/Figure9.nc')
nino=ds['nino34']
pdo=ds['pdo']
npgo=ds['npgo']
ssh=ds['ssh']
cuti=ds['cuti']
td=ds['td']
mld=ds['mld']
sst=ds['sst']
botT=ds['botT']
chl=ds['chl']
hld=ds['hld']
npp=ds['npp']
si=ds['si']
no3=ds['no3']
po4=ds['po4']
ph=ds['ph']

#
### PLOT
#
fig, axs = plt.subplots(nrows=13,ncols=1)
axs=axs.flatten()
#
axs[0].bar(nino34.index,nino34s,width=20,alpha=0.75,color='sienna',edgecolor='sienna')
axs[1].bar(npgo.index,npgos,width=20,alpha=0.5,color='navy',edgecolor='navy')
pdo.plot(ax=axs[1],color='k',linewidth=1.5)
axs[2].bar(sst.index,ssts,width=20,color='red',alpha=0.75,edgecolor='red')
axs[3].bar(chl.index,chls,width=20,color='green',alpha=0.75,edgecolor='green')
axs[4].bar(hld.index,hls,width=20,color='blue',alpha=0.75,edgecolor='blue')
td.plot(ax=axs[5],color='darkolivegreen',linewidth=1.5)
mld.plot(ax=axs[5],color='maroon',linewidth=1.5)
ssh.plot(ax=axs[6],color='k',linewidth=1.5)
cuti.plot(ax=axs[7],color='k',linewidth=1.5)
axs[9].bar(phs.index,phs,width=20,color='salmon',alpha=0.75,edgecolor='salmon')
axs[10].bar(no3s.index,no3s,width=20,color='teal',alpha=0.75,edgecolor='teal')
axs[11].bar(po4s.index,po4s,width=20,color='peru',alpha=0.75,edgecolor='peru')
axs[12].bar(sis.index,sis,width=20,color='purple',alpha=0.75,edgecolor='purple')
###
outfile=f'{dirout}/Figure9.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
