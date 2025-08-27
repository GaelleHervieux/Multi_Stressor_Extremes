# Created by Gaelle Hervieux
#
# Generate Vertical Profile

# S11 Figure: Composite average anomaly profiles (black dashed contour) of upper ocean 
# temperature (left), chlorophyll (middle), and oxygen (right) during extreme events relative to the 
# full study period (1996–2019). Annual anomaly profiles (solid contours) of each case study 
# period (July 1–June 30) relative to the full study period: 1997–1998 (yellow), 2007–2008 
# (green), 2010–2011 (blue), 2014–2015 (red), and 2015–2016 (purple). For each variable, the 
# nearshore zones 1–4 are displayed on the right and offshore zones 5–8 on the left, just as they 
# appear in Fig 1 (zone numbers increase from south to north). Note, depth ranges (y-axes) differ 
# between variables.

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

# 1- Read Data

### Temp
DS=xr.open_dataset(f'../DATA/VerticalProfile_Temp_MHWcomposite.nc')
ATz=DS['ATemp']
ATCz=DS['ATempC']
### O2
DS=xr.open_dataset(f'../DATA/VerticalProfile_O2_SHXcomposite.nc')
AOz=DS['AO2']
AOCz=DS['AO2C']
### CHL
DS=xr.open_dataset(f'../DATA/VerticalProfile_chl_LCxcomposite.nc')
ACz=DS['AChl']
ACCz=DS['AChlC']

Period=['1996-2019','1997-98','2000-01','2004-05','2007-08','2010-11','2014-15','2015-16']
Nperiod=['9619','9798','0001','0405','0708','1011','1415','1516']
Tdateb=['1996-01-01','1997-07-01','2000-07-01','2004-07-01','2007-07-01','2010-07-01','2014-07-01','2015-07-01']
Tdatee=['2019-12-31','1998-06-30','2001-06-30','2005-06-30','2008-06-30','2011-06-30','2015-06-30','2016-06-30']
Period=['1996-2019','1997-98','2007-08','2010-11','2014-15','2015-16']
#######

Tseason=['ANN','JAS','OND','JFM','AMJ']
Tmonth=[0,7,10,1,4]
#
# -------------------------------
# -------------------------------
Tbox=[8,4,7,3,6,2,5,1]
Nbox=['zone 8','zone 4','zone 7','zone 3','zone 6','zone 2','zone 5','zone 1']
Tcolor=['black','darkorange','dimgrey','darkgrey','green','blue','red','m']

Period=['1996-2019','1997-98','2007-08','2010-11','2014-15','2015-16']
iq=0

# 2 - Plot

yyy=xr.zeros_like(ATz[0,0,0,:])


### Temp
xmin=-2.15
xmax=3.5
fig, axs = plt.subplots(nrows=4,ncols=2,figsize=(10,12),num=3,clear=True)
fig.subplots_adjust(wspace=0.075,hspace=0.1)
axs=axs.flatten()
for ix in range(0,8):
  for ip in [0,1,4,5,6,7]:
    yyy.plot(ax=axs[ix],y='depth',yincrease=False,color='dimgrey',lw=1.,label='')
    if ip==0:
      ATz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],lw=1.75,label=f'A')
      ATCz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],ls='--',lw=2.,label=f'B')
    ATz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],lw=1.75,label=f'C')
    ATCz[0,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[0],ls='--',lw=2.,label=f'B')
  plt.text(0.69, 0.03, f'{Nbox[ix]}', transform=axs[ix].transAxes,fontsize=24)
  axs[ix].set_ylim(370.,0)
  axs[ix].set_xlabel('')
  axs[ix].set_ylabel('')
  axs[ix].set_title('')
  axs[ix].grid()
  axs[ix].set_xlim(xmin,xmax)
  if (ix==1) | (ix==3) |(ix==5) | (ix==7):
    axs[ix].yaxis.tick_right()
    axs[ix].yaxis.set_label_position("right")
    axs[ix].set_yticklabels('',fontsize=18)
    #axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=18)
  else:
    axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=18)
  if ix >=6:
    axs[ix].set_xticklabels(axs[ix].get_xticklabels()[:],fontsize=18)
  else:
    axs[ix].set_xticklabels('')
#
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles[0:3], ['Profile (1996-2019)','MHW Composite (1996-2019)'], loc='lower center',ncol=5, bbox_to_anchor=(0.5,0.91), prop={'size': 10})
fig.legend(handles[3::], Period[:], loc='lower center',ncol=len(Period), bbox_to_anchor=(0.5,0.88), prop={'size': 10})
#
plt.text(-0.3, 0., f'Depth ($m$)',transform=axs[2].transAxes,\
                rotation='vertical',va='center',fontsize=26)
plt.text(-0.4, -0.3, f'Temperature ($\degree$C)',transform=axs[7].transAxes,\
                va='center',fontsize=26)
outfile=f'Temp_VerticalProfile.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')



### CHL

xmin=-0.8
xmax=0.7
fig, axs = plt.subplots(nrows=4,ncols=2,figsize=(10,12),num=3,clear=True)
fig.subplots_adjust(wspace=0.075,hspace=0.1)
axs=axs.flatten()
for ix in range(0,8):
  yyy.plot(ax=axs[ix],y='depth',yincrease=False,color='dimgrey',lw=1.,label='')
  for ip in [0,1,4,5,6,7]:
    if ip==0:
      ACz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],lw=1.75,label='A')
      ACCz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],ls='--',lw=2.,label='B')
    ACz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],lw=1.75,label='C')
    ACCz[0,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[0],ls='--',lw=2.,label='B')
  plt.text(0.69, 0.03, f'{Nbox[ix]}',transform=axs[ix].transAxes,fontsize=24)
  axs[ix].set_ylim(175.,0)
  axs[ix].set_yticks(axs[ix].get_yticks()[::2])
  axs[ix].set_xlabel('')
  axs[ix].set_ylabel('')
  axs[ix].set_title('')
  axs[ix].grid()
  axs[ix].set_xlim(xmin,xmax)
  if (ix==1) | (ix==3) |(ix==5) | (ix==7):
    axs[ix].yaxis.tick_right()
    axs[ix].yaxis.set_label_position("right")
    axs[ix].set_yticklabels('',fontsize=18)
    #axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=16)
  else:
    axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=18)
  if ix >=6:
      axs[ix].set_xticklabels(['-0.8','','-0.4','','0','','0.4','',0.8],fontsize=18)
  else:
    axs[ix].set_xticklabels('')
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles[0:3], ['Profile (1996-2019)','LCX Composite (1996-2019)'], loc='lower center',ncol=5, \
            bbox_to_anchor=(0.5,0.91), prop={'size': 12})
fig.legend(handles[3::], Period[1:], loc='lower center',ncol=len(Period), bbox_to_anchor=(0.5,0.88), prop={'size': 12})
plt.text(-0.3, 0., f'Depth ($m$)',transform=axs[2].transAxes,\
                rotation='vertical',va='center',fontsize=26)
plt.text(-0.4, -0.3, f'chl ($mg$ $m^{-3}$)',transform=axs[7].transAxes,\
                va='center',fontsize=26)
fig.suptitle(f'ANN Profile Chl Anomaly ($mg$ $m^{-3}$) LCX Composite')
outfile=f'CHL_VerticalProfile.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')

### O2
xmin=-43
xmax=63
fig, axs = plt.subplots(nrows=4,ncols=2,figsize=(10,12),num=3,clear=True)
fig.subplots_adjust(wspace=0.075,hspace=0.1)
axs=axs.flatten()
for ix in range(0,8):
  yyy.plot(ax=axs[ix],y='depth',yincrease=False,color='dimgrey',lw=1.,label='')
  for ip in [0,1,4,5,6,7]:
    if ip==0:
      AOz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],lw=1.75,label='A')
      AOCz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],ls='--',lw=2.,label='B')
    AOz[ip,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[ip],lw=1.75,label='C')
    AOCz[0,0,Tbox[ix]-1,:].plot(ax=axs[ix],y='depth',yincrease=False,color=Tcolor[0],ls='--',lw=2.,label='B')
  plt.text(0.69, 0.03, f'{Nbox[ix]}',transform=axs[ix].transAxes,fontsize=24)
  axs[ix].set_ylim(370.,0)
  axs[ix].set_xlabel('')
  axs[ix].set_ylabel('')
  axs[ix].set_title('')
  axs[ix].grid()
  axs[ix].set_xlim(xmin,xmax)
  if (ix==1) | (ix==3) |(ix==5) | (ix==7):
    axs[ix].yaxis.tick_right()
    axs[ix].yaxis.set_label_position("right")
    axs[ix].set_yticklabels('',fontsize=18)
    #axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=16)
  else:
    axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=18)
  if ix >=6:
    axs[ix].set_xticklabels(axs[ix].get_xticklabels()[:],fontsize=18)
  else:
    axs[ix].set_xticklabels('')
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles[0:3], ['Profile (1996-2019)','SHX Composite (1996-2019)'], loc='lower center',ncol=5, bbox_to_anchor=(0.5,0.91), prop={'size': 10})
fig.legend(handles[3::], Period[1:], loc='lower center',ncol=len(Period), bbox_to_anchor=(0.5,0.88), prop={'size': 10})
#
plt.text(-0.3, 0., f'Depth ($m$)',transform=axs[2].transAxes,\
                rotation='vertical',va='center',fontsize=26)
plt.text(-0.4, -0.3, f'o2 ($mmol$ $m^{-3}$)',transform=axs[7].transAxes,\
                va='center',fontsize=26)
outfile=f'O2_VerticalProfile.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
