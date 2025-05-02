# Created by Gaelle Hervieux
#
# Generate figure S2.

# S2 Figure Scatter plots of observed (red) and simulated (black) seasonal standardized anomalies 666
# (filled circles) of SST and HLD (top row), SST and 0–100 m integrated chlorophyll 667
# concentration (R CHL; middle row), and HLD and R CHL (bottom row) from stations along 6 668
# CalCOFI lines (map inset; stations overlain on grayscale bathymetry from GLORYS-BGC). 669
# Also shown are regression lines with corresponding regression coefficients, r, and 95% 670
# confidence ellipses. Properties were first averaged over the nearshore (0–75 km from the coast; 671
# gold circles on map; right column of scatter plots) and offshore (75–300 km; teal circles on map; 
# left column of scatter plots) coastal bands of the CCLME. Also shown with scatter plots are 673
# regression lines with corresponding regression coefficients, r, and 95% confidence ellipses. 
 

import cartopy
import cartopy.crs as ccrs
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import statsmodels.api as sm


def get_cov_ellipse(cov, centre, nstd, **kwargs):
    """
    Return a matplotlib Ellipse patch representing the covariance matrix
    cov centred at centre and scaled by the factor nstd.

    """
    # Find and sort eigenvalues and eigenvectors into descending order
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = eigvals.argsort()[::-1]
    eigvals, eigvecs = eigvals[order], eigvecs[:, order]

    # The anti-clockwise angle to rotate our ellipse by
    vx, vy = eigvecs[:,0][0], eigvecs[:,0][1]
    theta = np.arctan2(vy, vx)

    # Width and height of ellipse to draw
    width, height = 2 * nstd * np.sqrt(eigvals)
    return Ellipse(xy=centre, width=width, height=height,
                   angle=np.degrees(theta), **kwargs)


# 1 - Read Data
 
DS=xr.open_dataset(f'../DATA/CalcofiLikeGlorys.nc')
sstC75300=DS['sst75300']
sstG75300=DS['sstG75300']
hldC75300=DS['hld75300']
hldG75300=DS['hldG75300']
chlC75300=DS['chl75300']
chlG75300=DS['chlG75300']
sstC075=DS['sst075']
sstG075=DS['sstG075']
hldC075=DS['hld075']
hldG075=DS['hldG075']
chlC075=DS['chl075']
chlG075=DS['chlG075']
####
#year=pd.date_range("1996-01-01", "2019-12-31", freq="M")
#####################################
#####################################
Tylabel=['HLD','HLD','$\int$Chl','$\int$Chl','$\int$Chl','$\int$Chl','$\int$Chl']
Txlabel=['SST','SST','SST','SST','HLD','HLD']
Ttitle=['75-300 km','0-75 km','75-300 km','0-75 km','75-300 km','0-75 km']
Txvar=[sstC75300,sstC075,sstC75300,sstC075,hldC75300,hldC075]
Tyvar=[hldC75300,hldC075,chlC75300,chlC075,chlC75300,chlC075]
TxGvar=[sstG75300,sstG075,sstG75300,sstG075,hldG75300,hldG075]
TyGvar=[hldG75300,hldG075,chlG75300,chlG075,chlG75300,chlG075]



# 2 - Plot

fig, axs = plt.subplots(nrows=3,ncols=2,figsize=(14,10),num=4,clear=True)
plt.subplots_adjust(bottom=0.11, hspace=0.4,left=0.1)
axs=axs.flatten()
###
for ix in range(0,6):
  cov = np.cov(Txvar[ix].where(~np.isnan(Tyvar[ix])).dropna('time'),Tyvar[ix].where(~np.isnan(Txvar[ix])).dropna('time'))
  covG =np.cov(TxGvar[ix].where(~np.isnan(TyGvar[ix])).dropna('time'),TyGvar[ix].where(~np.isnan(TxGvar[ix])).dropna('time'))
  e = get_cov_ellipse(cov, (np.nanmean(Txvar[ix]),np.nanmean(Tyvar[ix]) ), 2,fc='none', lw=1.5,ec='red')
  eG = get_cov_ellipse(covG, (np.nanmean(TxGvar[ix]),np.nanmean(TyGvar[ix])), 2,fc='none',lw=1.5,ec='black')
  results =sm.OLS(Txvar[ix].where(~np.isnan(Tyvar[ix])).dropna('time').data, \
          sm.add_constant(Tyvar[ix].where(~np.isnan(Txvar[ix])).dropna('time').data)).fit()
  resultsG =sm.OLS(TxGvar[ix].where(~np.isnan(TyGvar[ix])).dropna('time').data, \
                  sm.add_constant(TyGvar[ix].where(~np.isnan(TxGvar[ix])).dropna('time').data)).fit()
  a=results.params[1]
  aG=resultsG.params[1]
  b=results.params[0]
  bG=resultsG.params[0]
  #
  cs0=axs[ix].scatter(Txvar[ix],Tyvar[ix], c='red' ,s=30,edgecolors='red')
  cs1=axs[ix].scatter(TxGvar[ix],TyGvar[ix], c='k' ,s=30,edgecolors='black')
  r0=axs[ix].plot(Txvar[ix].dropna('time').data,Txvar[ix].dropna('time').data* a + b ,c='red')
  r1=axs[ix].plot(TxGvar[ix].dropna('time').data,TxGvar[ix].dropna('time').data* aG + bG,c='k')
  axs[ix].add_artist(e)
  axs[ix].add_artist(eG)
  axs[ix].set_ylabel(f'{Tylabel[ix]}',fontsize=20)
  axs[ix].set_xlabel(f'{Txlabel[ix]}',fontsize=20)
  axs[ix].set_ylim(-4.1,4.1)
  axs[ix].set_xlim(-4.1,4.1)
  axs[ix].set_yticklabels([f'{round(ix)}' for ix in axs[ix].get_yticks()],fontsize=16)
  axs[ix].set_xticklabels([f'{round(ix)}' for ix in axs[ix].get_xticks()],fontsize=16)
  axs[ix].grid()
  axs[ix].set_title(f'')
  plt.text(0.01,0.85, f'r=%.2f' % a,color='red',transform=axs[ix].transAxes,fontsize=14)
  plt.text(0.01,0.75, f'   %.2f' % aG,color='k', transform=axs[ix].transAxes,fontsize=14)
  if ix==0:
    axs[ix].set_title(f'{Ttitle[ix]}',fontsize=20,color='xkcd:sea',weight='bold')
    axs[ix].legend([cs0,cs1],['CalCOFI','GLORYS-BGC'],loc='upper left',ncol=2, bbox_to_anchor=(0.62,1.5),fontsize=20)
  if ix==1:
    axs[ix].set_title(f'{Ttitle[ix]}',fontsize=20,color='xkcd:saffron',weight='bold')
###
outfile=f'CalCOFI_comparison_Ellipse.png'
plt.savefig(outfile, dpi=150, facecolor='w', edgecolor='w', orientation='portrait')
