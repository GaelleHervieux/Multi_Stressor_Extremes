# Created by Gaelle Hervieux
#
# Generate Nearshore physical and biogeochemical variability in relation to ENSO phase figure.

# Figure 11: Nearshore physical and biogeochemical variability in relation to ENSO phase. 
# (a) From top to bottom, time series of monthly standardized anomalies of the Niño 3.4 
# climate index (brown bars) and nearshore-averaged monthly standardized anomalies of SST 
# (red bars), vertically-integrated (0-100 m) chlorophyll (CHL; green bars), HLD (blue bars), 
# thermocline depth (TD; 3-month running mean; green contour), MLD (3-month running mean; red 
# contour), CUTI (gray bars; black contour indicates the 3-month running mean), 
# vertically-integrated (0-100 m) net primary production (NPP; green bars), 100 m pH (pink bars), 
# and 100 m nitrate (N; teal bars), phosphate (P; gold bars), and silicate (Si; purple bars) 
# concentrations, respectively. All y-axes values have been restricted to a common range and 
# are expressed in sigma units. (b-c) Schematic representation of a simplified view of some of 
# the locally- and remotely-forced responses expected in the nearshore CCLME during a (b) El Niño 
# and (c) La Niña. Positive (+) and negative (-) anomalies in atmospheric winds (northerly, out 
# of the page; southerly, into the page), sea level pressure (SLP), the strength of the 
# Aleutian Low (AL), the type of coastally trapped waves (CTWs; upwelling (↑) or downwelling (↓)), 
# sea surface height (SSH), abundance of primary producers (star and oval shapes), temperature, 
# TD (dashed line), upwelling (solid arrow), pH, oxygen concentration, and nutrient concentration 
# (vertical colored gradient, where darker indicates higher). For illustrative purposes, size, 
# weight, or density is used to indicate the relative differences in scalar properties between 
# ENSO phases.


import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.lines import Line2D
import copy

# 1 - Read Data

ds=xr.open_dataset(f'../DATA/Timeseries_Variables_CCLMEnearshore.nc')
nino34g=ds['nino34']
pdog=ds['pdo']
npgog=ds['npgo']
nppg=ds['npp']
phg=ds['ph']
po4g=ds['po4']
no3g=ds['no3']
sig=ds['si']
cutig=ds['cuti']
tdg=ds['td']
mldg=ds['mld']
sshg=ds['ssh']
sstg=ds['sst']
chlg=ds['chl']
hlg=ds['hld']

nino34s= nino34g.to_series()
pdos= pdog.to_series()
npgos= npgog.to_series()
npps= nppg.to_series()
phs= phg.to_series()
po4s= po4g.to_series()
no3s= no3g.to_series()
sis= sig.to_series()
cutis=cutig.to_series()
tds=tdg.to_series()
mlds=mldg.to_series()
sshs=sshg.to_series()
ssts=sstg.to_series()
chls=chlg.to_series()
hls=hlg.to_series() 

# 2 - Plot

zerg=xr.zeros_like(nino34g)
nbmi=len(npps)//12
nbma=len(npps)//(12*4)

fig, axs = plt.subplots(nrows=13,ncols=1,
                        figsize=(12,12),num=3,clear=True)
axs=axs.flatten()
fig.subplots_adjust(bottom=0.04,top=0.95,left=0.15,right=0.97,hspace=0.2)#
#
axs[0].bar(nino34s.index,nino34s,width=20,alpha=0.75,color='sienna',edgecolor='sienna')
plt.text(-0.07, 0.5, 'NINO3.4', weight='bold',va='center',color='sienna', ha='right',fontsize=12,transform=axs[0].transAxes)
zerg.plot(ax=axs[0],color='dimgrey',linewidth=1.5)
axs[0].set_title(f'')
axs[0].set_xlabel('')
axs[0].set_ylabel('')
axs[0].set_ylim(-2.7,2.7)
axs[0].set_xlim(npps.index[0],npps.index[-1])
axs[0].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[0].set_xticklabels(''*nbma)
axs[0].set_yticks([-2.,2.])
axs[0].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[0].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[0].set_xticklabels(''*nbmi, minor=True)
axs[0].grid(which='major', color='grey', linewidth=1.)
#
axs[1].bar(npgos.index,npgos,width=20,alpha=0.5,color='navy',edgecolor='navy')
pdos.plot(ax=axs[1],color='k',linewidth=1.5)
plt.text(-0.07, 0.7, 'PDO', weight='bold',color='black',va='center', ha='right',fontsize=12,transform=axs[1].transAxes)
plt.text(-0.07, 0.3, 'NPGO', weight='bold',color='navy',va='center', ha='right',fontsize=12,transform=axs[1].transAxes)
zerg.plot(ax=axs[1],color='dimgrey',linewidth=1.5)
axs[1].set_title(f'')
axs[1].set_xlabel('')
axs[1].set_ylabel('')
axs[1].set_ylim(-2.7,2.7)
axs[1].set_xlim(npps.index[0],npps.index[-1])
axs[1].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[1].set_xticklabels(''*nbma)
axs[1].set_yticks([-2.,2.])
axs[1].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[1].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[1].set_xticklabels(''*nbmi, minor=True)
axs[1].grid(which='major', color='grey', linewidth=1.)
#
axs[2].bar(ssts.index,ssts,width=20,color='red',alpha=0.75,edgecolor='red')
plt.text(-0.07, 0.5, 'SST', weight='bold',va='center',ha='right',color='red',fontsize=12, transform=axs[2].transAxes)
zerg.plot(ax=axs[2],color='dimgrey',linewidth=1.5)
axs[2].set_title(f'')
axs[2].set_xlabel('')
axs[2].set_ylabel('')
axs[2].set_ylim(-2.7,2.7)
axs[2].set_xlim(npps.index[0],npps.index[-1])
axs[2].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[2].set_xticklabels(''*nbma)
axs[2].set_yticks([-2.,2.])
axs[2].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[2].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[2].set_xticklabels(''*nbmi, minor=True)
axs[2].grid(which='major', color='grey', linewidth=1.)
#
axs[3].bar(chls.index,chls,width=20,color='green',alpha=0.75,edgecolor='green')
plt.text(-0.07, 0.5, '$\int$CHL', weight='bold',va='center',ha='right',color='green',fontsize=12, transform=axs[3].transAxes)
zerg.plot(ax=axs[3],color='dimgrey',linewidth=1.5)
axs[3].set_title(f'')
axs[3].set_xlabel('')
axs[3].set_ylabel('')
axs[3].set_ylim(-2.7,2.7)
axs[3].set_xlim(npps.index[0],npps.index[-1])
axs[3].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[3].set_xticklabels(''*nbma)
axs[3].set_yticks([-2.,2.])
axs[3].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[3].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[3].set_xticklabels(''*nbmi, minor=True)
axs[3].grid(which='major', color='grey', linewidth=1.)
#
axs[4].bar(hls.index,hls,width=20,color='blue',alpha=0.75,edgecolor='blue')
plt.text(-0.07, 0.5, 'HLD', weight='bold',va='center',ha='right',color='blue',fontsize=12, transform=axs[4].transAxes)
zerg.plot(ax=axs[4],color='dimgrey',linewidth=1.5)
axs[4].set_title(f'')
axs[4].set_xlabel('')
axs[4].set_ylabel('')
axs[4].set_ylim(-2.7,2.7)
axs[4].set_xlim(npps.index[0],npps.index[-1])
axs[4].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[4].set_xticklabels(''*nbma)
axs[4].set_yticks([-2.,2.])
axs[4].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[4].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[4].set_xticklabels(''*nbmi, minor=True)
axs[4].grid(which='major', color='grey', linewidth=1.)
#
tdg.rolling(time=3,center=True).mean('time',skipna=False).plot(ax=axs[5],color='darkolivegreen',linewidth=1.5)
mldg.rolling(time=3,center=True).mean('time',skipna=False).plot(ax=axs[5],color='maroon',linewidth=1.5)
plt.text(-0.07, 0.7, 'TD', color='darkolivegreen',va='center',weight='bold',ha='right',fontsize=12, transform=axs[5].transAxes)
plt.text(-0.07, 0.3, 'MLD', color='maroon',va='center',ha='right', weight='bold',fontsize=12,transform=axs[5].transAxes)
zerg.plot(ax=axs[5],color='dimgrey',linewidth=1.5)
axs[5].set_title(f'')
axs[5].set_xlabel('')
axs[5].set_ylabel('')
axs[5].set_ylim(-2.7,2.7)
axs[5].set_xlim(npps.index[0],npps.index[-1])
axs[5].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[5].set_xticklabels(''*nbma)
axs[5].set_yticks([-2.,2.])
axs[5].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[5].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[5].set_xticklabels(''*nbmi, minor=True)
axs[5].grid(which='major', color='grey', linewidth=1.)
#
axs[6].bar(sshs.index,sshs,width=20,alpha=0.75,color='olive',edgecolor='k')
sshg.rolling(time=3, center=True).mean('time',skipna=False).plot(ax=axs[6],color='k',linewidth=1.5)
plt.text(-0.07, 0.5, 'SSH', weight='bold',ha='right',va='center',color='olive', fontsize=12,transform=axs[6].transAxes)
zerg.plot(ax=axs[6],color='dimgrey',linewidth=1.5)
axs[6].set_title(f'')
axs[6].set_xlabel('')
axs[6].set_ylabel('')
axs[6].set_ylim(-2.7,2.7)
axs[6].set_xlim(npps.index[0],npps.index[-1])
axs[6].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[6].set_xticklabels(''*nbma)
axs[6].set_yticks([-2.,2.])
axs[6].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[6].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[6].set_xticklabels(''*nbmi, minor=True)
axs[6].grid(which='major', color='grey', linewidth=1.)
#
axs[7].bar(cutis.index,cutis,width=20,alpha=0.75,color='grey',edgecolor='grey')
cutig.rolling(time=3, center=True).mean('time',skipna=False).plot(ax=axs[7],color='k',linewidth=1.5)
plt.text(-0.07, 0.5, 'CUTI', color='grey', weight='bold',va='center',ha='right',fontsize=12,transform=axs[7].transAxes)
zerg.plot(ax=axs[7],color='dimgrey',linewidth=1.5)
axs[7].set_title(f'')
axs[7].set_xlabel('')
axs[7].set_ylabel('')
axs[7].set_ylim(-2.7,2.7)
axs[7].set_xlim(npps.index[0],npps.index[-1])
axs[7].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[7].set_xticklabels(''*nbma)
axs[7].set_yticks([-2.,2.])
axs[7].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[7].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[7].set_xticklabels(''*nbmi, minor=True)
axs[7].grid(which='major', color='grey', linewidth=1.)
#
axs[8].bar(npps.index,npps,width=20,color='green',alpha=0.75,edgecolor='green')
plt.text(-0.07, 0.5, '$\int$NPP', weight='bold',va='center',ha='right',color='green',fontsize=12, transform=axs[8].transAxes)
zerg.plot(ax=axs[8],color='dimgrey',linewidth=1.5)
axs[8].set_title(f'')
axs[8].set_xlabel('')
axs[8].set_ylabel('')
axs[8].set_ylim(-2.7,2.7)
axs[8].set_xlim(npps.index[0],npps.index[-1])
axs[8].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[8].set_xticklabels(''*nbma)
axs[8].set_yticks([-2.,2.])
axs[8].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[8].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[8].set_xticklabels(''*nbmi, minor=True)
axs[8].grid(which='major', color='grey', linewidth=1.)
#
axs[9].bar(phs.index,phs,width=20,color='salmon',alpha=0.75,edgecolor='salmon')
plt.text(-0.07, 0.5, 'pH$_{100m}$', color='salmon',weight='bold',va='center',ha='right',fontsize=12, transform=axs[9].transAxes)
zerg.plot(ax=axs[9],color='dimgrey',linewidth=1.5)
axs[9].set_title(f'')
axs[9].set_xlabel('')
axs[9].set_ylabel('')
axs[9].set_ylim(-2.7,2.7)
axs[9].set_xlim(npps.index[0],npps.index[-1])
axs[9].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[9].set_xticklabels(''*nbma)
axs[9].set_yticks([-2.,2.])
axs[9].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[9].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[9].set_xticklabels(''*nbmi, minor=True)
axs[9].grid(which='major', color='grey', linewidth=1.)
#
axs[10].bar(no3s.index,no3s,width=20,color='teal',alpha=0.75,edgecolor='teal')
plt.text(-0.07, 0.5, 'NO3$_{100m}$',weight='bold',ha='right',va='center',color='teal',fontsize=12, transform=axs[10].transAxes)
zerg.plot(ax=axs[10],color='dimgrey',linewidth=1.5)
axs[10].set_title(f'')
axs[10].set_xlabel('')
axs[10].set_ylabel('')
axs[10].set_ylim(-2.7,2.7)
axs[10].set_xlim(npps.index[0],npps.index[-1])
axs[10].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[10].set_xticklabels(''*nbma)
axs[10].set_yticks([-2.,2.])
axs[10].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[10].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[10].set_xticklabels(''*nbmi, minor=True)
axs[10].grid(which='major', color='grey', linewidth=1.)
#
axs[11].bar(po4s.index,po4s,width=20,color='peru',alpha=0.75,edgecolor='peru')
plt.text(-0.07, 0.5, 'PO4$_{100m}$',color='peru',weight='bold',va='center',ha='right',fontsize=12,transform=axs[11].transAxes)
zerg.plot(ax=axs[11],color='dimgrey',linewidth=1.5)
axs[11].set_title(f'')
axs[11].set_xlabel('')
axs[11].set_ylabel('')
axs[11].set_ylim(-2.7,2.7)
axs[11].set_xlim(npps.index[0],npps.index[-1])
axs[11].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[11].set_xticklabels(''*nbma)
axs[11].set_yticks([-2.,2.])
axs[11].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[11].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[11].set_xticklabels(''*nbmi, minor=True)
axs[11].grid(which='major', color='grey', linewidth=1.)
#
axs[12].bar(sis.index,sis,width=20,color='purple',alpha=0.75,edgecolor='purple')
plt.text(-0.07, 0.5, 'SI$_{100m}$',weight='bold',ha='right',va='center',color='purple',fontsize=12, transform=axs[12].transAxes)
zerg.plot(ax=axs[12],color='dimgrey',linewidth=1.5)
axs[12].set_title(f'')
axs[12].set_xlabel('')
axs[12].set_ylabel('')
axs[12].set_ylim(-2.7,2.7)
axs[12].set_xlim(npps.index[0],npps.index[-1])
axs[12].set_xticks(npps.index[::12*4].strftime('%Y'))
axs[12].set_xticklabels(npps.index[::12*4].strftime('%Y'),fontsize=14,rotation='horizontal',ha='center')
axs[12].set_yticks([-2.,2.])
axs[12].set_yticklabels(axs[0].get_yticks(),fontsize=14)
axs[12].set_xticks(npps.index[::12].strftime('%Y'), minor=True)
axs[12].set_xticklabels(''*nbmi, minor=True)
axs[12].grid(which='major', color='grey', linewidth=1.)
###
plt.suptitle(f'Nearshore CCLME',fontsize=20)
outfile=f'Timeseries_Variables_CCLMEnearshore.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
