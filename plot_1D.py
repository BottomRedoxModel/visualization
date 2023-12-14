import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import os
import pandas as pd
import numpy as np
import config as cfg
import utils


def profiles(ds):
    '''
    Adapted from EYA
    vertical profiles at time t4vert
    :param ds:
    :return:
    '''

    CH4_1d=ds['CH4'].values[cfg.tprof,:50,cfg.icol_C] # mmol/m3
    bubble1d=ds['Bubble'].values[cfg.tprof,:50,cfg.icol_C] # mmol/m3
    r_bub1d=1000*ds['r_bub'].values[cfg.tprof,:50,cfg.icol_C]  # m convert to mm
    rise_buble1d=ds['sink:Bubble'].values[cfg.tprof,:50,cfg.icol_C] # mmol/m2/s convert to mmol/m2/d
    bub_dis1d=ds['Bubble_dissolution'].values[cfg.tprof,:50,cfg.icol_C] # mmol/m3/d
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


def depth_timeseries(ds):
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