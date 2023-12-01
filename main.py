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

# TODO: transfer to utils
def get_fname():
    fname = askopenfilename(
        initialdir=os.getcwd(),
        filetypes=(("netcdf file", "*.nc"), ("All Files", "*.*")),
        title="Choose a needed file.")
    return fname

fname = get_fname()

ds = xr.open_dataset(fname)
all_varnames = ds.keys()
oxy_varnames = ['Oxy', 'Phy', 'Het', 'POM', 'DOM', 'NUT',]
carb_varnames = ['DIC', 'Alk','CaCO3',  'pH',  'Om_Ar','CaCO3_form', 'pCO2', 'CO3','CaCO3_diss',]

brom_state_variables = ["Phy", "Het", "POML", "POMR", "DOML", "DOMR",
                        "O2", "NH4", "NO2", "NO3", "PO4", "Si",
                        "Baae", "Bhae", "Baan", "Bhan", "Fe2", "Fe3",
                        "FeS", "FeCO3", "FeS2", "Fe3PO42", "PO4_Fe3", "Mn2",
                        "Mn3", "Mn4", "MnS", "MnCO3", "PO4_Mn3","H2S",
                        "S0", "S2O3", "SO4", "Sipart", "DIC", "Alk",
                        "pH", "T", "S", "LimLight", "LimT", "LimN"]
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
# time period (dataset, picname, varnames, nrows, ncols)
z_time.fig_ztime(ds, 'ztime-oxy', oxy_varnames, cfg.icol_0, 2, 3)
#######################################################
# 1 year (dataset, picname, varnames, nrows, ncols)
one_yr.fig_ztime(ds, 'ztime-oxy-1yr', oxy_varnames, cfg.icol_0, 2, 3)

#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
transect.fig_transect(ds, 'transect-2015', oxy_varnames, '2014-10-15 00:00:00', 2, 3)

#---------------------------------------------------------------
# ANIMATION
#---------------------------------------------------------------
# anim_transect.anim_transect(ds, 'frames\Brom', for_poster_transect, '2020-07-10', '2020-07-30', 3, 3)

#---------------------------------------------------------------
# MAPS
#---------------------------------------------------------------
# x-time map (dataset, picname, varnames, z-level, nrows, ncols)
x_time.fig_map(ds, 'xtime-oxy', oxy_varnames, 0, 3, 2)
