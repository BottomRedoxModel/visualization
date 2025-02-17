import xarray as xr #used for 2d and 3d data

import utils #FILE
import compare_maps #FILE
import compare_transects #FILE


# TODO: move to the modules
#Loading configuration file
cfg = utils.load_config('config.yaml')

#Defining codes for dataset. Lists with file paths to the datasets
ds_codes = ['DS1', 'DS2', 'DS3']
fnames = [
    'e:/Users/EY/cases/0308a1c5%s1500i4800/RT_br_out.nc',
    'e:/Users/EY/cases/0309a1c5%s750i4800/RT_br_out.nc',
    'e:/Users/EY/cases/0309a1c5%s375i4800/RT_br_out.nc',
]

#Makes a list to save the datasets that will is compared
datasets_to_compare = []
for fname in fnames:

    ds = xr.open_dataset(fname)
    ds = ds.rename({'Waste': 'Woodchip'}).isel(time=slice(1,None)) #changing name and choses time
    datasets_to_compare.append(ds) #adds the datasets in the list

#Comparing maps for the datasets and saves the result as maps_compared
#Running fig_maps_compare from compare_maps to compare the maps data.
compare_maps.fig_map_compare(datasets_to_compare, 'maps_compared',
                             cfg['variable_sets']['compare_maps'], 44, #list of variables that will be compared. 44 is a parameter
                             3, 2, #rows, columns in the figure (3x2)
                             ([0, 5], [175, 290]))  # limits #axe limits

#compare transect - makes a figure to comparing transects (vertical profiles of data)
# (dss, picname, varnames, t0, lims)
compare_transects.fig_transect_compare(datasets_to_compare, 'transects_compared',
                             cfg['variable_sets']['compare_transects'], '2012-04-15 00:00:00', #the variables that will be compared (from config.yaml)
                             3, 2, #3 rows, 2 columns
                             ([0, 5e-5], [180, 350]),    # limits WATER COLUMN
                             ([0, 1e5], [0, 200]) )     # limits SEDIMENT