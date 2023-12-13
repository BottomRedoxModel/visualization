import xarray as xr
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import os
import pandas as pd
import numpy as np
import config as cfg
import utils
import seaborn as sns

'''
Now this module is adapted for data from AquaMonitor
Need to make it more general
'''

# pairs of plotted variables
# {'obs': 'model_var'} or
# {'obs': ['model_var1', 'model_var2']
# - in this case sum model_var1 + model_var2
pairs = {'O2 uM': 'O2',
         'SiO2 uM': 'Si',
         'PO4 uM': 'PO4',
         'NO3 uM': 'NO3',
          }

# not sure if it is the best solution
# maybe make them datetime directly in config?
datemin = cfg.t1_mod_vs_obs  # start
datemax = cfg.t2_mod_vs_obs  # stop
dstep = cfg.mod_tstep  # Nth days
icol = 0

wdepth_name = 'depth m'
seddepth_name = 'depth cm'

def model_vs_obs(ds, name_obs, plot_sed=True):
    # water: depth in m
    # sed: depth in cm, z-axis down (increases with depth of sediment)
    
    ds = ds.sel(time=slice(datemin, datemax))
    months = ds['time'].dt.month.values
    twinter = np.isin(months, [1, 2, 3, 11, 12])
    tsummer = np.isin(months, [4, 5, 6, 7, 8, 9, 10])

    wat = pd.read_excel(name_obs, sheet_name='water')

    # convert units to moles
    wat = utils.unit_conversion(wat, mode='mass to moles')
    wat = utils.make_season(wat, 'SampleDate')
    if plot_sed:
        sed = pd.read_excel(name_obs, sheet_name='sediment')
        sed = utils.unit_conversion(sed, mode='mass to moles')
        sed = utils.make_season(wat, 'SampleDate')
    
    # read model depthes
    zs = ds['z'].values
    zsed = ((zs - zs[cfg.sed])*100)

    # figure
    # TODO: make the size automatically depending on nrows,ncols
    fig = plt.figure(figsize=(15, 15))
    # nrows, ncols
    gs0 = fig.add_gridspec(2, 2, hspace=0.2, wspace=0.15)
    
    for (k, v), gs in zip(pairs.items(), gs0):
        print(k)

        # get model data
        md_winter = ds[v].load().sel(time=twinter).values[:,:,icol]
        md_summer = ds[v].load().sel(time=tsummer).values[:,:,icol]

        # create 1 or 2 panels depending on plot_sed flag
        if plot_sed:
            gs2 = gs.subgridspec(2, 1, height_ratios=(2,1), hspace=0.3)
        else:
            gs2 = gs.subgridspec(1, 1)
        axw = fig.add_subplot(gs2[0])  # axis for water column

        # WATER COLUMN
        axw.set_title(k)
        axw.invert_yaxis()
        axw.grid(axis='y')
        axw.axhspan(wat[wdepth_name].max(), -0.5, color='dodgerblue', alpha=0.2)
        axw.set_ylim(top=-0.5)

        # model curves
        axw.plot(md_summer[::dstep,:cfg.sed].T, zs[:cfg.sed], color='coral', alpha=0.3)
        axw.plot(md_winter[::dstep,:cfg.sed].T, zs[:cfg.sed], color='royalblue', alpha=0.3)

        # observations
        if k in list(wat.columns):
            sns.scatterplot(data=wat, x=k, y=wdepth_name,
                            hue='season',
                            size=2, palette=['navy', 'crimson'],
                            ax=axw)
    
        # SEDIMENTS
        if plot_sed:
            axsed = fig.add_subplot(gs2[1])  # axis for sediments

            axsed.invert_yaxis()
            axsed.grid(axis='y')
            axsed.set_ylim(15, -5)
            axsed.axhspan(15,0, color='sandybrown', alpha=0.3)
            axsed.axhspan(0,-10, color='dodgerblue', alpha=0.2)

            # model curves
            axsed.plot(md_summer[::dstep,cfg.sed2:].T, zsed[cfg.sed2:], color='coral', alpha=0.3)
            axsed.plot(md_winter[::dstep,cfg.sed2:].T, zsed[cfg.sed2:], color='royalblue', alpha=0.3)

            # observations
            if k in list(sed.columns):
                sns.scatterplot(data=sed, x=k, y=seddepth_name,
                                hue='season',
                                size=2, palette=['navy', 'crimson'],
                                ax=axw)
    
    plt.savefig('test_mod_obs.png', dpi=200, bbox_inches='tight')

