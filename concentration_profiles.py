import xarray as xr
import matplotlib.pyplot as plt
import os
import gsw
import pandas as pd
import config as cfg
import re

plt.rcParams["figure.facecolor"] = 'w'

iday = cfg.iday
hor_ax = cfg.hor_ax
sed = 17

# {model: obs}


obs_wat = pd.read_excel('PI_aug15.xlsx', sheet_name='water')
obs_sed = pd.read_excel('PI_aug15.xlsx', sheet_name='sediment')
obs_o2_wat = pd.read_excel('PI_aug15_O2_T_Tur_Chla.xlsx', sheet_name='water')
obs_o2_sed = pd.read_excel('PI_aug15_O2_T_Tur_Chla.xlsx', sheet_name='sediment')


def plot_ax(axs, vax, colors_vax, ds, depth, plot_type):
    for i, ax in enumerate(axs):
        ax_vars, ax_colors = vax[i], colors_vax[i]
        ax.invert_yaxis()
        shift = 0
        ax.grid(which='major', axis='y', linestyle='--', color='0.5')
        if i not in [0, 5]:
            ax.tick_params(left=False, labelleft=False)
        else:
            if hor_ax == 'z':
                ax.set_ylabel('Depth, m', fontsize=13)
            else:
                ax.set_ylabel('Sigma', fontsize=13)
            ax.tick_params(axis='y', labelsize=13)

        for av, ac in zip(ax_vars, ax_colors):
            print(av)
            var = ds[av][iday, :, 0]
            axn = ax.twiny()
            axn.plot(var, depth, zorder=5, color=ac, lw=1.5)

            if av in cfg.variable_mapping.keys():
                obsname = cfg.variable_mapping[av]
            if plot_type == 'water':
                axn.set_ylim(6, 0)  # ADJUST DEPTHS IF YOU CHANGE MODEL POINT

                if av in ['O2', 'T']:
                    obsv = obs_o2_wat[[obsname, 'depth']]
                elif av in cfg.variable_mapping.keys():
                    obsv = obs_wat[[obsname, 'depth']]

            elif plot_type == 'sediment':
                axn.set_ylim(top=-10, bottom=10)

                if av in ['O2', 'T']:
                    obsv = obs_o2_sed[[obsname, 'depth']]
                elif av in cfg.variable_mapping.keys():
                    obsv = obs_sed[[obsname, 'depth']]

            # Observations
            if av in cfg.variable_mapping.keys():
                axn.scatter(obsv[obsname], obsv['depth'], c=ac, s=10, marker='x', label=av)

            axn.spines['top'].set_position(('outward', shift))
            shift += 41
            axn.tick_params(axis='x', labelcolor=ac, labelsize=13)
            ax.tick_params(bottom=False, labelbottom=False)
            if av == 'T':
                axn.set_xlabel(r'T, $^{\circ}$C', color=ac, fontsize=13)
            elif av == 'S':
                axn.set_xlabel('S, PSU', color=ac, fontsize=13)
            elif av == 'pH':
                axn.set_xlabel('pH', color=ac, fontsize=13)
            elif av == 'pCO2':
                axn.set_xlabel('pCO2, ppm', color=ac, fontsize=13)
            else:
                axn.set_xlabel(av+r', $\mu$M', color=ac, fontsize=13)

        if plot_type == 'water':
            axn.axhspan(6, -0.5, color='dodgerblue', alpha=0.2)
        elif plot_type == 'sediment':
            axn.axhspan(15, 0, color='sandybrown', alpha=0.3)
            axn.axhspan(0, -10, color='dodgerblue', alpha=0.2)


def plot_fig(ds, vax, colors_vax):

    if hor_ax == 'z':
        depth = ds['z']  # depth
    elif hor_ax == 'dens':
        P = ds['z'] - 10.1325  # Sea pressure in dbar
        SA = gsw.SA_from_SP(ds['S'].isel(time=iday),  # Absolute salinity
                            P, 42, 30.5)
        CT = gsw.CT_from_t(SA, ds['T'].isel(time=iday), P)  # Conservative temperature (ITS-90)
        depth = gsw.density.sigma0(SA, CT)  # potential density anomaly
    else:
        print('Variable hor_ax is incorrect. Check it, please.')

    depth_sed = ((depth - depth[sed]) * 100)

    fig, axs = plt.subplots(2, 5, figsize=(15, 15), gridspec_kw={'hspace': 0.6, 'wspace': 0.15})
    plot_ax(axs[0, :], vax, colors_vax, ds, depth, 'water')
    plot_ax(axs[1, :], vax, colors_vax, ds, depth_sed, 'sediment')

    plt.savefig(cfg.fname + '.png', dpi=400, bbox_inches='tight')

