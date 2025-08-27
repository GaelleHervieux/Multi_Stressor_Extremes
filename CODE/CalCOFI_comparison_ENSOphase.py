# Created by Gaelle Hervieux
#
# Generate figure S3.

# S3 Figure Scatter plots of observed (x-axis) and simulated (y-axis) seasonal standardized 
# anomalies (open black circles) of SST (top row), 0– 100 m integrated chlorophyll concentration 
# (∫Chl; middle row), and HLD (bottom row) from stations along 6 CalCOFI lines, first averaged 
# over the offshore (75-300 km; left column) and nearshore (0-75 km from the coast; right column) 
# coastal bands of the CCLME (see map inset in S2 Fig). Five case study years (July 1–June 30) 
# are indicated by distinct markers and colored by the general ENSO phase (magenta = warm, teal 
# = cool; see key). The 1:1 line is shown in black and correlation coefficients (r) are annotated.
 

import cartopy
import cartopy.crs as ccrs
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


# 1 - Read Data
 
DS=xr.open_dataset(f'../DATA/CalcofiLikeGlorys.nc')
sst75300=DS['sst75300']
sstG75300=DS['sstG75300']
hld75300=DS['hld75300']
hldG75300=DS['hldG75300']
chl75300=DS['chl75300']
chlG75300=DS['chlG75300']
sst075=DS['sst075']
sstG075=DS['sstG075']
hld075=DS['hld075']
hldG075=DS['hldG075']
chl075=DS['chl075']
chlG075=DS['chlG075']
####
#year=pd.date_range("1996-01-01", "2019-12-31", freq="M")
#####################################
#####################################

Period=['1996-2019','1997-1998','2007-2008','2010-2011','2014-2015','2015-2016']
Nperiod=['96-19','97-98','07-08','10-11','14-15','15-16']
Tdateb=['1996-01-01','1997-07-01','2007-07-01','2010-07-01','2014-07-01','2015-07-01']
Tdatee=['2019-12-31','1998-06-30','2008-06-30','2011-06-30','2015-06-30','2016-06-30']

# 2 - Plot

fig, axs = plt.subplots(nrows=3,ncols=2,figsize=(14,11),num=4,clear=True)
plt.subplots_adjust(bottom=0.11,\
        hspace=0.25,wspace=0.1,left=0.15,right=0.88)
axs=axs.flatten()
###
axs[0].scatter(sst75300,sstG75300, c='w' ,s=60,linewidth=2.0,edgecolors='black')
cs0=axs[0].scatter(sst75300.sel(time=slice(Tdateb[1],Tdatee[1])), sstG75300.sel(time=slice(Tdateb[1],Tdatee[1])) , \
  c='w',s=90,marker='*',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs1=axs[0].scatter(sst75300.sel(time=slice(Tdateb[2],Tdatee[2])), sstG75300.sel(time=slice(Tdateb[2],Tdatee[2])) , \
  c='w',s=90,marker='v',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs2=axs[0].scatter(sst75300.sel(time=slice(Tdateb[3],Tdatee[3])), sstG75300.sel(time=slice(Tdateb[3],Tdatee[3])) , \
  c='w',s=90,marker='^',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs3=axs[0].scatter(sst75300.sel(time=slice(Tdateb[4],Tdatee[4])), sstG75300.sel(time=slice(Tdateb[4],Tdatee[4])) , \
  c='w',s=90,marker='X',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs4=axs[0].scatter(sst75300.sel(time=slice(Tdateb[5],Tdatee[5])), sstG75300.sel(time=slice(Tdateb[5],Tdatee[5])) , \
  c='w',s=90,marker='P',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
###
axs[1].scatter(sst075,sstG075, c='w' ,s=60,edgecolors='black',linewidth=2.0)
cs0=axs[1].scatter(sst075.sel(time=slice(Tdateb[1],Tdatee[1])), sstG075.sel(time=slice(Tdateb[1],Tdatee[1])) , \
  c='w',linewidth=2.0,s=90,marker='*',cmap='bwr',vmin=-3,vmax=3,ec='m')
cs1=axs[1].scatter(sst075.sel(time=slice(Tdateb[2],Tdatee[2])), sstG075.sel(time=slice(Tdateb[2],Tdatee[2])) , \
  c='w',linewidth=2.0,s=90,marker='v',cmap='bwr',vmin=-3,vmax=3,ec='c')
cs2=axs[1].scatter(sst075.sel(time=slice(Tdateb[3],Tdatee[3])), sstG075.sel(time=slice(Tdateb[3],Tdatee[3])) , \
  c='w',linewidth=2.0,s=90,marker='^',cmap='bwr',vmin=-3,vmax=3,ec='c')
cs3=axs[1].scatter(sst075.sel(time=slice(Tdateb[4],Tdatee[4])), sstG075.sel(time=slice(Tdateb[4],Tdatee[4])) , \
  c='w',linewidth=2.0,s=90,marker='X',cmap='bwr',vmin=-3,vmax=3,ec='m')
cs4=axs[1].scatter(sst075.sel(time=slice(Tdateb[5],Tdatee[5])), sstG075.sel(time=slice(Tdateb[5],Tdatee[5])) , \
  c='w',linewidth=2.0,s=90,marker='P',cmap='bwr',vmin=-3,vmax=3,ec='m')
axs[1].legend([cs0,cs1,cs2,cs3,cs4],[Nperiod[1],Nperiod[2],Nperiod[3],Nperiod[4],Nperiod[5]],fontsize=18,borderpad=0.1,edgecolor='k',bbox_to_anchor=(1.05,1.5),loc='upper left',handletextpad=0.01)
###
axs[2].scatter(chl75300,chlG75300, c='w' ,s=60,linewidth=2.0,edgecolors='black')
cs0=axs[2].scatter(chl75300.sel(time=slice(Tdateb[1],Tdatee[1])), chlG75300.sel(time=slice(Tdateb[1],Tdatee[1])) , \
  c='w',s=90,marker='*',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs1=axs[2].scatter(chl75300.sel(time=slice(Tdateb[2],Tdatee[2])), chlG75300.sel(time=slice(Tdateb[2],Tdatee[2])) , \
  c='w',s=90,marker='v',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs2=axs[2].scatter(chl75300.sel(time=slice(Tdateb[3],Tdatee[3])), chlG75300.sel(time=slice(Tdateb[3],Tdatee[3])) , \
  c='w',s=90,marker='^',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs3=axs[2].scatter(chl75300.sel(time=slice(Tdateb[4],Tdatee[4])), chlG75300.sel(time=slice(Tdateb[4],Tdatee[4])) , \
  c='w',s=90,marker='X',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs4=axs[2].scatter(chl75300.sel(time=slice(Tdateb[5],Tdatee[5])), chlG75300.sel(time=slice(Tdateb[5],Tdatee[5])) , \
  c='w',s=90,marker='P',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
###
axs[3].scatter(chl075,chlG075, c='w' ,s=60,linewidth=2.0,edgecolors='black')
cs0=axs[3].scatter(chl075.sel(time=slice(Tdateb[1],Tdatee[1])), chlG075.sel(time=slice(Tdateb[1],Tdatee[1])) , \
  c='w',s=90,marker='*',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs1=axs[3].scatter(chl075.sel(time=slice(Tdateb[2],Tdatee[2])), chlG075.sel(time=slice(Tdateb[2],Tdatee[2])) , \
  c='w',s=90,marker='v',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs2=axs[3].scatter(chl075.sel(time=slice(Tdateb[3],Tdatee[3])), chlG075.sel(time=slice(Tdateb[3],Tdatee[3])) , \
  c='w',s=90,marker='^',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs3=axs[3].scatter(chl075.sel(time=slice(Tdateb[4],Tdatee[4])), chlG075.sel(time=slice(Tdateb[4],Tdatee[4])) , \
  c='w',s=90,marker='X',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs4=axs[3].scatter(chl075.sel(time=slice(Tdateb[5],Tdatee[5])), chlG075.sel(time=slice(Tdateb[5],Tdatee[5])) , \
  c='w',s=90,marker='P',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
###
axs[4].scatter(hld75300,hldG75300, c='w' ,s=60,linewidth=2.0,ec='black')
cs0=axs[4].scatter(hld75300.sel(time=slice(Tdateb[1],Tdatee[1])), hldG75300.sel(time=slice(Tdateb[1],Tdatee[1])) , \
  c='w',s=90,marker='*',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs1=axs[4].scatter(hld75300.sel(time=slice(Tdateb[2],Tdatee[2])), hldG75300.sel(time=slice(Tdateb[2],Tdatee[2])) , \
  c='w',s=90,marker='v',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs2=axs[4].scatter(hld75300.sel(time=slice(Tdateb[3],Tdatee[3])), hldG75300.sel(time=slice(Tdateb[3],Tdatee[3])) , \
  c='w',s=90,marker='^',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs3=axs[4].scatter(hld75300.sel(time=slice(Tdateb[4],Tdatee[4])), hldG75300.sel(time=slice(Tdateb[4],Tdatee[4])) , \
  c='w',s=90,marker='X',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs4=axs[4].scatter(hld75300.sel(time=slice(Tdateb[5],Tdatee[5])), hldG75300.sel(time=slice(Tdateb[5],Tdatee[5])) , \
  c='w',s=90,marker='P',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
###
axs[5].scatter(hld075,hldG075, c='w' ,s=60,linewidth=2.0,edgecolors='black')
cs0=axs[5].scatter(hld075.sel(time=slice(Tdateb[1],Tdatee[1])), hldG075.sel(time=slice(Tdateb[1],Tdatee[1])) , \
  c='w',s=90,marker='*',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs1=axs[5].scatter(hld075.sel(time=slice(Tdateb[2],Tdatee[2])), hldG075.sel(time=slice(Tdateb[2],Tdatee[2])) , \
  c='w',s=90,marker='v',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs2=axs[5].scatter(hld075.sel(time=slice(Tdateb[3],Tdatee[3])), hldG075.sel(time=slice(Tdateb[3],Tdatee[3])) , \
  c='w',s=90,marker='^',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='c')
cs3=axs[5].scatter(hld075.sel(time=slice(Tdateb[4],Tdatee[4])), hldG075.sel(time=slice(Tdateb[4],Tdatee[4])) , \
  c='w',s=90,marker='X',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
cs4=axs[5].scatter(hld075.sel(time=slice(Tdateb[5],Tdatee[5])), hldG075.sel(time=slice(Tdateb[5],Tdatee[5])) , \
  c='w',s=90,marker='P',cmap='bwr',vmin=-3,vmax=3,linewidth=2.0,ec='m')
Txvar =[ sst75300, sst075, chl75300, chl075, hld75300, hld075]
TxGvar=[sstG75300,sstG075,chlG75300,chlG075,hldG75300,hldG075]
Tcor=np.zeros((1,len(TxGvar)))
for ix in range(0,6):
  xxx=np.where(np.isnan(TxGvar[ix])==False)
  Tcor[0,ix]=np.round(np.corrcoef(TxGvar[ix][xxx],Txvar[ix][xxx])[0][1],2)
  axs[ix].plot([0, 1], [0, 1], color='k', transform=axs[ix].transAxes)
  if (ix==0) | (ix==2) |(ix==4):
    axs[ix].set_ylabel('GLORYS-BGC',fontsize=20)
  if (ix==4) | (ix==5) :
    axs[ix].set_xlabel('CalCOFI',fontsize=20)
  axs[ix].set_ylim(-3.5,3.5)
  axs[ix].set_xlim(-3.5,3.5)
  axs[ix].set_yticks([-2,0,2])
  axs[ix].set_yticklabels([-2,0,2],fontsize=20)
  axs[ix].set_xticklabels([f'{round(ix)}' for ix in axs[ix].get_xticks()],fontsize=20)
  axs[ix].grid()
  axs[ix].set_title(f'',fontsize=20)
  axs[ix].text(0.018,0.85, f'r=%.2f' % Tcor[0,ix],color='k',transform=axs[ix].transAxes,fontsize=18)
plt.text(-0.4,0.5, f'SST',color='k',va='center',weight='bold',transform=axs[0].transAxes,fontsize=22)
plt.text(-0.4,0.5,\
        f'$\int$CHL',color='k',va='center',weight='bold',transform=axs[2].transAxes,fontsize=22)
plt.text(-0.4,0.5,\
        f'HLD',color='k',va='center',weight='bold',transform=axs[4].transAxes,fontsize=22)
plt.text(0.5,1.3, f'75-300 km',color='k',ha='center',weight='bold',transform=axs[0].transAxes,fontsize=22)
plt.text(0.5,1.3, f'0-75 km',color='k',ha='center',weight='bold',transform=axs[1].transAxes,fontsize=22)
outfile=f'CalCOFI_comparison_ENSOphase.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
