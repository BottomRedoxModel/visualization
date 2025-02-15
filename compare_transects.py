import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
# import config as cfg
import grid_maker as gm
import my_cmaps as mcm
import utils

#Loading configuration file
cfg = utils.load_config('config.json')

#Getting sediment values from the configuration
sed = cfg["case_specific"]["sed"]
sed2 = cfg["case_specific"]["sed2"]

#Drawing a variable from the dataset
def plot_param(ds, name, x, y, y_sed, axis,axis_cb,axis_sed,axis_cb_sed, lims_w, lims_sed):

    var = ds[name].values.T
    print(var.shape)
    levels = np.linspace(lims_w[0], lims_w[1], 30)
    sed_levels = np.linspace(lims_sed[0], lims_sed[1], 30)
    # if all(lev == levels[0] for lev in levels):
    #     levels = np.linspace(levels[0], levels[0]+0.1, 30)
    # if all(lev == sed_levels[0] for lev in sed_levels):
    #     sed_levels = np.linspace(sed_levels[0], sed_levels[0]+0.1, 30)

    #Making grid for water and sediment
    X,Y = np.meshgrid(x,y[:sed2])
    X_sed,Y_sed = np.meshgrid(x,y_sed[sed2:])
    if name in mcm.cmap_dict.keys():
        cmap = mcm.cmap_dict[name]
    else:
        cmap = 'turbo'

    #Drawing the sediment part
    CS_1_sed = axis_sed.contourf(X_sed,Y_sed, var[:,sed2:].T,
                                 levels = sed_levels, cmap = cmap, extend='both')

    #if the variable is oxygen, use plasma color map
    # TODO: fix it
    if name == 'Oxy':
        cmap = 'plasma'
    CS_1 = axis.contourf(X, Y, var[:, :sed2].T,
                         levels=levels, cmap=cmap)

    #setting up color scale
    locw = ticker.MaxNLocator(nbins=2, steps=[2, 3, 5, 10])

    cb = plt.colorbar(CS_1,cax = axis_cb, extend='both')
    cb.ax.yaxis.set_major_locator(locw)
    cb.formatter.set_powerlimits((-4, 4))

    cb_sed = plt.colorbar(CS_1_sed,cax = axis_cb_sed, extend='both')
    locs = ticker.MaxNLocator(nbins=2, steps=[2, 3, 5, 10])
    cb_sed.ax.yaxis.set_major_locator(locs)
    cb_sed.formatter.set_powerlimits((-4, 4))

    axis.set_ylim(np.max(y[:sed2]),0)
    axis_sed.set_ylim(5,-5)

    #adding a dotted line with the 0 level in the sediment
    axis_sed.axhline(0,linestyle = '--',linewidth = 0.5,color = 'w')

    axis.tick_params(axis='y', pad = 0.01)
    axis_sed.tick_params(axis='y', pad = 1)

    #hiding the x-axis
    axis.set_xticklabels([])

    #adding title with unit
    # TODO: check how to simplify this
    for unit, vnames in cfg["units"].items():
        if name in vnames:
            title = name + ', ' + unit
            break

#Making figures for more datasets and saves as picture
def fig_transect_compare(dss, picname, varnames, t0, nrows, ncols, lims_w, lims_sed):

    nv = nrows*ncols #total amount of plots

    print(nrows, ncols, nv)

    #makes a figure with several plots
    fig, (axes, axes_cb, axes_sed, axes_sed_cb) = gm.get_fig_axes(nrows, ncols, nv, gstype='22')
    n = 0 #counting where we are in the figure
    for ids, ds in enumerate(dss):
        print(ids)
        ds = ds.sel(time=t0, method='nearest').squeeze()
        xs = ds['i'].values
        ys = ds['z'].values
        y_sed = ((ys - ys[sed]) * 100)

        #Drawing each variable
        for i in range(ncols):
            plot_param(ds, varnames[i], xs, ys, y_sed,
                       axes[n], axes_cb[n], axes_sed[n], axes_sed_cb[n],
                       lims_w[i], lims_sed[i])
            title = '%s, $\mu M$' % varnames[i]
            axes[n].set_title(title)
            n+=1 #Increasing the counter
    plt.savefig(picname + t0[:-9] + '.png', bbox_inches='tight', dpi=300) #Saving the figure as a picture