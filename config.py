import my_cmaps as mcm
import colormaps as cmaps


site = 1 #case 1=Norskehavet, 2=Black Sea; 3=Oslofjord
if site==1:
# vertical layers numbers for SWI (sed) and upper boundary of BBL (sed2)
    sed  = 45 #45       # SWI
    sed2 = 41 #42      # upper boundary of BBL
# time period for ONE selected year or a selected SHORT period [YYYY-MM-DD]
    t1_1yr = '2020-01-01'
    t2_1yr = '2021-01-01'
# thickness of BBL and sediments for plotting (in cm)
    bbl_h = 20 #10

if site==2:
# vertical layers numbers for SWI (sed) and upper boundary of BBL (sed2)
    sed  = 60 #45       # SWI for Black Sea
    sed2 = 59 #42      # upper boundary of BBL for Black Sea
# time period for ONE selected year or a selected SHORT period [YYYY-MM-DD]
    t1_1yr = '2027-01-01'# '2020-01-01'
    t2_1yr = '2027-12-31' #'2021-01-01'
# thickness of BBL and sediments for plotting (in cm)
    bbl_h = 10 #10

# column for baseline (icol_0) and injection (icol_C)
icol_0 = 0  # baseline column
icol_C = 0

# z-time (time period) [YYYY-MM-DD]  None: *from start* or *to end*
t1_ztime = None
t2_ztime = None
yspace = 5


plot_1year = True #True #False # to plot changes in short selected period (<= 1 year)
plot_depth_timeser = False # to plot temporal changes at selected depths

# dates to draw transect
ts_transect = ['2016-07-15 00:00:00', '2016-07-20 00:00:00', '2016-07-30 00:00:00',
               '2016-08-10 00:00:00', '2016-08-20 00:00:00', '2016-08-30 00:00:00',
               '2016-10-30 00:00:00', '2016-11-10 00:00:00', '2016-11-15 00:00:00',
               '2016-11-20 00:00:00', '2016-11-25 00:00:00']

transect_lev = 0  # for 1D plot

# animation
anim_tstep = 1  # output steps for animation  (every 3d step, i.e. 3 hours if timestep is 1 hour)

# model vs observations
plot_obs_n_mod =False # to plot changes in short selected period (<= 1 year)
t1_mod_vs_obs = None # '2020-01-01'
t2_mod_vs_obs = None  # '2021-01-01'
mod_tstep = 24  # in model steps

# profiles (EYA version)
tprof = 22222  #22222 #222 #888


# concentrations profiles with sediments (MATWEY)
pidays = [365,]  #6935,6966,6995,7026,7056,7086,7117,7147,7178,7219,7249,7280]
picol = 0
plot_obs = False
hor_ax = 'z'  # Vertical axis. Only z or dens.
#----------------------------------------------------------------------

units_dict = {'$°C$': ['T'],
              '$psu$': ['S'],
              '$tot$': ['pH'],
              '$ppm$': ['pCO2'],
              '$m$': ['r_bub'],
              '$nd$': ['LimLight','LimT','LimN','Om_Ar'],
              '$mmol$ $m^-$$^2$$d^-$$^1$': ['sink:bubble','fick:bubble','fick:CH4'],
              '$\mu M$ $d^-$$^1$': ['CaCO3_form','CaCO3_diss','DOM_decay_ox','DOM_decay_denitr',
                                    'POM_decay_ox'], #,'POM_decay_denitr'],
              '$d^-$$^1$': ['GrowthPhy','GrazPhy','GrazPOM'],
              # add new units here
               }

cmap_dict = {'MP_free': mcm.mp, 'MP_biof': mcm.mp,
             'MP_het': mcm.mp, 'MP_det': mcm.mp,
             'MP_TOT': mcm.mp, 'MP_TOT_items': mcm.mp,
             'Oxy': mcm.oxy, 'Phy': mcm.phy, 'Het': mcm.het,
             'POM': mcm.pom, 'DOM': mcm.dom, 'NUT': cmaps.amp,
             'T': 'RdYlBu_r', 'S': cmaps.haline,
             'pH': cmaps.bilbao, 'pCO2': cmaps.lapaz_r,
             'Om_Ar': cmaps.savanna_r, 'DIC': cmaps.tokyo_r,
             'Alk': cmaps.buda_r, 'CO3': cmaps.turku_r,
}
