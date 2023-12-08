import xarray as xr
import config as cfg

import one_yr
import z_time
import transect
import x_time
import anim_transect
import utils
from model_vs_obs import model_vs_obs
import concentration_profiles as conc_prof


ds = xr.open_dataset(cfg.fname)

#---------------------------------------------------------------
# Model vs observation profiles
#---------------------------------------------------------------
conc_prof.plot_fig(ds, colors_vax2, 'set2')

#---------------------------------------------------------------
# Model vs observation profiles
#---------------------------------------------------------------
# name_obs = '../Aqm_Dk1_cleaned.xlsx'  # utils.get_fname('Observations')
# model_vs_obs(ds, name_obs, plot_sed=False)

#---------------------------------------------------------------
# TEMPORAL VARIABILITY OF VERT. DISTRIBUTIONS
#---------------------------------------------------------------
# time period (dataset, picname, varnames, nrows, ncols)
# z_time.fig_ztime(ds, 'ztime-oxy', cfg.varnames, cfg.icol_0, 2, 3)

# 1 year (dataset, picname, varnames, nrows, ncols)
# one_yr.fig_ztime(ds, 'ztime-oxy-1yr', cfg.varnames, cfg.icol_0, 2, 3)

#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
# transect.fig_transect(ds, 'transect-2015', cfg.varnames, '2014-10-15 00:00:00', 2, 3)

#---------------------------------------------------------------
# ANIMATION
#---------------------------------------------------------------
# anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-07-10', '2020-07-30', 3, 3)

#---------------------------------------------------------------
# MAPS
#---------------------------------------------------------------
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
# x_time.fig_map(ds, 'xtime-oxy', cfg.varnames, 0, 3, 2)
