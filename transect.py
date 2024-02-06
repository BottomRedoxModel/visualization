import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
# import config as cfg
import grid_maker as gm
import my_cmaps as mcm
import utils


cfg = utils.load_config('config.json')

sed = cfg["case_specific"]["sed"]
sed2 = cfg["case_specific"]["sed2"]


def plot_param(ds, name, x, y, y_sed, axis,axis_cb,axis_sed,axis_cb_sed):

    var = ds[name].values.T
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
    axis_sed.set_ylim(5,-5)

    axis_sed.axhline(0,linestyle = '--',linewidth = 0.5,color = 'w')

    axis.tick_params(axis='y', pad = 0.01)
    axis_sed.tick_params(axis='y', pad = 1)

    axis.set_xticklabels([])


    # TODO: check how to simplify this
    for unit, vnames in cfg["units"].items():
        if name in vnames:
            title = name + ', ' + unit
            break


def plot_param_depth(ds, name, lev, x, ax):

    var = ds[name].isel(z=lev)
    ax.plot(x, var, c='k')
    ax.set_xticklabels([])

def fig_transect(ds, picname, varnames, t0, nrows, ncols):

    ds = ds.sel(time=t0, method='nearest').squeeze()
    xs = ds['i'].values
    ys = ds['z'].values
    y2s = ds['z2'].values
    y_sed = ((ys - ys[sed]) * 100)

    nv = len(varnames)

    fig, (axes, axes_cb, axes_sed, axes_sed_cb) = gm.get_fig_axes(nrows, ncols, nv, gstype='22')

    for i in np.arange(nv):
        if varnames[i] != 'Kz':
            plot_param(ds, varnames[i], xs, ys, y_sed, axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])
        else:
            plot_param(ds, varnames[i], xs, y2s, y_sed, axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])
        title = '%s, $\mu M$' % varnames[i]
        axes[i].set_title(title)

    # fig.suptitle(t0[:-9])
    plt.savefig(picname + t0[:-9] + '.png', bbox_inches='tight', dpi=300)


def fig_transect_depth(ds, picname, varnames, t0, lev, nrows, ncols):

    ds = ds.sel(time=t0, method='nearest').squeeze()
    xs = ds['i'].values
    ys = ds['z'].values
    y2s = ds['z2'].values
    y_sed = ((ys - ys[sed]) * 100)

    nv = len(varnames)

    fig, (axes1d, axes, axes_cb, axes_sed, axes_sed_cb) = gm.get_fig_axes(nrows, ncols, nv, gstype='32')

    for i in np.arange(nv):

        if varnames[i] != 'Kz':
            plot_param_depth(ds, varnames[i], lev, xs, axes1d[i])
            plot_param(ds, varnames[i], xs, ys, y_sed, axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])
        else:
            plot_param(ds, varnames[i], xs, y2s, y_sed, axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])
        title = '%s, $\mu M$' % varnames[i]
        axes1d[i].set_title(title)
    # fig.suptitle(t0[:-9])
    plt.savefig(picname + t0[:-9] + '.png', bbox_inches='tight', dpi=300)
