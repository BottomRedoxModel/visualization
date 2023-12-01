import my_cmaps as mcm
import colormaps as cmaps
#
#---case of the model:-------------------------------------------------
icase = 2  # 1 = BROM @ Berre;  2 = BROM @ Oslo; 3 = OxyDep @ Laptev
#----------------------------------------------------------------------
plot1year = True #False # to plot changes in short selected period (<= 1 year)
#----------------------------------------------------------------------

if icase == 1:  # BROM @ Berre
# vertical layers numbers for SWI (sed) and upper boundary of BBL (sed2)
    sed  = 17       # SWI
    sed2 = 12      # upper boundary of BBL
# column for baseline (icol_0) and injection (icol_0)
    icol_0 = 0  # baseline column
    icol_C =  0 #26 #2 #22 #18 #5 # 19  ## 22 for 45 column ## 18 for 37 colomns
# z-time (time period) [YYYY-MM-DD]  None: *from start* or *to end*
    t1_ztime = None
    t2_ztime = None
# time period for ONE selected year or a selected SHORT period [YYYY-MM-DD]
    t1_1yr = '2015-01-01'
    t2_1yr = '2016-08-29'
# thickness of BBL and sediments for plotting (in cm)
    bbl_h = 10
#----------------------------------------------------------------------
if icase == 2: # BROM @ Oslo
# vertical layers numbers for SWI (sed) and upper boundary of BBL (sed2)
    sed  = 45       # SWI
    sed2 = 42      # upper boundary of BBL
# column for baseline (icol_0) and injection (icol_0)
    icol_0 = 0  # baseline column
    icol_C = 0 #2 #22 #18 #5 # 19  ## 22 for 45 column ## 18 for 37 colomns
# z-time (time period) [YYYY-MM-DD]  None: *from start* or *to end*
    t1_ztime = None
    t2_ztime = None
# time period for ONE selected year or a selected SHORT period [YYYY-MM-DD]
    t1_1yr = '2023-01-01' #'2012-01-01' for Oslo starting from 2017
    t2_1yr = '2023-12-31' #'2012-05-01' '2013-01-01' #'2012-04-15' #
# thickness of BBL and sediments for plotting (in cm)
    bbl_h = 10
#----------------------------------------------------------------------
yspace = 1
#----------------------------------------------------------------------
# for Animation
# dates to draw transect
ts_transect = ['2016-07-15 00:00:00', '2016-07-20 00:00:00', '2016-07-30 00:00:00',
               '2016-08-10 00:00:00', '2016-08-20 00:00:00', '2016-08-30 00:00:00',
               '2016-10-30 00:00:00', '2016-11-10 00:00:00', '2016-11-15 00:00:00',
               '2016-11-20 00:00:00', '2016-11-25 00:00:00']
               #'2020-11-20 00:00:00', '2020-11-30 00:00:00' ]
#ts_transect = ['2020-07-15 00:00:00', '2020-07-20 00:00:00', '2020-07-30 00:00:00',
#               '2020-08-10 00:00:00', '2020-08-20 00:00:00', '2020-08-30 00:00:00',
#               '2020-10-30 00:00:00', '2020-11-10 00:00:00', '2020-11-15 00:00:00',
#               '2020-11-20 00:00:00', '2020-11-25 00:00:00']
#               #'2020-11-20 00:00:00', '2020-11-30 00:00:00' ]

# animation
tstep = 1  # output steps for animation  (every 3d step, i.e. 3 hours if timestep is 1 hour)
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
