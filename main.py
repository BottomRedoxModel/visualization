import xarray as xr

import one_yr
import z_time
import transect
import x_time
import anim_transect
# import config as cfg
import utils
from model_vs_obs import model_vs_obs
from plot_1D import profiles, depth_timeseries
from profile_plotter import conc_profiles
from datetime import datetime, timedelta


fname = utils.get_fname('Model output')
# read file with model output
#fname = '../BS_br_out.nc' # utils.get_fname('Model output')#
# fname = '//wsl.localhost/Ubuntu-20.04/home/eya/cases/wchips/RT_br_out.nc'

offset = 101
ds = xr.open_dataset(fname)
ds['time'] = ds['time'].to_index() - timedelta(days = offset*365)
ds = ds.isel(time=slice(365*5, None))
#ds = ds.rename({'Waste': 'Woodchip'}).isel(time=slice(1,None))

# TODO: move to the modules
cfg = utils.load_config('config.json')

varnames = cfg["variable_sets"]["brom_state"]
# varnames = utils.read_all_vars(ds)
varnames_sel = cfg["variable_sets"]["brom_state_sel"]
biomass_state_sel = cfg["variable_sets"]["biomass_state_sel"]


# profiles
# TODO: remove idays from here and make a loop in the module?
for iday in cfg["profile_plotter"]["idays"]:
    conc_profiles(ds, iday)

#---------------------------------------------------------------
# VERTICAL PROFILES MODEL VS OBSERVATIONS
#---------------------------------------------------------------
# # read file with observations
# name_obs = utils.get_fname('Observations')
# model_vs_obs(ds, name_obs, plot_sed=False)
# #---------------------------------------------------------------
# # TEMPORAL VARIABILITY OF VERT. DISTRIBUTIONS
# #---------------------------------------------------------------
# # time period (dataset, picname, varnames, nrows, ncols)
# # z_time.fig_ztime(ds, 'ztime-oxy', varnames, cfg.icol_0, 2, 3)
z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames, cfg["plot_1D"]["icol_base"], 8, 6)
#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames, cfg["plot_1D"]["icol_injection"], 8, 6)

#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs_sel', biomass_state_sel, cfg["plot_1D"]["icol_injection"], 5, 4)

#
# # 1 year (dataset, picname, varnames, nrows, ncols)
#one_yr.fig_ztime(ds, 'ztime-brom-waste-1yr', varnames, cfg["plot_1D"]["icol_base"], 8, 6)
#one_yr.fig_ztime(ds, 'ztime-brom-waste-1yr_i', varnames, cfg["plot_1D"]["icol_injection"], 8, 6)
#one_yr.fig_ztime(ds, 'ztime-brom-waste-1yr_i_sel', biomass_state_sel, cfg["plot_1D"]["icol_injection"], 5, 5)

#
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_1p', varnames[:48], cfg.icol_0, 8, 6)
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_2p', varnames[48:96], cfg.icol_0, 8, 6)
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_3p', varnames[96:144], cfg.icol_0, 8, 6)
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_4p', varnames[144:192], cfg.icol_0, 8, 6)

#---------------------------------------------------------------
# plot 1D
#---------------------------------------------------------------
# # profiles(ds)
# # TODO: remove reading of variables here
depth_timeseries(ds, # define subset from the datafile "ds"
                 cfg["variable_sets"]["depth_timeseries_Oslo"], # list of parameters to plot
                 [cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"], # depth, k-number
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"],
                  cfg["case_specific"]["sed"]],
                 ['b','g','r','y','k','m','c','k','y','g'], #colors
                 [False, False, False, False, False,   # negative oriented y-axis
                  False, False, False, False, False],
                 [(None, None), (None, None), (None, None), (None, None), (None, None),   # ranges of changes of parameters
                  (None, None), (None, None), (None, None), (None, None), (None, None)],
                 'time_series_var_swi', #file name
                 )
depth_timeseries(ds,
                 cfg["variable_sets"]["depth_timeseries_Oslo"],
                 [47,47,47,47,47,47,47,47,47,47],
                 ['b','g','r','y','k','m','c','k','y','g'],
                 [False, False, False, False, False,
                  False, False, False, False, False],
                 [(None, None), (None, None), (None, None), (None, None), (None, None),
                  (None, None), (None, None), (None, None), (None, None), (None, None)],
                 'time_series_var_swi+1')
depth_timeseries(ds,
                 cfg["variable_sets"]["depth_timeseries_Oslo"],
                 [48,48,48,48,48,48,48,48,48,48],
                 ['b','g','r','y','k','m','c','k','y','g'],
                 [False, False, False, False, False,
                  False, False, False, False, False],
                 [(None, None), (None, None), (None, None), (None, None), (None, None),
                  (None, None), (None, None), (None, None), (None, None), (None, None)],
                 'time_series_var_swi+2')
depth_timeseries(ds,
                 cfg["variable_sets"]["depth_timeseries_Oslo"],
                 [45,45,45,45,45,45,45,45,45,45],
                 ['b','g','r','y','k','m','c','k','y','g'],
                 [False, False, False, False, False,
                  False, False, False, False, False],
                 [(None, None), (None, None), (None, None), (None, None), (None, None),
                  (None, None), (None, None), (None, None), (None, None), (None, None)],
                 'time_series_var_swi-1')
 #                [(None, None), (None, None), (0, 400000), (7.5, 8.0), (2200, 2800),
 #                 (0, 1), (None, None), (None, None), (None, None), (None, None)],
depth_timeseries(ds,
                 cfg["variable_sets"]["depth_timeseries_flux"],
                [cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"],
                 cfg["case_specific"]["sed"]],
                ['b','g','r','y','k','m','c','k','y'],
                [False,  True, False,False,False,False,False,False,False,False],
                 [(None, None), (None, None), (None, None), (None, None), (None, None),
                  (None, None), (None, None), (None, None), (None, None), (None, None)],
                 'time_series_flux')


#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
#transect.fig_transect(ds, 'transect-2015', varnames, '2012-04-15 00:00:00', 8, 6)
#transect.fig_transect(ds, 'transect-2015', varnames, '2012-07-10 00:00:00', 8, 6)
#transect.fig_transect_depth(ds, 'transect-depth', varnames, '2012-04-15 00:00:00', cfg["transect"]["ilev_1D"], 8, 6)
# for iday in cfg.vidays:
#     vert(ds, iday, cfg.vicol)


#---------------------------------------------------------------
# ANIMATION
#---------------------------------------------------------------
# anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-07-10', '2020-07-30', 3, 3)

#---------------------------------------------------------------
# MAPS
#---------------------------------------------------------------
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
#x_time.fig_map(ds, 'xtime-oxy', biomass_state_sel, 44, 5, 5)
#x_time.fig_map(ds, 'xtime-oxy', varnames, 44, 8, 6)

#x_time.fig_map(ds, 'xtime-oxy', biomass_state_sel, 11, 5, 5)
#x_time.fig_map(ds, 'xtime-oxy', varnames, 11, 8, 6)
