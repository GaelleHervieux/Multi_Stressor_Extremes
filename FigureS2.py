import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import statsmodels.api as sm


dirdata=''
dirout=''

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
#####################################
Tylabel=['HLD','HLD','$\int$CHL','$\int$CHL','$\int$CHL','$\int$CHL','$\int$CHL']
Txlabel=['SST','SST','SST','SST','HLD','HLD']
Ttitle=['75-300 km','0-75 km','75-300 km','0-75 km','75-300 km','0-75 km']
Txvar=[sst75300,sst075,sst75300,sst075,hld75300,hld075]
Tyvar=[hld75300,hld075,chl75300,chl075,chl75300,chl075]
TxGvar=[sstG75300,sstG075,sstG75300,sstG075,hldG75300,hldG075]
TyGvar=[hldG75300,hldG075,chlG75300,chlG075,chlG75300,chlG075]


#############
#############
fig, axs = plt.subplots(nrows=3,ncols=2,figsize=(14,10),num=4,clear=True)
plt.subplots_adjust(bottom=0.11, hspace=0.4,left=0.1)
axs=axs.flatten()
###
for ix in range(0,6):
  cov = np.cov(Txvar[ix].dropna('time'),Tyvar[ix].dropna('time'))
  covG = np.cov(TxGvar[ix].dropna('time'),TyGvar[ix].dropna('time'))
  results = sm.OLS(Txvar[ix].dropna('time').data,sm.add_constant(Tyvar[ix].dropna('time').data)).fit()
  resultsG = sm.OLS(TxGvar[ix].dropna('time').data,sm.add_constant(TyGvar[ix].dropna('time').data)).fit()
  a=results.params[1]
  aG=resultsG.params[1]
  b=results.params[0]
  bG=resultsG.params[0]
  #
  cs0=axs[ix].scatter(Txvar[ix],Tyvar[ix], c='red' ,s=30,edgecolors='red')
  cs1=axs[ix].scatter(TxGvar[ix],TyGvar[ix], c='k' ,s=30,edgecolors='black')
  r0=axs[ix].plot(Txvar[ix].dropna('time').data,Txvar[ix].dropna('time').data* a + b ,c='red')
  r1=axs[ix].plot(TxGvar[ix].dropna('time').data,TxGvar[ix].dropna('time').data* aG + bG,c='k')

###
outfile=f'{dirout}/FigureS2.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
