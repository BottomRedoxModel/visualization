import xarray as xr
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import os
import gsw
import pandas as pd
import config as cfg

plt.rcParams["figure.facecolor"] = 'w'

iday = 5688
hor_ax = 'z'  # Horizontal axis. Only z or dens.
sed = cfg.sed
plot_obs = False

# drawn concentrations
vax1 = [['T', 'S', 'O2'],
       ['H2S', 'S2O3', 'S0'],
       ['NO2', 'NO3', 'NH4'],
       ['Mn4', 'Mn3', 'Mn2'],
       ['Fe3', 'Fe2'],]
vax2 = [['Phy', 'Het'],
       ['Baae', 'Bhae', 'Baan', 'Bhan'],
       ['DOML', 'DOMR', 'POML', 'POMR'],
       ['PO4', 'Si', 'CH4'],
       ['pH', 'Alk', 'DIC']
       ]

# drawn concentration colors
colors_vax1 = [['#377eb8', '#e41a1c', '#4daf4a'],
              ['#984ea3', '#a65628', '#e6ab02'],
              ['#377eb8', '#e41a1c', '#f781bf'],
              ['#377eb8', '#4daf4a', '#984ea3'],
              ['#a65628', '#f781bf'],]
colors_vax2 = [['#4daf4a', '#ff7f00'],
              ['#377eb8', '#4daf4a', '#984ea3', '#e6ab02'],
              ['#a65628', '#f781bf', '#e41a1c', '#377eb8'],
              ['#4daf4a', '#984ea3', '#ff7f00'],
              ['#e6ab02', '#a65628', '#f781bf']
              ]

# {model: obs}
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

if plot_obs:
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

            if plot_type == 'water':
                axn.set_ylim(6, 0)  # ADJUST DEPTHS IF YOU CHANGE MODEL POINT
            elif plot_type == 'sediment':
                axn.set_ylim(top=-10, bottom=10)

            if plot_obs:
                if av in variable_mapping.keys():
                    obsname = variable_mapping[av]
                if plot_type == 'water':

                    if av in ['O2', 'T']:
                        obsv = obs_o2_wat[[obsname, 'depth']]
                    elif av in variable_mapping.keys():
                        obsv = obs_wat[[obsname, 'depth']]

                elif plot_type == 'sediment':

                    if av in ['O2', 'T']:
                        obsv = obs_o2_sed[[obsname, 'depth']]
                    elif av in variable_mapping.keys():
                        obsv = obs_sed[[obsname, 'depth']]

                # Observations
                if av in variable_mapping.keys():
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
            axn.axhspan(6,-0.5, color='dodgerblue', alpha=0.2)
        elif plot_type == 'sediment':
            axn.axhspan(15,0, color='sandybrown', alpha=0.3)
            axn.axhspan(0,-10, color='dodgerblue', alpha=0.2)


def conc_profiles(ds, vax, colors_vax, fname):

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
    plot_ax(axs[0,:], vax, colors_vax, ds, depth, 'water')
    plot_ax(axs[1,:], vax, colors_vax, ds, depth_sed, 'sediment')

    plt.savefig(fname + '.png', dpi=400, bbox_inches='tight')

# plot_fig(vax1, colors_vax1, 'set1')
conc_profiles(vax2, colors_vax2, 'set2')
