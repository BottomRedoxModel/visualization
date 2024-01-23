# Filename: profile_plotter.py
import xarray as xr
import matplotlib.pyplot as plt
import gsw
import pandas as pd
import config as cfg

icol = cfg.picol
hor_ax = cfg.hor_ax  # Horizontal axis. Only z or dens.
sed = cfg.sed
sed2 = cfg.sed2
plot_obs = cfg.plot_obs
bbl_h = cfg.bbl_h

obs_files = {}

# drawn concentrations
var = [
        ['T', 'S', 'O2'],
        ['H2S', 'S2O3', 'S0'],
        ['NO2', 'NO3', 'NH4'],
        ['Mn4', 'Mn3', 'Mn2'],
        ['Fe3', 'Fe2'],

        ['Phy', 'Het'],
        ['Baae', 'Bhae', 'Baan', 'Bhan'],
        ['DOML', 'DOMR', 'POML', 'POMR'],
        ['PO4', 'Si', 'CH4'],
        ['pH', 'Alk', 'DIC']
    ]

# drawn concentration colors
colors_vax = [
        ['#377eb8', '#e41a1c', '#4daf4a'],
        ['#984ea3', '#a65628', '#e6ab02'],
        ['#377eb8', '#e41a1c', '#f781bf'],
        ['#377eb8', '#4daf4a', '#984ea3'],
        ['#a65628', '#f781bf'],

        ['#4daf4a', '#ff7f00'],
        ['#377eb8', '#4daf4a', '#984ea3', '#e6ab02'],
        ['#a65628', '#f781bf', '#e41a1c', '#377eb8'],
        ['#4daf4a', '#984ea3', '#ff7f00'],
        ['#e6ab02', '#a65628', '#f781bf'],
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

def load_obs_data(plot_obs, obs_files):
    if plot_obs:
        obs_data = {key: pd.read_excel(*value) for key, value in obs_files.items()}
        return obs_data
    return None

def get_depth(ds, hor_ax, sed, iday):
    if hor_ax == 'z':
        return ds['z']
    elif hor_ax == 'dens':
        P = ds['z'] - 10.1325
        SA = gsw.SA_from_SP(ds['S'].isel(time=iday), P, 42, 30.5)
        CT = gsw.CT_from_t(SA, ds['T'].isel(time=iday), P)
        return gsw.density.sigma0(SA, CT)
    else:
        raise ValueError('Variable hor_ax is incorrect. Check it please.')


def configure_ax(axn, av, ac, shift):
    # Configuration code for axn (axis)
    # Set labels, limits, etc.
    axn.spines['top'].set_position(('outward', shift))

    axn.tick_params(axis='x', labelcolor=ac, labelsize=13)
    axn.set_xlabel(av, color=ac, fontsize=13)


def plot_profile(ax, ds, vax, colors, depth, plot_type, iday, obs_data):

    ax.tick_params(bottom=False, labelbottom=False)
    shift = 0
    for av, ac in zip(vax, colors):
        var = ds[av][iday, :, icol]
        axn = ax.twiny()
        if plot_type == 'water':
            axn.plot(var, depth, zorder=5, color=ac, lw=1.5)
        elif plot_type == 'sediment':
            axn.plot(var[sed2:], depth[sed2:], zorder=5, color=ac, lw=1.5)

        # Add observations if needed
        if obs_data and av in variable_mapping:
            obs_name = variable_mapping[av]
            obsv = obs_data[f'{plot_type}_{av}'][[obs_name, 'depth']]
            axn.scatter(obsv[obs_name], obsv['depth'], c=ac, s=10, marker='x', label=av)

        configure_ax(axn, av, ac, shift)
        shift += 41

    # we do it only for the last axn
    if plot_type == 'water':
        axn.axhspan(-0.5, depth.max(), color='dodgerblue', alpha=0.2)
        axn.set_ylim(top=0, bottom=depth.max())
    elif plot_type == 'sediment':
        axn.axhspan(bbl_h, 0, color='sandybrown', alpha=0.3)
        axn.axhspan(0, -bbl_h, color='dodgerblue', alpha=0.2)
        axn.set_ylim(top=-bbl_h, bottom=bbl_h)


def conc_profiles(ds, iday):
    depth = get_depth(ds, hor_ax, sed, iday)
    depth_sed = ((depth - depth[sed]) * 100)

    fig, axs = plt.subplots(2, 10, figsize=(25, 10), gridspec_kw={'hspace': 0.8, 'wspace': 0.32})
    obs_data = load_obs_data(plot_obs, obs_files)

    for i, (vax, colors) in enumerate(zip(var, colors_vax)):
        plot_profile(axs[0,i], ds, vax, colors, depth, 'water', iday, obs_data)
        plot_profile(axs[1, i], ds, vax, colors, depth_sed, 'sediment', iday, obs_data)

    date = ds['time'][iday].values
    fig.suptitle(date.astype(str)[:10], y=1.05, fontweight='bold')
    plt.savefig('prof_%i.png' % iday, dpi=400, bbox_inches='tight')
