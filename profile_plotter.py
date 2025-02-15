# Filename: profile_plotter.py
import xarray as xr
import matplotlib.pyplot as plt
import gsw
import pandas as pd
# import config as cfg
import utils

cfg = utils.load_config('config.json')

icol = cfg["profile_plotter"]["icol"]
vert_ax = cfg["profile_plotter"]["vertical_ax"] # Horizontal axis. Only z or dens.
plot_obs = cfg["profile_plotter"]["plot_observations"]

sed = cfg["case_specific"]["sed"]
sed2 = cfg["case_specific"]["sed2"]
bbl_h = cfg["case_specific"]["bbl_h"]


obs_files = {}

# drawn concentrations
var = cfg["profile_plotter"]['var']

# drawn concentration colors
colors_vax = cfg["profile_plotter"]['colors_vax']

# {model: obs}
model_obs_mapping = cfg["profile_plotter"]['model_obs_mapping']

def load_obs_data(plot_obs, obs_files):
    if plot_obs:
        obs_data = {key: pd.read_excel(*value) for key, value in obs_files.items()}
        return obs_data
    return None

def get_depth(ds, vert_ax, sed, iday):
    if vert_ax == 'z':
        return ds['z']
    elif vert_ax == 'dens':
        P = ds['z'] - 10.1325
        SA = gsw.SA_from_SP(ds['S'].isel(time=iday), P, 42, 30.5)
        CT = gsw.CT_from_t(SA, ds['T'].isel(time=iday), P)
        return gsw.density.sigma0(SA, CT)
    else:
        raise ValueError('Variable vert_ax is incorrect. Check it please.')


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
        if obs_data and av in model_obs_mapping:
            obs_name = model_obs_mapping[av]
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
    depth = get_depth(ds, vert_ax, sed, iday)
    depth_sed = ((depth - depth[sed]) * 100)

    nvar = len(var)
    fig, axs = plt.subplots(2, nvar,
                            figsize=(nvar*2.5, 10),
                            gridspec_kw={'hspace': 0.8, 'wspace': 0.32})
    obs_data = load_obs_data(plot_obs, obs_files)

    for i, (vax, colors) in enumerate(zip(var, colors_vax)):
        plot_profile(axs[0,i], ds, vax, colors, depth, 'water', iday, obs_data)
        plot_profile(axs[1, i], ds, vax, colors, depth_sed, 'sediment', iday, obs_data)

    date = ds['time'][iday].values
    fig.suptitle(date.astype(str)[:10], y=1.05, fontweight='bold')
    plt.savefig('prof_%i.png' % iday, dpi=400, bbox_inches='tight')
