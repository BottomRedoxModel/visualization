import xarray as xr

import utils
import compare_maps
import compare_transects

# TODO: move to the modules
cfg = utils.load_config('config.json')

ds_codes = ['DS1', 'DS2', 'DS3']
datasets_to_compare = []
for ds_code in ds_codes:
    # fname = utils.get_fname(ds_code)
    fname = '../w0206_0.nc'
    ds = xr.open_dataset(fname)
    ds = ds.rename({'Waste': 'Woodchip'}).isel(time=slice(1,None))
    datasets_to_compare.append(ds)


compare_maps.fig_map_compare(datasets_to_compare, 'maps_compared',
                             cfg['variable_sets']['compare_maps'], 44,
                             3, 2,
                             ([0, 50], [250, 300]))  # limits

# (dss, picname, varnames, t0, lims)
compare_transects.fig_transect_compare(datasets_to_compare, 'transects_compared',
                             cfg['variable_sets']['compare_transects'], '2012-04-15 00:00:00',
                             3, 2,
                             ([0, 2e-5], [250, 320]),    # limits WATER COLUMN
                             ([0, 1e6], [0, 220]) )     # limits SEDIMENT