import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
from PIL import Image
import glob
import config as cfg
import grid_maker as gm


sed = cfg.sed
sed2 = cfg.sed2
tstep = cfg.anim_tstep


def plot_param(ds, name, lims_dict, sed_lims_dict, x, y, y_sed, axis,axis_cb,axis_sed,axis_cb_sed):

    var = ds[name].values.T
    print(var.shape)
    levels = np.linspace(*lims_dict[name], 30)
    sed_levels = np.linspace(*sed_lims_dict[name], 30)
    if all(lev == levels[0] for lev in levels):
        levels = np.linspace(levels[0], levels[0]+0.1, 30)
    if all(lev == sed_levels[0] for lev in sed_levels):
        sed_levels = np.linspace(sed_levels[0], sed_levels[0]+0.1, 30)

    X,Y = np.meshgrid(x,y[:sed2])
    X_sed,Y_sed = np.meshgrid(x,y_sed[sed2:])
    if name in cfg.cmap_dict.keys():
        cmap = cfg.cmap_dict[name]
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

    title = '%s, $\mu M$' % name

    # TODO: check how to simplify this
    for unit, vnames in cfg.units_dict.items():
        if name in vnames:
            title = name + ', ' + unit
            break

    axis.set_title(title)

def anim_transect(ds, picname, varnames, t1, t2, nrows, ncols):

    ds = ds.sel(time=slice(t1, t2))
    xs = ds['i'].values
    ys = ds['z'].values
    y2s = ds['z2'].values
    y_sed = ((ys - ys[sed]) * 100)

    # water min max
    dsw = ds.isel(z=slice(None, sed2))
    lims = [(dsw[name].min().values, dsw[name].max().values) for name in varnames]
    lims_dict = dict(zip(varnames, lims))

    # sediments min max
    dssed = ds.isel(z=slice(sed2, None))
    sed_lims = [(dssed[name].min().values, dssed[name].max().values) for name in varnames]
    sed_lims_dict = dict(zip(varnames, sed_lims))

    nv = len(varnames)
    nt = ds.sizes['time']
    for t in range(0, nt, tstep):  # stepping just by index of time!

        dst = ds.isel(time=t)
        fig, (axes, axes_cb, axes_sed, axes_sed_cb) = gm.get_fig_axes(nrows, ncols, nv)

        for i in np.arange(nv):
            print(i,varnames[i])
            if varnames[i] != 'Kz':
                plot_param(dst, varnames[i], lims_dict, sed_lims_dict, xs, ys, y_sed,
                           axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])
            else:
                plot_param(dst, varnames[i], lims_dict, sed_lims_dict, xs, y2s, y_sed,
                           axes[i], axes_cb[i], axes_sed[i], axes_sed_cb[i])

        fig.suptitle(str(dst['time'].values)[:18], y=1.05)
        print(str(dst['time'].values)[:18])
        plt.savefig(picname + str(dst['time'].values)[:13] + '.png', bbox_inches='tight', dpi=300)

def make_gif(frame_folder, gifname):
    frames = [Image.open(image) for image in sorted(glob.glob(f"{frame_folder}/*.png"))]
    frame_one = frames[0]
    frame_one.save(gifname, format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)