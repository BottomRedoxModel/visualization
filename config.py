# import my_cmaps as mcm
# import colormaps as cmaps
import utils

fname = utils.get_fname('Model output')

# sets of variables to plot
oxy_varnames = ['Oxy', 'Phy', 'Het', 'POM', 'DOM', 'NUT']
carb_varnames = ['DIC', 'Alk', 'CaCO3',  'pH',  'Om_Ar', 'CaCO3_form', 'pCO2', 'CO3', 'CaCO3_diss']
brom_state_variables = ["Phy", "Het", "POML", "POMR", "DOML", "DOMR",
                        "O2", "NH4", "NO2", "NO3", "PO4", "Si",
                        "Baae", "Bhae", "Baan", "Bhan", "Fe2", "Fe3",
                        "FeS", "FeCO3", "FeS2", "Fe3PO42", "PO4_Fe3", "Mn2",
                        "Mn3", "Mn4", "MnS", "MnCO3", "PO4_Mn3", "H2S",
                        "S0", "S2O3", "SO4", "Sipart", "DIC", "Alk",
                        "pH", "T", "S", "LimLight", "LimT", "LimN"]

# what we will actually plot
varnames = oxy_varnames

# Profiles properties
iday = 5688
hor_ax = 'z'  # Horizontal axis. Only z or dens.


# drawn concentration colors
# colors_vax1 = [['#377eb8', '#e41a1c', '#4daf4a'],
#                ['#984ea3', '#a65628', '#e6ab02'],
#                ['#377eb8', '#e41a1c', '#f781bf'],
#                ['#377eb8', '#4daf4a', '#984ea3'],
#                ['#a65628', '#f781bf']]
# colors_vax2 = [['#4daf4a', '#ff7f00'],
#                ['#377eb8', '#4daf4a', '#984ea3', '#e6ab02'],
#                ['#a65628', '#f781bf', '#e41a1c', '#377eb8'],
#                ['#4daf4a', '#984ea3', '#ff7f00'],
#                ['#e6ab02', '#a65628', '#f781bf']]

variable_mapping = {"NO3": "NO3 uM",
                    "NO2": "NO2 uM",
                    "NH4": "NH4 uM",
                    "PO4": "PO4 uM",
                    "Si": "SI uM",
                    "S": "Salinity",
                    "pH": "pH",
                    "Mn2": "Mn uM",
                    "Fe2": "Fe uM",
                    "H2S": "H2S uM",
                    "SO4": "SO4 uM",
                    "DIC": "tCO2 uM",
                    "O2": "O2 (µM)",
                    "T": "T"}

# TODO: automaticaly identify sed and sed2 based on dz
# vertical layers numbers for SWI (sed) and upper boundary of BBL (sed2)
sed = 45       # SWI
sed2 = 42       # upper boundary of BBL

# column for baseline (icol_0) and injection (icol_C)
icol_0 = 0  # baseline column
icol_C = 0
# thickness of BBL and sediments for plotting (in cm)
bbl_h = 10

# z-time (time period) [YYYY-MM-DD]  None: *from start* or *to end*
t1_ztime = None
t2_ztime = None
yspace = 5

# time period for ONE selected year or a selected SHORT period [YYYY-MM-DD]
t1_1yr = '2020-01-01'
t2_1yr = '2021-01-01'

# dates to draw transect
ts_transect = ['2016-07-15 00:00:00', '2016-07-20 00:00:00', '2016-07-30 00:00:00',
               '2016-08-10 00:00:00', '2016-08-20 00:00:00', '2016-08-30 00:00:00',
               '2016-10-30 00:00:00', '2016-11-10 00:00:00', '2016-11-15 00:00:00',
               '2016-11-20 00:00:00', '2016-11-25 00:00:00']

# animation
anim_tstep = 1  # output steps for animation  (every 3d step, i.e. 3 hours if timestep is 1 hour)

# model vs observations
t1_mod_vs_obs = None # '2020-01-01'
t2_mod_vs_obs = None  # '2021-01-01'
mod_tstep = 24  # in model steps
#----------------------------------------------------------------------

units_dict = {'$°C$': ['T'],
              '$psu$': ['S'],
              '$tot$': ['pH'],
              '$ppm$': ['pCO2'],
              '$m$': ['r_bub'],
              '$nd$': ['LimLight', 'LimT', 'LimN', 'Om_Ar'],
              '$mmol$ $m^-$$^2$$d^-$$^1$': ['sink:bubble', 'fick:bubble', 'fick:CH4'],
              '$\mu M$ $d^-$$^1$': ['CaCO3_form', 'CaCO3_diss', 'DOM_decay_ox', 'DOM_decay_denitr',
                                    'POM_decay_ox'],  # ,'POM_decay_denitr'],
              '$d^-$$^1$': ['GrowthPhy', 'GrazPhy', 'GrazPOM'],
              # add new units here
               }

# cmap_dict = {'MP_free': mcm.mp, 'MP_biof': mcm.mp,
#              'MP_het': mcm.mp, 'MP_det': mcm.mp,
#              'MP_TOT': mcm.mp, 'MP_TOT_items': mcm.mp,
#              'Oxy': mcm.oxy, 'Phy': mcm.phy, 'Het': mcm.het,
#              'POM': mcm.pom, 'DOM': mcm.dom, 'NUT': cmaps.amp,
#              'T': 'RdYlBu_r', 'S': cmaps.haline,
#              'pH': cmaps.bilbao, 'pCO2': cmaps.lapaz_r,
#              'Om_Ar': cmaps.savanna_r, 'DIC': cmaps.tokyo_r,
#              'Alk': cmaps.buda_r, 'CO3': cmaps.turku_r}
