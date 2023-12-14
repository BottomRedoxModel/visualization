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
    currently for CH4 and bubbles
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
    buba[buba < 1e-5] = np.nan
    rise_rate1d=np.nan_to_num(100.*rise_buble1d/buba/86400., nan=0.0) # (mmol/m2/d)/(mmol/m3)=m/d convert to cm/s

    # Create subplots
    fig, axs = plt.subplots(1, 6, figsize=(13.9, 3.1)) # (11.6, 3.1)) figsize=(9.3, 3.1)) figsize=(18, 6)
    # Plot buble1d vs. depth
    axs[0].plot(bubble1d, depth, c='r', lw=2, label='CH_4 in bubbles')
    axs[0].set_xlabel('$\mu M$')
    axs[0].set_ylabel('Depth, m')

    # Plot r_bub1d vs. depth
    axs[1].plot(r_bub1d, depth, c='b', lw=2, label='Bubbles radii')
    axs[1].set_xlabel('$mm$')

    # Plot rise_rate1d vs. depth
    axs[2].plot(rise_rate1d, depth, c='c', lw=2, label='rising rate')
    axs[2].set_xlabel('$cm\ s^{-1}$')

    # Plot bub_dis1d vs. depth
    axs[3].plot(bub_dis1d, depth, c='y', lw=2, label='Dissollution rate')
    axs[3].set_xlabel('$\mu M\ $d^{-1}$')

    # Plot rise_buble1d vs. depth
    axs[4].plot(rise_buble1d, depth, c='g', lw=2, label='Vert. flux')
    axs[4].set_xlabel('$mmol\ m^{-2}d^{-1}$')

    # Plot CH4diss vs. depth
    axs[5].plot(CH4_1d, depth, c='k', lw=2, label='CH$_4$ dissolved')
    axs[5].plot(bubble1d, depth, c='r', lw=2, label='CH$_4$ in bubbles')
    axs[5].set_xlabel('$\mu M$')

    for ax in axs:
        ax.legend() # Add legends
        ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("vert_dist.png",dpi=300)


def depth_timeseries(ds, names, levs, colors):
    '''
    Adapted from EYA
    temporal changes at depth levs
    :param ds:
    :param names: list of variable names
    :param levs: list of corresponding depth levels
    :return:
    '''

    ds = ds.sel(time=slice(cfg.t1_ztime, cfg.t2_ztime))
    xs = ds['time'].values
    zs = ds['z'].values

    fig, axs = plt.subplots(len(names), 1, figsize=(8, len(names)*1.5))

    for i, name in enumerate(names):
        v = ds[name].values[:,levs[i],cfg.icol_C] # mmol/m3
        axs[i].plot(xs, v, c=colors[i], lw=1, label=name)
        axs[i].set_title('%s, z = %.2f m' % (name, zs[levs[i]]))

    plt.tight_layout()
    plt.savefig("time_change.png",dpi=300, bbox_inches='tight')