import my_cmaps as mcm
import colormaps as cmaps

# Test commit
# SWI
sed = 30       # SWI
sed2 = 12      # upper boundary of SWI

# column to select
icol_0 = 0
icol_C = 26 #2 #22 #18 #5 # 19  ## 22 for 45 column ## 18 for 37 colomns

# z-time (time period)
# 'YYYY-MM-DD'
# None: *from start* or *to end*
t1_ztime = None
t2_ztime = None
yspace = 1

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

# 1 year parameters for ONE selected year or a selected SHORT period
# 'YYYY-MM-DD'
t1_1yr = '2010-08-01T00:00:00'
t2_1yr = '2010-02-01T00:00:00'

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
