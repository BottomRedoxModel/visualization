import xarray as xr

# import config as cfg
import utils
import one_yr
import z_time
import transect
import x_time
import anim_transect
from datetime import datetime, timedelta
from model_vs_obs import model_vs_obs
from plot_1D import profiles, depth_timeseries
from profile_plotter import conc_profiles

fname = utils.get_fname('Model output')
# read file with model output
# fname = '../BS_br_out.nc' # utils.get_fname('Model output')#
# fname = '//wsl.localhost/Ubuntu-20.04/home/eya/cases/wchips/RT_br_out.nc'

offset =  0 # 101
ds = xr.open_dataset(fname)
ds['time'] = ds['time'].to_index() - timedelta(days = offset*365)
# ds["fick:Ci_partic"] = ds["fick:Ci_POM"] + ds["fick:Ci_phy"] + ds["fick:Ci_het"]
# ds["fick:Ci_dissolved"] = ds["fick:Ci_free"] + ds["fick:Ci_DOM"]
# ds["sink:Ci_partic"] = ds["sink:Ci_POM"] + ds["sink:Ci_phy"] + ds["sink:Ci_het"]
ds["POM"] = ds["POML"] + ds["POMR"]
ds["DOM"] = ds["DOML"] + ds["DOMR"]
# ds["Ci_biota"] = ds["Ci_phy"] + ds["Ci_het"]
# ds["Ci_in_biota"] = ds["Ci_in_biota"] #/ 1000.
ds['z'] = ds['z']
# ds['Ci_tot_biodegrad'] = ds['Ci_tot_biodegrad']
# ds = ds.isel(time=slice(365*5, None))
#ds = ds.rename({'Waste': 'Woodchip'}).isel(time=slice(1,None))

# TODO: move to the modules
cfg = utils.load_config('config.json')

varnames = cfg["variable_sets"]["brom_state"]
varnames_all = utils.read_all_vars(ds)
varnames_sel = cfg["variable_sets"]["brom_state_sel"]
biomass_state_sel = cfg["variable_sets"]["biomass_state_sel"]
varnames_ni = cfg["variable_sets"]["brom_state_Ni"]
varnames_ba = cfg["variable_sets"]["brom_state_Ba"]
varnames_subst = cfg["variable_sets"]["brom_state_subst"]
varnames_ci = cfg["variable_sets"]["brom_state_ci"]
varnames_ci_short = cfg["variable_sets"]["brom_state_ci_short"]
varnames_ci_diagn = cfg["variable_sets"]["brom_state_ci_diagn"]

# profiles
#---------------------------------------------------------------
# VERTICAL PROFILES ALL VARIABLES
#---------------------------------------------------------------
#  TODO: remove idays from here and make a loop in the module?
for iday in cfg["profile_plotter"]["idays"]:
    conc_profiles(ds, iday)
####for iday in cfg["profile_plotter"]["idays"]:
#conc_profiles(ds, 7300)
#conc_profiles(ds, 7485)
#conc_profiles(ds, 10000)
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
#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames_ni, cfg["plot_1D"]["icol_base"], 8, 6)
#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames_ni, cfg["plot_1D"]["icol_injection"], 8, 6)
# z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames, cfg["plot_1D"]["icol_base"], 8, 6)
#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames_ba, cfg["plot_1D"]["icol_base"], 8, 6)
# z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', varnames_subst, cfg["plot_1D"]["icol_base"], 8, 6)
# z_time.fig_ztime(ds, 'ztime-BROM-all-yrs-ci', varnames_ci, cfg["plot_1D"]["icol_base"], 4, 3)
# z_time.fig_ztime(ds, 'ztime-BROM-all-yrs-ci_short', varnames_ci_short, cfg["plot_1D"]["icol_base"], 3, 2)

#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs-ci-diagn', varnames_ci_diagn, cfg["plot_1D"]["icol_base"], 6, 3)

#z_time.fig_ztime(ds, 'ztime-BROM-all-yrs_sel', biomass_state_sel, cfg["plot_1D"]["icol_injection"], 5, 4)

# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
#transect.fig_transect(ds, 'transect-2030', varnames, '2030-04-15 00:00:00', 8, 6)

#
# # 1 year (dataset, picname, varnames, nrows, ncols)
#one_yr.fig_ztime(ds, 'ztime-brom-waste-1yr', varnames, cfg["plot_1D"]["icol_base"], 8, 6)
#one_yr.fig_ztime(ds, 'ztime-brom-waste-1yr_i', varnames, cfg["plot_1D"]["icol_injection"], 8, 6)
#one_yr.fig_ztime(ds, 'ztime-brom-waste-1yr_i_sel', biomass_state_sel, cfg["plot_1D"]["icol_injection"], 5, 5)

# #
# one_yr.fig_ztime(ds, 'ztime-BROM-1yr_1p', varnames_all[:48], cfg["plot_1D"]["icol_base"], 8, 6)
# one_yr.fig_ztime(ds, 'ztime-BROM-1yr_2p', varnames_all[48:96], cfg["plot_1D"]["icol_base"], 8, 6)
# one_yr.fig_ztime(ds, 'ztime-BROM-1yr_3p', varnames_all[96:144], cfg["plot_1D"]["icol_base"], 8, 6)
# one_yr.fig_ztime(ds, 'ztime-BROM-1yr_4p', varnames_all[144:192], cfg["plot_1D"]["icol_base"], 8, 6)
# one_yr.fig_ztime(ds, 'ztime-BROM-1yr_5p', varnames_all[192:240], cfg["plot_1D"]["icol_base"], 8, 6)

# one_yr.fig_ztime(ds, 'ztime-BROM-1yr_Ci', varnames_ci, cfg["plot_1D"]["icol_base"], 6, 2)

"""
one_yr.fig_ztime(ds, 'ztime-BROM-1yr_1p', varnames_all[:48], cfg["plot_1D"]["icol_injection"], 8, 6)
one_yr.fig_ztime(ds, 'ztime-BROM-1yr_2p', varnames_all[48:96], cfg["plot_1D"]["icol_injection"], 8, 6)
one_yr.fig_ztime(ds, 'ztime-BROM-1yr_3p', varnames_all[96:144], cfg["plot_1D"]["icol_injection"], 8, 6)
one_yr.fig_ztime(ds, 'ztime-BROM-1yr_4p', varnames_all[144:192], cfg["plot_1D"]["icol_injection"], 8, 6)
"""
#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
#transect.fig_transect(ds, 'transect-2015', varnames, '2012-04-15 00:00:00', 8, 6)
#for d in cfg["transect"]["timesteps"]:
#    transect.fig_transect(ds, 'transect-2022', varnames_ni, d, 8, 6)
#transect.fig_transect_depth(ds, 'transect-depth', varnames, '2022-04-15 00:00:00', cfg["transect"]["ilev_1D"], 8, 6)
# for iday in cfg.vidays:
#     vert(ds, iday, cfg.vicol)


#---------------------------------------------------------------
# MAPS
#---------------------------------------------------------------
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
#x_time.fig_map(ds, 'xtime-oxy', biomass_state_sel, 44, 5, 5)
#x_time.fig_map(ds, 'xtime-oxy', biomass_state_sel, 11, 5, 5)
#x_time.fig_map(ds, 'xtime-oxy', varnames, 11, 8, 6)

#---------------------------------------------------------------
# plot 1D
#---------------------------------------------------------------
# # profiles(ds)
# # TODO: remove reading of variables here
# depth_timeseries(ds, # define subset from the datafile "ds"
#                  cfg["variable_sets"]["depth_timeseries_ci"], # list of parameters to plot
#                  [cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"], # depth, k-number
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"]],
#                  ['b','g','r','y','k','m','c','k','y','g'], #colors
#                  [False, False, False, False, False,   # negative oriented y-axis
#                   False, False, False, False, False],
#                  [(None, None), (None, None), (None, None), (None, None), (None, None),   # ranges of changes of parameters
#                   (None, None), (None, None), (None, None), (None, None), (None, None)],
#                  'time_series_swi_ci', #file name
#                  )
# depth_timeseries(ds, # define subset from the datafile "ds"
#  #                cfg["variable_sets"]["depth_timeseries_Ni"], # list of parameters to plot
#                  cfg["variable_sets"]["depth_timeseries_ci_flux"], # list of parameters to plot
#                  [cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"], # depth, k-number
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"]],
#                  ['b','g','r','y','k','m','c','k','y','g'], #colors
#                  [True, True, True, True, True,   # negative oriented y-axis
#                   False, False, False, False, False],
#                  [(None, None), (None, None), (None, None), (None, None), (None, None),   # ranges of changes of parameters
#                   (None, None), (None, None), (None, None), (None, None), (None, None)],
#                  'time_series_swi_ci_flux', #file name
#                  )
# depth_timeseries(ds, # define subset from the datafile "ds"
#  #                cfg["variable_sets"]["depth_timeseries_Ni"], # list of parameters to plot
#                  cfg["variable_sets"]["depth_timeseries_ci_flux_sum"], # list of parameters to plot
#                  [cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"], # depth, k-number
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"],
#                   cfg["case_specific"]["sed"]],
#                  ['b','g','r','y','k','m','c','k','y','g'], #colors
#                  [True, True, True, True, True,   # negative oriented y-axis
#                   False, False, False, False, False],
#                  [(None, None), (None, None), (None, None), (None, None), (None, None),   # ranges of changes of parameters
#                   (None, None), (None, None), (None, None), (None, None), (None, None)],
#                  'time_series_swi_ci_flux_sum', #file name
#                  )

#---------------------------------------------------------------
# ANIMATION
#---------------------------------------------------------------
# anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-07-10', '2020-07-30', 3, 3)

