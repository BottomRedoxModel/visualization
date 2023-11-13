import xarray as xr
import os
from tkinter.filedialog import askopenfilename
import one_yr
import z_time
import transect
import x_time
import anim_transect
import config as cfg
import matplotlib.pyplot as plt
import numpy as np
import Berre

def get_fname():
    fname = askopenfilename(
        initialdir=os.getcwd(),
        filetypes=(("netcdf file", "*.nc"), ("All Files", "*.*")),
        title="Choose a needed file.")
    return fname


fname = get_fname()
# fname = '../OD_OF_30m_0md.nc'
ds = xr.open_dataset(fname)
all_varnames = ds.keys()
for name in ds.keys(): ##print list of all  variables in ds
  print(name)
vert_varnames = ['Oxy']
oxy_varnames = ['Oxy', 'Phy', 'Het', 'POM', 'DOM', 'NUT',]
carb_varnames = ['DIC', 'Alk','CaCO3',  'pH',  'Om_Ar','CaCO3_form', 'pCO2', 'CO3','CaCO3_diss',]
one_yr_varnames= ['Oxy', 'Phy', 'Het', 'POM', 'DOM', 'NUT', 'pH', 'DIC', 'Alk',]

oxy_diagn_varnames = ['LimLight', 'LimT', 'LimN', 'GrowthPhy','GrazPhy', 'GrazPOM',
                      'DOM_decay_ox', 'DOM_decay_denitr', 'POM_decay_ox', 'POM_decay_denitr',]
bubbl_varnames=['Bubble','r_bub','Bubble_dissolution',
                'sink:Bubble','ch4_o2','fick:CH4',
                'CH4','ch4_so4','fick:Bubble',]
all_and_diagn = ['Oxy', 'Phy', 'Het', 'POM', 'DOM',
                 'NUT', 'pH', 'DIC', 'Alk','CaCO3',
                 'LimLight', 'LimT', 'LimN', 'GrowthPhy','GrazPhy',
                 'GrazPOM','DOM_decay_ox', 'DOM_decay_denitr', 'POM_decay_ox', 'POM_decay_denitr',
                 'pCO2','CH4', ] #'Om_Ar','CaCO3_form','CaCO3_diss']
for_poster_ztime=['DIC', 'Alk', 'pCO2', 'pH', 'CaCO3', 'Om_Ar','CH4',] + ['Bubble','r_bub']
for_poster_transect=['DIC', 'Alk', 'pCO2', 'pH', 'CaCO3', 'Om_Ar','CH4',] + ['Bubble','Oxy']
brom_state_variables = ["Phy","Het","POML","POMR","DOML","DOMR","O2","H2S", "T","S"]
berre_10yr = ["Phy", "Het", "POML", "POMR", "DOML",
              "DOMR", "O2", "NH4", "NO2", "NO3",
              "PO4", "Si", "Baae", "Bhae", "Baan",
              "Bhan", "Fe2", "Fe3", "FeS", "FeCO3",
              "FeS2", "Fe3PO42", "PO4_Fe3", "Mn2", "Mn3",
              "Mn4", "MnS", "MnCO3", "PO4_Mn3", "H2S",
              "S0", "S2O3", "SO4", "Sipart", "DIC",
              "T", "S", "Alk", "LimLight", "LimNO3"]
l = list(ds.keys())
l = [ x for x in l if "sink:" not in x ]
l = [ x for x in l if "fick:" not in x ]
l = [ x for x in l if x not in ["z", "z2", "time", "Ux"] ]
print(l)
print(len(l))
all_vars = l

#---------------------------------------------------------------
# TEMPORAL VARIABILITY OF VERT. DISTRIBUTIONS
#---------------------------------------------------------------

# 1 year (dataset, picname, varnames, nrows, ncols)
#!!one_yr.fig_ztime(ds, '1yr-oxy', one_yr_varnames, cfg.icol_C, 3, 3)
# icol = 0
#one_yr.fig_ztime(ds, 'ztime_1yr', oxy_varnames, cfg.icol_0, 3, 2) # 6,4
#one_yr.fig_ztime(ds, '1yr-carb', carb_varnames, cfg.icol_0, 3, 3)
# # icol = C
# one_yr.fig_ztime(ds, '1yr-carb', carb_varnames, cfg.icol_C, 3, 3)
one_yr.fig_ztime(ds, 'one_yr-Berre_1yr_1p', all_vars[:50], cfg.icol_0, 10, 5)
one_yr.fig_ztime(ds, 'one_yr-Berre_1yr_2p', all_vars[50:100], cfg.icol_0, 10, 5)
one_yr.fig_ztime(ds, 'one_yr-Berre_1yr_3p', all_vars[100:150], cfg.icol_0, 10, 5)
one_yr.fig_ztime(ds, 'one_yr-Berre_1yr_4p', all_vars[150:], cfg.icol_0, 10, 5)
# time period (dataset, picname, varnames, nrows, ncols)
# for icol = 0
#¤z_time.fig_ztime(ds, 'n45col/ztime-oxy0', oxy_varnames, cfg.icol_0, 3, 2)
#¤z_time.fig_ztime(ds, 'n45col/ztime-carb0', carb_varnames, cfg.icol_0, 3, 3)
#¤z_time.fig_ztime(ds, 'n45col/ztime-bubbl0', bubbl_varnames, cfg.icol_0, 3, 3)
######################################################
z_time.fig_ztime(ds, 'ztime-Berre_10yr', berre_10yr, cfg.icol_0, 8, 5)
#z_time.fig_ztime(ds, 'ztime-Berre_2p', all_vars[50:100], cfg.icol_0, 10, 5)
#z_time.fig_ztime(ds, 'ztime-Berre_3p', all_vars[100:150], cfg.icol_0, 10, 5)
#z_time.fig_ztime(ds, 'ztime-Berre_4p', all_vars[150:], cfg.icol_0, 10, 5)
#######################################################
#!z_time.fig_ztime(ds, 'ztime-oxy0', oxy_varnames, cfg.icol_0, 3, 2)
#!z_time.fig_ztime(ds, 'ztime-carb0', carb_varnames, cfg.icol_0, 3, 3)
#!z_time.fig_ztime(ds, 'ztime-bubbl0', bubbl_varnames, cfg.icol_0, 3, 3)
# for icol = C
### z_time.fig_ztime(ds, '45col/ztime-poster', for_poster_ztime, cfg.icol_C, 3, 3)
#!z_time.fig_ztime(ds, 'ztime-oxy', oxy_varnames, cfg.icol_C, 3, 2)
#!z_time.fig_ztime(ds, 'ztime-carb', carb_varnames, cfg.icol_C, 3, 3)
#!z_time.fig_ztime(ds, 'ztime-bubbl', bubbl_varnames, cfg.icol_C, 3, 3)

#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
#!transect.fig_transect(ds, 'transect-2015', for_poster_transect, '2014-10-15 00:00:00', 3, 3)
#!transect.fig_transect(ds, 'transect-2017', for_poster_transect, '2018-10-15 00:00:00', 3, 3)
#transect.fig_transect(ds, '45col/transect-poster-', for_poster_transect, '2020-10-15 00:00:00', 3, 3)
#for tt in cfg.ts_transect:
#    transect.fig_transect(ds, '45col/transect-poster-', for_poster_transect, tt, 3, 3)
# transect.fig_transect(ds, 'transect-oxy_start', oxy_varnames, 0, 3, 2)
# transect.fig_transect(ds, 'transect-oxy_end', oxy_varnames, -1, 3, 2)
#
### transect.fig_transect(ds, '45col/transect-carb_start', carb_varnames, '', 3, 3)
### transect.fig_transect(ds, '45col/transect-carb_end', carb_varnames, '', 3, 3)
#transect.fig_transect(ds, 'transect-bubb_end', bubbl_varnames, -1, 3, 3)

#---------------------------------------------------------------
# ANIMATION
#---------------------------------------------------------------
#anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-07-10', '2020-07-30', 3, 3)
#anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-11-13', '2020-11-25', 3, 3)
#anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2016-11-13', '2016-11-25', 3, 3)
#anim_transect.make_gif('frames', 'out.gif')

#---------------------------------------------------------------
# MAPS
#---------------------------------------------------------------
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
### x_time.fig_map(ds, '45col/xtime-carb_poster', carb_varnames, 0, 3, 3)
# x_time.fig_map(ds, 'xtime-oxy', oxy_varnames, 0, 3, 2)
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
#!x_time.fig_map(ds, 'xtime-oxy', oxy_varnames, cfg.sed, 3, 2)
#!x_time.fig_map(ds, 'xtime-carb', carb_varnames, cfg.sed, 3, 3)
#!x_time.fig_map(ds, 'xtime-carb0', carb_varnames, 0, 3, 3)

#---------------------------------------------------------------
# Berre
#---------------------------------------------------------------
Berre.fig_ztime(ds, 'Berre', berre_10yr, cfg.icol_0, 8, 5)
