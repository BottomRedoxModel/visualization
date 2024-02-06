import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
import matplotlib.dates as mdates
import config as cfg
import grid_maker as gm
import utils
import my_cmaps as mcm

cfg = utils.load_config('config.json')

sed = cfg["case_specific"]["sed"]
sed2 = cfg["case_specific"]["sed2"]
bbl_h = cfg["case_specific"]["bbl_h"]
t1 = cfg["z-time"]["t1"]
t2 = cfg["z-time"]["t2"]
yspace = cfg["z-time"]["yspace"]


def plot_param(ds, name, x, y, y_sed, axis,axis_cb,axis_sed,axis_cb_sed):

    var = ds[name].values
    print(var.shape)
    levels = np.linspace(np.min(var[:,:sed2]), np.max(var[:,:sed2]), 30)
    sed_levels = np.linspace(np.min(var[:,sed2:]), np.max(var[:,sed2:]), 30)
    if all(lev == levels[0] for lev in levels):
        levels = np.linspace(levels[0], levels[0]+0.1, 30)
    if all(lev == sed_levels[0] for lev in sed_levels):
        sed_levels = np.linspace(sed_levels[0], sed_levels[0]+0.1, 30)

    X,Y = np.meshgrid(x,y[:sed2])
    X_sed,Y_sed = np.meshgrid(x,y_sed[sed2:])
    if name in mcm.cmap_dict.keys():
        cmap = mcm.cmap_dict[name]
    else:
        cmap = 'turbo'

    if var[:, sed2:].shape[1] == len(Y_sed):
        CS_1_sed = axis_sed.contourf(X_sed,Y_sed, var[:,sed2:].T, levels = sed_levels, cmap = cmap)
    else:
        CS_1_sed = axis_sed.contourf(X_sed, Y_sed, var[:, sed2+1:].T, levels=sed_levels, cmap=cmap)

    # TODO: fix it
    if name == 'Oxy':
        cmap = 'plasma'
    CS_1 = axis.contourf(X, Y, var[:, :sed2].T, levels=levels, cmap=cmap)

    locw = ticker.MaxNLocator(nbins=2, steps=[2, 3, 5, 10])

    cb = plt.colorbar(CS_1,cax = axis_cb)
    cb.ax.yaxis.set_major_locator(locw)

    cb_sed = plt.colorbar(CS_1_sed,cax = axis_cb_sed)
    locs = ticker.MaxNLocator(nbins=2, steps=[2, 3, 5, 10])
    cb_sed.ax.yaxis.set_major_locator(locs)

    axis.set_ylim(np.max(y[:sed2]),0)
    axis_sed.set_ylim(bbl_h,-bbl_h)

    axis_sed.axhline(0,linestyle = '--',linewidth = 0.5,color = 'w')

    axis.tick_params(axis='y', pad = 0.01)
    axis_sed.tick_params(axis='y', pad = 1)

    years = mdates.YearLocator(yspace)  # every Xth year
    years_fmt = mdates.DateFormatter('%Y')

    axis.xaxis.set_major_locator(years)
    axis.xaxis.set_major_formatter(years_fmt)
    axis_sed.xaxis.set_major_locator(years)
    axis_sed.xaxis.set_major_formatter(years_fmt)

    axis.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    axis.set_xticklabels([])

    title = '%s, $\mu M$' % name

    # TODO: check how to simplify this
    for unit, vnames in cfg["units"].items():
        if name in vnames:
            title = name + ', ' + unit
            break

    axis.set_title(title)

def fig_ztime(ds, picname, varnames, icol, nrows, ncols):
    global gs

    ds = ds.sel(time=slice(t1, t2)).isel(i=icol)
    xs = ds['time'].values
    ys = ds['z'].values
    y2s = ds['z2'].values
    y_sed = ((ys - ys[sed]) * 100)

    nv = len(varnames)

    fig, (axes, axes_cb, axes_sed, axes_sed_cb) = gm.get_fig_axes(nrows, ncols, nv)

    for i in np.arange(len(varnames)):
        print(i,varnames[i])
        if varnames[i] != 'Kz':
            plot_param(ds, varnames[i], xs, ys, y_sed, axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])
        else:
            plot_param(ds, varnames[i], xs, y2s, y_sed, axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])

    plt.savefig(picname + '.png', bbox_inches='tight', dpi=300)
