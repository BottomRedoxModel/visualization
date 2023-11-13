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

for_poster_ztime=['DIC', 'Alk', 'pCO2', 'pH', 'CaCO3', 'Om_Ar','CH4',] + ['Bubble','r_bub']
for_poster_transect=['DIC', 'Alk', 'pCO2', 'pH', 'CaCO3', 'Om_Ar','CH4',] + ['Bubble','Oxy']

#---------------------------------------------------------------
# VERTICAL DISTRIBUTIONS
#---------------------------------------------------------------


#---------------------------------------------------------------
# TEMPORAL VARIABILITY OF VERT. DISTRIBUTIONS
#---------------------------------------------------------------

# 1 year (dataset, picname, varnames, nrows, ncols)
one_yr.fig_ztime(ds, '1yr-oxy', one_yr_varnames, cfg.icol_C, 3, 3)
# icol = 0
#one_yr.fig_ztime(ds, '1yr-carb', carb_varnames, cfg.icol_0, 3, 3)
# # icol = C
# one_yr.fig_ztime(ds, '1yr-carb', carb_varnames, cfg.icol_C, 3, 3)

# time period (dataset, picname, varnames, nrows, ncols)
# for icol = 0
#¤z_time.fig_ztime(ds, 'n45col/ztime-oxy0', oxy_varnames, cfg.icol_0, 3, 2)
#¤z_time.fig_ztime(ds, 'n45col/ztime-carb0', carb_varnames, cfg.icol_0, 3, 3)
#¤z_time.fig_ztime(ds, 'n45col/ztime-bubbl0', bubbl_varnames, cfg.icol_0, 3, 3)
z_time.fig_ztime(ds, 'ztime-oxy0', oxy_varnames, cfg.icol_0, 3, 2)
z_time.fig_ztime(ds, 'ztime-carb0', carb_varnames, cfg.icol_0, 3, 3)
z_time.fig_ztime(ds, 'ztime-bubbl0', bubbl_varnames, cfg.icol_0, 3, 3)
# for icol = C
### z_time.fig_ztime(ds, '45col/ztime-poster', for_poster_ztime, cfg.icol_C, 3, 3)
z_time.fig_ztime(ds, 'ztime-oxy', oxy_varnames, cfg.icol_C, 3, 2)
z_time.fig_ztime(ds, 'ztime-carb', carb_varnames, cfg.icol_C, 3, 3)
z_time.fig_ztime(ds, 'ztime-bubbl', bubbl_varnames, cfg.icol_C, 3, 3)

#---------------------------------------------------------------
#TRANSECTS
#---------------------------------------------------------------
# transect snapshot (dataset, picname, varnames, day, nrows, ncols)
transect.fig_transect(ds, 'transect-2015', for_poster_transect, '2014-10-15 00:00:00', 3, 3)
transect.fig_transect(ds, 'transect-2017', for_poster_transect, '2018-10-15 00:00:00', 3, 3)
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
x_time.fig_map(ds, 'xtime-oxy', oxy_varnames, cfg.sed, 3, 2)
x_time.fig_map(ds, 'xtime-carb', carb_varnames, cfg.sed, 3, 3)
x_time.fig_map(ds, 'xtime-carb0', carb_varnames, 0, 3, 3)

#---------------------------------------------------------------
# vertical profiles at time t4vert
#---------------------------------------------------------------
t4vert=22222 #22222 #222 #888
CH4_1d=ds['CH4'].values[t4vert,:50,cfg.icol_C] # mmol/m3
bubble1d=ds['Bubble'].values[t4vert,:50,cfg.icol_C] # mmol/m3
r_bub1d=1000*ds['r_bub'].values[t4vert,:50,cfg.icol_C]  # m convert to mm
rise_buble1d=ds['sink:Bubble'].values[t4vert,:50,cfg.icol_C] # mmol/m2/s convert to mmol/m2/d
bub_dis1d=ds['Bubble_dissolution'].values[t4vert,:50,cfg.icol_C] # mmol/m3/d
depth=ds['z'].values[:50]
buba = bubble1d.copy()
buba[buba < 0.000001] = np.nan
rise_rate1d=np.nan_to_num(100.*rise_buble1d/buba/86400., nan=0.0) # (mmol/m2/d)/(mmol/m3)=m/d convert to cm/s

#rise_rate1d(:)=0.
# for i in range(0,50):
# ##    print(i, rise_rate1d[i], rise_buble1d[i], bubble1d[i])
#     if bubble1d[i] > 0.000001:
#         rise_rate1d[i]=100.*rise_buble1d[i]/bubble1d[i]/86400. # (mmol/m2/d)/(mmol/m3)=m/d convert to cm/s
#     if rise_rate1d[i] > 1000.:
#         rise_rate1d[i]=0.

# Create subplots
fig, axs = plt.subplots(1, 6, figsize=(13.9, 3.1)) # (11.6, 3.1)) figsize=(9.3, 3.1)) figsize=(18, 6)
# Plot buble1d vs. depth
axs[0].plot(bubble1d, depth, c='r', lw=2, label='CH_4 in bubbles')
axs[0].set_xlabel('$\mu M$')
axs[0].set_ylabel('Depth, m')
axs[0].invert_yaxis()  # Invert the y-axis to have depth as negative values
# Plot r_bub1d vs. depth
axs[1].plot(r_bub1d, depth, c='b', lw=2, label='Bubbles radii')
axs[1].set_xlabel('$mm$')
axs[1].invert_yaxis()
# Plot rise_rate1d vs. depth
axs[2].plot(rise_rate1d, depth, c='c', lw=2, label='rising rate')
axs[2].set_xlabel('$cm$ $s^-$$^1$')
axs[2].invert_yaxis()
# Plot bub_dis1d vs. depth
axs[3].plot(bub_dis1d, depth, c='y', lw=2, label='Dissollution rate')
axs[3].set_xlabel('$\mu M$ $d^-$$^1$')
axs[3].invert_yaxis()
# Plot rise_buble1d vs. depth
axs[4].plot(rise_buble1d, depth, c='g', lw=2, label='Vert. flux')
axs[4].set_xlabel('$ mmol$ $m^-$$^2$$d^-$$^1$')
axs[4].invert_yaxis()
# Plot CH4diss vs. depth
axs[5].plot(CH4_1d, depth, c='k', lw=2, label='CH$_4$ dissolved')
axs[5].plot(bubble1d, depth, c='r', lw=2, label='CH$_4$ in bubbles')
axs[5].set_xlabel('$\mu M$')
axs[5].invert_yaxis()  # Invert the y-axis to have depth as negative values
for ax in axs:
    ax.legend() # Add legends
plt.tight_layout()
plt.savefig("vert_dist.png",dpi=300) #plt.show() # Show the plot


#---------------------------------------------------------------
# temporal changes at depth depth4tc
#---------------------------------------------------------------
depth4tc=5
bubble_tc=ds['Bubble'].values[:,depth4tc,cfg.icol_C] # mmol/m3
CH4_tc=ds['CH4'].values[:,depth4tc,cfg.icol_C] # mmol/m3
DIC_tc=ds['DIC'].values[:,depth4tc,cfg.icol_C] # mmol/m3
pH_tc = ds['pH'].values[:,depth4tc,cfg.icol_C] # mmol/m3
Oxy_tc=ds['Oxy'].values[:,depth4tc,cfg.icol_C] # mmol/m3
Om_Ar_tc=ds['Om_Ar'].values[:,depth4tc,cfg.icol_C] # mmol/m3

xs = ds.sel(time=slice(cfg.t1_ztime, cfg.t2_ztime))['time'].values
# Create subplots
fig, axs = plt.subplots(6, 1, figsize=(8, 9)) # (11.6, 3.1)) figsize=(9.3, 3.1)) figsize=(18, 6)
# Plot buble1d vs. depth
axs[0].plot(xs, bubble_tc, c='r', lw=1, label='CH4 in bubbles')
axs[0].set_ylabel('$CH_4$ $in$ $ bubbles,$ $\mu M$')
axs[1].plot(xs, CH4_tc, c='k', lw=1, label='CH4 dissolved')
axs[1].set_ylabel('$CH_4$ $ dissoled,$ $\mu M$')
axs[2].plot(xs, DIC_tc, c='b', lw=1, label='DIC')
axs[2].set_ylabel('$DIC,$ $\mu M$')
axs[3].plot(xs, pH_tc, c='c', lw=1, label='pH')
axs[3].set_ylabel('pH')
axs[4].plot(xs, Oxy_tc, c='g', lw=1, label='Oxy')
axs[4].set_ylabel('$Oxy,$ $\mu M$')
axs[5].plot(xs, Om_Ar_tc, c='y', lw=1, label='Aragonite Saturation')
axs[5].set_ylabel('$\Omega$  $aragonite$')

plt.tight_layout()
plt.savefig("time_change.png",dpi=300) #plt.show() # Show the plot

#print (Depth)
## Create subplots
#fig, axs = plt.subplots(3, sharex=True, figsize=(8, 10))
#
## Oxy1d vs Depth
#axs[0].plot(depth[:len(Oxy1d)], Oxy1d, marker='o', linestyle='-')
#axs[0].set_ylabel('Oxy1d')
#axs[0].set_title('Distribution of Oxygen, Bubble, and Rise vs. Depth')
#
## Bubble vs Depth
#axs[1].plot(depth[:len(buble1d)], buble1d, marker='o', linestyle='-')
#axs[1].set_ylabel('Bubble')#
#
## Rise vs Depth
#axs[2].plot(depth[:len(rise_buble1d)], rise_buble1d, marker='o', linestyle='-')
#axs[2].set_xlabel('Depth')
#axs[2].set_ylabel('rise_buble1d')

# Display the plot
#plt.tight_layout()
# Create a new figure

