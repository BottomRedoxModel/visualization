import xarray as xr
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import os
import pandas as pd
import numpy as np

def get_fname(title):
    fname = askopenfilename(
        initialdir=os.getcwd(),
        title=title)
    return fname

name_ds = get_fname('Model output')
name_obs = get_fname('Observations')
datemin = np.datetime64('2065-01-01')  # start
datemax = np.datetime64('2066-01-01')  # stop
dstep = 2  # plot every Nth day
zswi = 12  # index of SWI
zswi2 = 10

# name_ds = 'BROM_Seva.nc'
# name_obs = 'obs_SevBay.xls'

ds = xr.open_dataset(name_ds)
ds = ds.sel(time=slice(datemin, datemax))
wat = pd.read_excel(name_obs, sheet_name=0)
sed = pd.read_excel(name_obs, sheet_name=1)

# read depthes
zs = ds['z'].values
zsed = ((zs - zs[zswi])*100)
# pairs of plotted variables
# {'obs': 'model_var'} or
# {'obs': ['model_var1', 'model_var2']
# - in this case sum model_var1 + model_var2
pairs = {'O2 uM': 'O2',
          'Alk uM': 'Alk',
          'pH': 'pH',
          'NH4 uM': 'NH4',
          'SiO3 uM': 'Si',
         'PO4 uM': 'PO4',
          'NO2+NO3 uM': ['NO2', 'NO3'],
          'Fe (II) uM': 'Fe2',
          'H2S uM': 'H2S',
          'Mn (II) uM': 'Mn2',
          'Corg uM': ['DOMR', 'POML' ,'POMR' ,'DOML'] * 7
          }

fig = plt.figure(figsize=(15, 15))
gs0 = fig.add_gridspec(3, 4, hspace=0.2, wspace=0.15)

for (k, v), gs in zip(pairs.items(), gs0):
    print(k)
    # get model data
    if type(v) != list:
        md = ds[v].values[:,:,0]
    else:  # if a list is passed, we sum it (but only for 2 arrays)))
        md = ds[v[0]].values[:,:,0] + ds[v[1]].values[:,:,0]

    gs2 = gs.subgridspec(2, 1, height_ratios=(2,1), hspace=0.3)
    axw = fig.add_subplot(gs2[0])  # axis for water column
    axsed = fig.add_subplot(gs2[1])  # axis for sediments

    # WATER COLUMN
    axw.set_title(k)
    axw.invert_yaxis()
    axw.grid(axis='y')
    axw.axhspan(17,-0.5, color='dodgerblue', alpha=0.2)
    axw.set_ylim(17,-0.5)
    # model curves
    md_summer = md[91:273, :]
    md_winter = md[np.r_[0:91, 273:365], :]
#    md_winter = md[np.r_[0:91, 273:365], :]
    axw.plot(md_summer[::dstep,:zswi].T, zs[:zswi], color='coral', alpha=0.3)
    axw.plot(md_winter[::dstep,:zswi].T, zs[:zswi], color='royalblue', alpha=0.3)
    # observations
    if k in list(wat.columns):
        axw.scatter(wat[k], wat['depth m'], c='navy', zorder=10)

    # SEDIMENTS
    axsed.invert_yaxis()
    axsed.grid(axis='y')
    axsed.set_ylim(15, -5)
    axsed.axhspan(15,0, color='sandybrown', alpha=0.3)
    axsed.axhspan(0,-10, color='dodgerblue', alpha=0.2)
    # model curves
    axsed.plot(md_summer[::dstep,zswi2:].T, zsed[zswi2:], color='coral', alpha=0.3)
    axsed.plot(md_winter[::dstep,zswi2:].T, zsed[zswi2:], color='royalblue', alpha=0.3)
    # observations
    if k in list(sed.columns):
        depth = sed['depth mm']/10  # from mm to cm
        axsed.scatter(sed[k], depth, c='crimson', zorder=10)

plt.savefig('test_mod_obs.png', dpi=200, bbox_inches='tight')

