# Created by Gaelle Hervieux
#
# Generate Annual snapshots of nearshore extremes during five case study periods figure.

# Figure 9: Annual snapshots of nearshore extremes during five case study periods. Daily time series 
# (solid contours) of nearshore extreme variables (rows; same as in Figure 3) isolated during a single 
# year (July 1–June 30) of five case study periods (columns): from left to right, 1997–1998 (El Niño), 
# 2007-2008 (La Niña), 2010–2011 (La Niña), 2014–2015 (“Blob”), and 2015–2016 (El Niño), respectively. 
# Additional contours indicate the daily climatology (dotted) and both the 90th and 10th percentiles (dashed). 
# High and low extreme events of each ocean variable are indicated with gray under-the-curve and vertical 
# shading (refer to Table 1). Note the inverted y-axis for HLD (third row). 

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.lines import Line2D

# 1 - Read Data
# 
ds=xr.open_dataset('../DATA/Timeseries_CCLME_0-75km.nc')
SST=ds['SST']
SSTclimE=SST.groupby('time.dayofyear').mean('time').sel(dayofyear=SST.time.dt.dayofyear)
SST90thE=ds['sst90th'].sel(dayofyear=SST.time.dt.dayofyear)
SST10thE=ds['sst10th'].sel(dayofyear=SST.time.dt.dayofyear)
chl=ds['chl']
chlclimE=chl.groupby('time.dayofyear').mean('time').sel(dayofyear=SST.time.dt.dayofyear)
chl90thE=ds['chl90th'].sel(dayofyear=SST.time.dt.dayofyear)
chl10thE=ds['chl10th'].sel(dayofyear=SST.time.dt.dayofyear)
hld=-ds['HLD']
hldclimE=hld.groupby('time.dayofyear').mean('time').sel(dayofyear=SST.time.dt.dayofyear)
hld90thE=-ds['HLD90th'].sel(dayofyear=SST.time.dt.dayofyear)
hld10thE=-ds['HLD10th'].sel(dayofyear=SST.time.dt.dayofyear)
T=ds['botT']
TclimE=T.groupby('time.dayofyear').mean('time').sel(dayofyear=SST.time.dt.dayofyear)
T90thE=ds['botT90th'].sel(dayofyear=T.time.dt.dayofyear)
T10thE=ds['botT10th'].sel(dayofyear=T.time.dt.dayofyear)
unitssst='$\degreeC$'
unitsT='$\degree$C'
unitschl='$mg m-2$'
unitso2='$m$'

Period=['1997-1998','2007-2008','2010-2011','2014-2015','2015-2016']
Tdateb=['1997-07-01','2007-07-01','2010-07-01','2014-07-01','2015-07-01']
Tdatee=['1998-06-30','2008-06-30','2011-07-01','2015-06-30','2016-06-30']

# 2 - Plot

fig, axs = plt.subplots(nrows=4,ncols=len(Period),figsize=(16,8),num=2,clear=True)
fig.subplots_adjust(hspace=.05,wspace=.1,top=0.9)
axs=axs.flatten()

###
for ip in range(0,len(Period)):
  year = ds.sel(time=slice(Tdateb[ip],Tdatee[ip])).indexes['time'].to_datetimeindex()
  ###
  axs[0+ip].plot(year,SST.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='red',linewidth=1.2,label='SST')
  axs[0+ip].plot(year,SST10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='red',linestyle='dashed',linewidth=1.,label='10th percentile of SST')
  axs[0+ip].plot(year,SST90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='red',linestyle='dashed',linewidth=1.,label='90th percentile of SST')
  axs[0+ip].plot(year,SSTclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='red',linestyle='dotted',linewidth=1.2,label='seasonal cycle of SST')
  axs[0+ip].fill_between(year,SST.sel(time=slice(Tdateb[ip],Tdatee[ip])),SST90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(SST.sel(time=slice(Tdateb[ip],Tdatee[ip]))>SST90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  axs[0+ip].fill_between(year,SST.sel(time=slice(Tdateb[ip],Tdatee[ip])),SST10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(SST.sel(time=slice(Tdateb[ip],Tdatee[ip]))<SST10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  #axs[0+ip].grid(c='k',lw=0.4)
  axs[0+ip].set_ylabel('')
  axs[0+ip].set_xlim(year[0],year[-1])
  axs[0+ip].xaxis.set_major_locator(mdates.MonthLocator())
  axs[0+ip].set_xticklabels([])
  axs[0+ip].set_ylim(axs[0+ip].get_ylim()[0],axs[0+ip].get_ylim()[1])
  #
  axs[len(Period)+ip].plot(year,chl.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='green',linewidth=1.2,label='chlIntV')
  axs[len(Period)+ip].plot(year,chl10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='green',linestyle='dashed',linewidth=1.,label='10th percentile of [chlIntV]')
  axs[len(Period)+ip].plot(year,chl90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='green',linestyle='dashed',linewidth=1.,label='90th percentile of [chlIntV]')
  axs[len(Period)+ip].plot(year,chlclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='green',linestyle='dotted',linewidth=1.2,label='seasonal cycle of [chlIntV]')
  axs[len(Period)+ip].fill_between(year,chl.sel(time=slice(Tdateb[ip],Tdatee[ip])),chl10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(chl10thE.sel(time=slice(Tdateb[ip],Tdatee[ip]))>chl.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  axs[len(Period)+ip].fill_between(year,chl.sel(time=slice(Tdateb[ip],Tdatee[ip])),chl90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(chl90thE.sel(time=slice(Tdateb[ip],Tdatee[ip]))<chl.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  #axs[len(Period)+ip].grid(c='k',lw=0.4)
  axs[len(Period)+ip].set_ylabel('')
  axs[len(Period)+ip].set_xlim(year[0],year[-1])
  axs[len(Period)+ip].xaxis.set_major_locator(mdates.MonthLocator())
  axs[len(Period)+ip].set_xticklabels([])
  axs[len(Period)+ip].set_ylim(axs[len(Period)+ip].get_ylim()[0],axs[len(Period)+ip].get_ylim()[1])
  #
  axs[len(Period)*2+ip].plot(year,hld.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='blue',linewidth=1.2,label='Hypoxic Layer')
  axs[len(Period)*2+ip].plot(year,hld10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='blue',linestyle='dashed',linewidth=1.,label='10th percentile of HI')
  axs[len(Period)*2+ip].plot(year,hld90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='blue',linestyle='dashed',linewidth=1.,label='90th percentile of HI')
  axs[len(Period)*2+ip].plot(year,hldclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='blue',linestyle='dotted',linewidth=1.2,label='seasonal cycle of HI')
  axs[len(Period)*2+ip].fill_between(year,hld.sel(time=slice(Tdateb[ip],Tdatee[ip])),hld10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(hld10thE.sel(time=slice(Tdateb[ip],Tdatee[ip]))<hld.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  axs[len(Period)*2+ip].fill_between(year,hld.sel(time=slice(Tdateb[ip],Tdatee[ip])),hld90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(hld90thE.sel(time=slice(Tdateb[ip],Tdatee[ip]))>hld.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  #axs[len(Period)*2+ip].grid(c='k',lw=0.4)
  axs[len(Period)*2+ip].set_ylabel('')
  axs[len(Period)*2+ip].set_xlim(year[0],year[-1])
  axs[len(Period)*2+ip].xaxis.set_major_locator(mdates.MonthLocator())
  axs[len(Period)*2+ip].set_xticklabels([])
  axs[len(Period)*2+ip].set_ylim(axs[len(Period)*2+ip].get_ylim()[0],axs[len(Period)*2+ip].get_ylim()[1])
  axs[len(Period)*3+ip].plot(year,T.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='black',linewidth=1.2,label='Bot Temp')
  axs[len(Period)*3+ip].plot(year,T10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='black',linestyle='dashed',linewidth=1.,label='10th percentile of Bot T')
  axs[len(Period)*3+ip].plot(year,T90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='black',linestyle='dashed',linewidth=1.,label='90th percentile of Bot T')
  axs[len(Period)*3+ip].plot(year,TclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='black',linestyle='dotted',linewidth=1.2,label='seasonal cycle of Bot T')
  axs[len(Period)*3+ip].fill_between(year,T.sel(time=slice(Tdateb[ip],Tdatee[ip])),T90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(T.sel(time=slice(Tdateb[ip],Tdatee[ip]))>T90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  axs[len(Period)*3+ip].fill_between(year,T.sel(time=slice(Tdateb[ip],Tdatee[ip])),T10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), \
    np.where(T.sel(time=slice(Tdateb[ip],Tdatee[ip]))<T10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),color='grey', alpha=0.5)
  #axs[len(Period)*3+ip].grid(c='k',lw=0.4)
  axs[len(Period)*3+ip].set_ylabel('')
  axs[len(Period)*3+ip].set_xlim(year[0],year[-1])
  axs[len(Period)*3+ip].xaxis.set_major_locator(mdates.MonthLocator())
  axs[len(Period)*3+ip].set_xticklabels(["A",'','O','','D','','F','','A','','J'],fontsize=16)
  axs[len(Period)*3+ip].set_ylim(axs[len(Period)*3+ip].get_ylim()[0],axs[len(Period)*3+ip].get_ylim()[1])
  if ip==0:
    axs[0].text(-0.5,0.5,unitsT,fontsize=17,transform=axs[0].transAxes,rotation='vertical',va='center')
    axs[len(Period)].text(-0.5,0.5,unitschl,fontsize=17,transform=axs[len(Period)].transAxes,rotation='vertical',va='center')
    axs[len(Period)*2].text(-0.5,0.5,unitso2,fontsize=17,transform=axs[len(Period)*2].transAxes,rotation='vertical',va='center')
    axs[len(Period)*3].text(-0.5,0.5,unitsT,fontsize=17,transform=axs[len(Period)*3].transAxes,rotation='vertical',va='center')
    axs[0].set_title('1997-98',fontsize=20)
    axs[1].set_title('2007-08',fontsize=20)
    axs[2].set_title('2010-11',fontsize=20)
    axs[3].set_title('2014-15',fontsize=20)
    axs[4].set_title('2015-16',fontsize=20)
    axs[0].set_yticklabels([round(ix) for ix in axs[0].get_yticks()],fontsize=16)
    axs[len(Period)].set_yticklabels([round(ix) for ix in axs[len(Period)].get_yticks()],fontsize=16)
    axs[len(Period)*2].set_yticklabels([round(-ix) for ix in axs[len(Period)*2].get_yticks()[:-1]],fontsize=16)
    axs[len(Period)*3].set_yticklabels([ix for ix in axs[len(Period)*3].get_yticks()],fontsize=16)
  else:
    axs[0+ip].set_yticklabels('')
    axs[len(Period)+ip].set_yticklabels('')
    axs[len(Period)*2+ip].set_yticklabels('')
    axs[len(Period)*3+ip].set_yticklabels('')
###
for ix in range(0,len(Period)):
  axs[0+ix].set_ylim(min([axs[0+ip].get_ylim()[0] for ip in range(0,len(Period))]),max([axs[0+ip].get_ylim()[1] for ip in range(0,len(Period))]))
  axs[len(Period)+ix].set_ylim(min([axs[len(Period)+ip].get_ylim()[0] for ip in range(0,len(Period))]),max([axs[len(Period)+ip].get_ylim()[1] for ip in range(0,len(Period))]))
  axs[len(Period)*2+ix].set_ylim(min([axs[len(Period)*2+ip].get_ylim()[0] for ip in range(0,len(Period))]),max([axs[len(Period)*2+ip].get_ylim()[1] for ip in range(0,len(Period))]))
  axs[len(Period)*3+ix].set_ylim(min([axs[len(Period)*3+ip].get_ylim()[0] for ip in range(0,len(Period))]),max([axs[len(Period)*3+ip].get_ylim()[1] for ip in range(0,len(Period))]))
#
for ip in range(0,len(Period)):
  year = ds.sel(time=slice(Tdateb[ip],Tdatee[ip])).indexes['time'].to_datetimeindex()
  f1=axs[0+ip].fill_between(year,axs[0+ip].get_ylim()[0],axs[0+ip].get_ylim()[1],\
    np.where(SST.sel(time=slice(Tdateb[ip],Tdatee[ip]))>SST90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[0+ip].fill_between(year,axs[0+ip].get_ylim()[0],axs[0+ip].get_ylim()[1],\
    np.where(SST.sel(time=slice(Tdateb[ip],Tdatee[ip]))<SST10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[len(Period)+ip].fill_between(year,axs[len(Period)+ip].get_ylim()[0],axs[len(Period)+ip].get_ylim()[1],\
    np.where(chl.sel(time=slice(Tdateb[ip],Tdatee[ip]))>chl90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[len(Period)+ip].fill_between(year,axs[len(Period)+ip].get_ylim()[0],axs[len(Period)+ip].get_ylim()[1],\
    np.where(chl.sel(time=slice(Tdateb[ip],Tdatee[ip]))<chl10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[len(Period)*2+ip].fill_between(year,axs[len(Period)*2+ip].get_ylim()[0],axs[len(Period)*2+ip].get_ylim()[1],\
    np.where(hld.sel(time=slice(Tdateb[ip],Tdatee[ip]))<hld90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[len(Period)*2+ip].fill_between(year,axs[len(Period)*2+ip].get_ylim()[0],axs[len(Period)*2+ip].get_ylim()[1],\
    np.where(hld.sel(time=slice(Tdateb[ip],Tdatee[ip]))>hld10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[len(Period)*3+ip].fill_between(year,axs[len(Period)*3+ip].get_ylim()[0],axs[len(Period)*3+ip].get_ylim()[1],\
    np.where(T.sel(time=slice(Tdateb[ip],Tdatee[ip]))>T90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)
  f1=axs[len(Period)*3+ip].fill_between(year,axs[len(Period)*3+ip].get_ylim()[0],axs[len(Period)*3+ip].get_ylim()[1],\
    np.where(T.sel(time=slice(Tdateb[ip],Tdatee[ip]))<T10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])),True,False),\
    color='grey', alpha=0.3,edgecolor=None)#
fig.suptitle(f'Annual snapshots of nearshore extremes during five case study periods')
outfile=f'Timeseries_CCLME_0-75km_snapshots.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')




