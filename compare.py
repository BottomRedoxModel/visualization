import xarray as xr

import utils
import compare_maps
import compare_transects

# TODO: move to the modules
cfg = utils.load_config('config.json')

ds_codes = ['DS1', 'DS2', 'DS3']
fnames = [
    'e:/Users/EY/cases/0308a1c5%s1500i4800/RT_br_out.nc',
    'e:/Users/EY/cases/0309a1c5%s750i4800/RT_br_out.nc',
    'e:/Users/EY/cases/0309a1c5%s375i4800/RT_br_out.nc',
]

datasets_to_compare = []
for fname in fnames:

    ds = xr.open_dataset(fname)
    ds = ds.rename({'Waste': 'Woodchip'}).isel(time=slice(1,None))
    datasets_to_compare.append(ds)


compare_maps.fig_map_compare(datasets_to_compare, 'maps_compared',
                             cfg['variable_sets']['compare_maps'], 44,
                             3, 2,
                             ([0, 5], [175, 290]))  # limits

# (dss, picname, varnames, t0, lims)
compare_transects.fig_transect_compare(datasets_to_compare, 'transects_compared',
                             cfg['variable_sets']['compare_transects'], '2012-04-15 00:00:00',
                             3, 2,
                             ([0, 5e-5], [180, 350]),    # limits WATER COLUMN
                             ([0, 1e5], [0, 200]) )     # limits SEDIMENT