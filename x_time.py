import matplotlib.pyplot as plt
import numpy as np

from matplotlib import ticker
import matplotlib.dates as mdates
# import config as cfg
import utils
import my_cmaps as mcm

h = 0.2
w = 0.04
cfg = utils.load_config('config.json')
yspace = cfg["z-time"]["yspace"]

def plot_param(ds, name, x, y, axis):

    var = ds[name].values
    levels = np.linspace(np.min(var), np.max(var), 30)
    if all(lev == levels[0] for lev in levels):
        levels = np.linspace(levels[0], levels[0] + 0.1, 30)

    X, Y = np.meshgrid(x, y)

    if name in mcm.cmap_dict.keys():
        cmap = mcm.cmap_dict[name]
    else:
        cmap = 'turbo'
    CS_1 = axis.contourf(X, Y, var.T, levels=levels, cmap=cmap)

    tick_locator = ticker.MaxNLocator(nbins=4)
    cb = plt.colorbar(CS_1, ax=axis)
    cb.formatter.set_powerlimits((-4, 4))
    cb.locator = tick_locator
    cb.update_ticks()

    years = mdates.YearLocator(yspace)  # every 5 year
    years_fmt = mdates.DateFormatter('%Y')

    axis.xaxis.set_major_locator(years)
    axis.xaxis.set_major_formatter(years_fmt)

    axis.format_xdata = mdates.DateFormatter('%Y-%m-%d')


def fig_map(ds, picname, varnames, zlev, nrows, ncols):

    ds = ds.isel(z=zlev)
    xs = ds['time'].values
    ys = ds['i'].values

    fig, axs = plt.subplots(nrows, ncols)
    fig.set_size_inches((6*ncols,2*nrows))

    for i,name in enumerate(varnames):
        ax = axs.flatten()[i]
        plot_param(ds, name, xs, ys, ax)
        print(name)

        title = '%s, $\mu M$' % name

        # TODO: check how to simplify this
        for unit, vnames in cfg["units"].items():
            if name in vnames:
                title = name + ', ' + unit
                break
        ax.set_title(title)

    [fig.delaxes(axs.flatten()[j]) for j in np.arange(i+1,nrows*ncols)]

    [axis.set_ylabel('x ,m') for axis in axs.flatten()]
    fig.tight_layout()
    plt.savefig('%ss_lev%i.png' % (picname, zlev))