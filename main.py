import xarray as xr

import one_yr
import z_time
import transect
import x_time
import anim_transect
import config as cfg
import utils
from model_vs_obs import model_vs_obs
from plot_1D import profiles, depth_timeseries

# read file with model output
fname = utils.get_fname('Model output')
ds = xr.open_dataset(fname)

varnames = utils.read_all_vars(ds)  # cfg.varnames
#---------------------------------------------------------------
# VERTICAL PROFILES MODEL VS OBSERVATIONS
#---------------------------------------------------------------
# # read file with observations
# if cfg.plot_obs_n_mod:
#    name_obs = utils.get_fname('Observations')
#    model_vs_obs(ds, name_obs, plot_sed=False)
# #---------------------------------------------------------------
# # TEMPORAL VARIABILITY OF VERT. DISTRIBUTIONS
# #---------------------------------------------------------------
# # time period (dataset, picname, varnames, nrows, ncols)
# # z_time.fig_ztime(ds, 'ztime-oxy', varnames, cfg.icol_0, 2, 3)
# z_time.fig_ztime(ds, 'ztime-BROM-all-yrs', cfg.brom_state_variables, cfg.icol_0, 8, 6)
#
# # 1 year (dataset, picname, varnames, nrows, ncols)
# # one_yr.fig_ztime(ds, 'ztime-oxy-1yr', varnames, cfg.icol_0, 2, 3)
#
# if cfg.plot_1year:
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_1p', varnames[:48], cfg.icol_0, 8, 6)
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_2p', varnames[48:96], cfg.icol_0, 8, 6)
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_3p', varnames[96:144], cfg.icol_0, 8, 6)
#     one_yr.fig_ztime(ds, 'ztime-BROM-1yr_4p', varnames[144:192], cfg.icol_0, 8, 6)
#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
# transect.fig_transect(ds, 'transect-2015', varnames, '2014-10-15 00:00:00', 2, 3)

#---------------------------------------------------------------
# ANIMATION
#---------------------------------------------------------------
# anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-07-10', '2020-07-30', 3, 3)

#---------------------------------------------------------------
# MAPS
#---------------------------------------------------------------
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
# x_time.fig_map(ds, 'xtime-oxy', varnames, 0, 3, 2)

# plot 1D
# profiles(ds)
depth_timeseries(ds, ["O2", "O2", "NH4", "DOML"],
                 [cfg.sed, cfg.sed+1, cfg.sed, 20],
                 ['b', 'g', 'r', 'y'],
                 offset=91)  # adjust years here