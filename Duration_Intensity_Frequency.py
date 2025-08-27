# Created by Gaelle Hervieux
#
# Generate Intensity–duration–frequency relationships for single extreme events 
# across zones and Intensity–duration–frequency relationships for compound extreme 
# events across zones figures.


# Figure 4: Intensity–duration–frequency relationships for single extreme events 
# across zones. Single extremes of SMHWs (browns; left), LCXs (greens; middle), and 
# SHXs (purples; right) are binned by duration (x-axis; days), intensity (y-axis; 
# standardized and expressed in sigma units), and frequency (color; average number 
# of events per year) from 1996 to 2019. Markers (+) are overlain to represent the median 
# of the distribution. Each extreme displays the nearshore zones 1–4 on the right and 
# offshore zones 5–8 on the left, just as they appear in Figure 1 (zone numbers increase 
# from south to north). Note, colorbar ranges differ between extremes.

# Figure 6: Intensity–duration–frequency relationships for compound extreme events across 
# zones. Compound extremes of SMHW-LCXs (oranges; left), LCX-SHXs (greens; second from left), 
# SMHW-SHXs (pinks; second from right), and SMHW-LCX-SHXs (grays; right) are binned by 
# duration (x-axis; days), intensity (y-axis; standardized and expressed in sigma units (𝛹′)), 
# and frequency (color; number of events per year) from 1996 to 2019. Markers (+) are overlain 
# to represent the median of the distribution. Each extreme displays the nearshore zones 1–4 
# on the right and offshore zones 5–8 on the left, just as they appear in Figure 1 (zone 
# numbers increase from south to north). Note, colorbar ranges differ between extremes 
# and the LCX-SHX y axis has been restricted to display the most common range across extremes, 
# hiding an outlier event found in the 9.75-10𝜎 intensity and 5-7 day duration bin.

# 1 - Read Data

Tvar=['sMHW' ,'LCX' ,'SHX', 'sMHWLCX' ,'LCXSHX' ,'sMHWSHX', 'sMHWLCXSHX']
for ivar in Tvar[:]:
  varname=ivar
  ncname=f'../DATA/DIF_{varname}.nc'
  MHW=xr.open_dataset(ncname)
  DIF=MHW['DIF']
  Dm=MHW['Duration_median']
  Im=MHW['Intensity_median']
  DIF=DIF/24.
  vmx=round((np.nanmax(DIF.data)))
  if varname=='sMHWLCXSHX':
    vartitle='SMHW-LCX-SHX'
    cmap=cm.get_cmap('Greys',34)
    xrnge=np.arange(5,190,15)
  elif varname=='sMHW':
    vartitle='SMHW'
    cmap=cm.get_cmap('copper_r',34)
    xrnge=np.arange(0,650,100)
  elif varname=='LCX':
    vartitle='LCX'
    cmap=cm.get_cmap('Greens',34)
    xrnge=np.arange(0,650,100)
  elif varname=='SHX':
    vartitle='SHX'
    cmap=cm.get_cmap('Purples',34)
    xrnge=np.arange(0,650,100)
  elif varname=='sMHWSHX':
    vartitle='SMHW-SHX'
    cmap=cm.get_cmap('RdPu',34)
    xrnge=np.arange(5,190,15)
  elif varname=='sMHWLCX':
    cmap=cm.get_cmap('Oranges',34)
    xrnge=np.arange(5,190,15)
  elif varname=='LCXSHX':
    vartitle='LCX-SHX'
    cmap=cm.get_cmap('YlGn',34)
    xrnge=np.arange(5,190,15)
  yrnge=np.arange(0,6,1)
  cmaplist = [cmap(i) for i in range(10,cmap.N)]
  new_cmap = colors.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, 24)

# 2 - Plot

  Tbox=[8,4,7,3,6,2,5,1]
  Nbox=['zone 8','zone 4','zone 7','zone 3','zone 6','zone 2','zone 5','zone 1']
  #
  fig, axs = plt.subplots(nrows=4,ncols=2,figsize=(9,14),num=2,clear=True)
  fig.subplots_adjust(bottom=0.18, top=0.92, wspace=0.075,hspace=0.14)
  axs=axs.flatten()
  #
  for ix in range(0,8):
    data=DIF[Tbox[ix]-1,:,:].T
    if (varname=='sMHW')|(varname=='LCX')|(varname=='SHX'):
      sc1=data.plot(ax=axs[ix],levels=np.linspace(1/24.,vmx,20,dtype=int),cmap=new_cmap,add_colorbar = False)
    elif (varname=='sMHWLCX'):
      clev=np.arange(0,160,10)
      sc1=data.plot(ax=axs[ix],levels=clev,cmap=new_cmap,add_colorbar = False)
    elif (varname=='sMHWSHX'):
      clev=np.arange(0,52,4)
      sc1=data.plot(ax=axs[ix],levels=clev,cmap=new_cmap,add_colorbar = False)
    elif (varname=='LCXSHX'):
      clev=np.arange(0,14,1)
      sc1=data.plot(ax=axs[ix],levels=clev,cmap=new_cmap,add_colorbar = False)
    elif (varname=='sMHWLCXSHX'):
      clev=np.arange(0,4.25,0.25)
      sc1=data.plot(ax=axs[ix],levels=clev,cmap=new_cmap,add_colorbar = False)
    axs[ix].scatter(Dm[Tbox[ix]-1],Im[Tbox[ix]-1],marker='+',ec='k',s=80,c='None',zorder=30,linewidths=2)
    if (varname=='sMHWLCXSHX'):
      axs[ix].scatter(Dm[Tbox[ix]-1],Im[Tbox[ix]-1],marker='+',ec='r',s=80,c='None',zorder=30,linewidths=2)
    axs[ix].set_ylabel('')
    axs[ix].set_xlabel('')
    axs[ix].set_title('')
    axs[ix].set_xlim(5,xrnge[-1])
    axs[ix].set_ylim(yrnge[0],yrnge[-1])
    axs[ix].set_xticks(xrnge[:])
    axs[ix].set_yticks(yrnge)
    axs[ix].grid()
    plt.text(0.67, 0.03, f'{Nbox[ix]}',transform=axs[ix].transAxes,fontsize=24)
    if (ix==1) | (ix==3) |(ix==5) | (ix==7):
      axs[ix].yaxis.tick_right()
      axs[ix].yaxis.set_label_position("right")
      axs[ix].set_yticklabels('',fontsize=18)
    else:
      axs[ix].set_yticklabels(axs[ix].get_yticklabels()[:],fontsize=18)
    if ix >=6:
      if (varname=='sMHW')|(varname=='LCX')|(varname=='SHX'):
        axs[ix].set_xticks(xrnge[:-1])
        axs[ix].set_xticklabels(axs[ix].get_xticklabels()[:],fontsize=18)
      else:
        axs[ix].set_xticklabels(['','20','','50','','80','','110','','140','','170',''],fontsize=18)
    else:
      axs[ix].set_xticklabels('')
  #
  plt.text(-0.25, 0., f'Intensity ($\sigma$)',transform=axs[2].transAxes,\
                rotation='vertical',va='center',fontsize=26)
  plt.text(-0.35, -0.35, f'Duration (Days)',transform=axs[7].transAxes,\
                va='center',fontsize=26)
  cbar_ax = fig.add_axes([0.11, 0.07, 0.8, 0.015])
  if (varname=='sMHW')|(varname=='LCX'):
    clev=np.linspace(1/24,vmx,20,dtype=int)
    cbar=fig.colorbar(sc1,cax=cbar_ax,orientation='horizontal',ticks=clev[1::2])
  elif (varname=='SHX'):
    clev=np.linspace(1/24,vmx,20,dtype=int)
    cbar=fig.colorbar(sc1,cax=cbar_ax,orientation='horizontal',ticks=clev[2::2])
  else:
    cbar=fig.colorbar(sc1,cax=cbar_ax,orientation='horizontal',ticks=clev[1::2])#,format='%.2f')
  cbar.set_label(label=f'Frequency (Events/year)',fontsize=16)
  cbar.ax.tick_params(labelsize=16)
  cbar.ax.minorticks_off()
  #
  plt.suptitle(f'{vartitle}',fontsize=26)
  plt.savefig(f'DIF_{varname}.png')
