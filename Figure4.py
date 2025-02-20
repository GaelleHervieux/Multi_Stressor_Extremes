import xarray as xr
import matplotlib.pyplot as plt


dirplots=''
dirdata=''



## ###############################
##  OPEN DATASETS
## ###############################

DS=xr.open_dataset(f'{dirdata}/Figure3.nc')
SST=DS['SST']
SST90thE=DS['sst90th'].sel(dayofyear=SST.time.dt.dayofyear)
SST10thE=DS['sst10th'].sel(dayofyear=SST.time.dt.dayofyear)
chl=DS['chl']
chl90thE=DS['chl90th'].sel(dayofyear=SST.time.dt.dayofyear)
chl10thE=DS['chl10th'].sel(dayofyear=SST.time.dt.dayofyear)
o2=DS['HLD']
o290thE=DS['HLD90th'].sel(dayofyear=SST.time.dt.dayofyear)
o210thE=DS['HLD10th'].sel(dayofyear=SST.time.dt.dayofyear)
T=DS['botT']
T90thE=DS['botT90th'].sel(dayofyear=T.time.dt.dayofyear)
T10thE=DS['botT10th'].sel(dayofyear=T.time.dt.dayofyear)

#######################
Period=['1997-1998','2007-2008','2010-2011','2014-2015','2015-2016']
Tdateb=['1997-07-01','2007-07-01','2010-07-01','2014-07-01','2015-07-01']
Tdatee=['1998-06-30','2008-06-30','2011-07-01','2015-06-30','2016-06-30']

################# PLOTS
fig, axs = plt.subplots(nrows=4,ncols=len(Period))
axs=axs.flatten()
###
for ip in range(0,len(Period)):
  year = DSchl.sel(time=slice(Tdateb[ip],Tdatee[ip])).indexes['time'].to_datetimeindex()
  ###
  axs[0+ip].plot(year,SST.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='red',linewidth=1.2,label='SST')
  axs[0+ip].plot(year,SST10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='red',linestyle='dashed',linewidth=1.,label='10th percentile of SST')
  axs[0+ip].plot(year,SST90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='red',linestyle='dashed',linewidth=1.,label='90th percentile of SST')
  axs[0+ip].plot(year,SSTclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='red',linestyle='dotted',linewidth=1.2,label='seasonal cycle of SST')

  #
  axs[len(Period)+ip].plot(year,chl.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='green',linewidth=1.2,label='chlIntV')
  axs[len(Period)+ip].plot(year,chl10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='green',linestyle='dashed',linewidth=1.,label='10th percentile of [chlIntV]')
  axs[len(Period)+ip].plot(year,chl90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='green',linestyle='dashed',linewidth=1.,label='90th percentile of [chlIntV]')
  axs[len(Period)+ip].plot(year,chlclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='green',linestyle='dotted',linewidth=1.2,label='seasonal cycle of [chlIntV]')
  #
  axs[len(Period)*2+ip].plot(year,-o2.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='blue',linewidth=1.2,label='Hypoxic Layer')
  axs[len(Period)*2+ip].plot(year,-o210thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='blue',linestyle='dashed',linewidth=1.,label='10th percentile of HI')
  axs[len(Period)*2+ip].plot(year,-o290thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='blue',linestyle='dashed',linewidth=1.,label='90th percentile of HI')
  axs[len(Period)*2+ip].plot(year,-o2climE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='blue',linestyle='dotted',linewidth=1.2,label='seasonal cycle of HI')
  #
  axs[len(Period)*3+ip].plot(year,T.sel(time=slice(Tdateb[ip],Tdatee[ip])),color='black',linewidth=1.2,label='Bot Temp')
  axs[len(Period)*3+ip].plot(year,T10thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='black',linestyle='dashed',linewidth=1.,label='10th percentile of Bot T')
  axs[len(Period)*3+ip].plot(year,T90thE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='black',linestyle='dashed',linewidth=1.,label='90th percentile of Bot T')
  axs[len(Period)*3+ip].plot(year,TclimE.sel(time=slice(Tdateb[ip],Tdatee[ip])), color='black',linestyle='dotted',linewidth=1.2,label='seasonal cycle of Bot T')
#
outfile=f'{dirout}/Figure4.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
