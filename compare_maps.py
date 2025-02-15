import constants
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import ticker
import matplotlib.dates as mdates
import utils
import my_cmaps as mcm #color maps

h = 0.2 #height figure
w = 0.04 #width figure
cfg = utils.load_config('config.json') #load configs from a file
yspace = cfg["z-time"]["yspace"] #how often the year will be shown on x-axis

#Making a plot with:
def plot_param(ds, name, x, y, axis, lims):

    var = ds[name].values #loading values
    levels = np.linspace(lims[0], lims[1], 30) #color limits
    if all(lev == levels[0] for lev in levels): #adjust if all levels are equal
        levels = np.linspace(levels[0], levels[0] + 0.1, 30)

    X, Y = np.meshgrid(x, y) #making a grid for x and y values

    if name in mcm.cmap_dict.keys(): #if the name is mcm.cmap_dict (color map)
        cmap = mcm.cmap_dict[name]
    else:
        cmap = 'turbo' #if no, use turbo as standard color map
    CS_1 = axis.contourf(X, Y, var.T, levels=levels, cmap=cmap) #making a color map (contour map)

    #setting up color scale
    tick_locator = ticker.MaxNLocator(nbins=4) #Maximum 4 numbers on the scale
    cb = plt.colorbar(CS_1, ax=axis, extend='both') #Adding color scale
    cb.formatter.set_powerlimits((-4, 4)) #Adjusting exponent format
    cb.locator = tick_locator
    cb.update_ticks()

    #Adding years to the scale
    years = mdates.YearLocator(yspace)  # every 5 year
    years_fmt = mdates.DateFormatter('%Y') #Showing only years

    axis.xaxis.set_major_locator(years)
    axis.xaxis.set_major_formatter(years_fmt)

    axis.format_xdata = mdates.DateFormatter('%Y-%m-%d')

#Comparing more maps and making a figure
def fig_map_compare(dss, picname, varnames, zlev, nrows, ncols, lims):

    fig, axs = plt.subplots(nrows, ncols)
    fig.set_size_inches((6 * ncols, 2 * nrows)) #size on the figure

    #Going through the data sets
    for ids, ds in enumerate(dss):
        ds = ds.isel(z=zlev) #depth
        xs = ds['time'].values #time
        ys = ds['i'].values #positions

        #Going through the variables
        for i,name in enumerate(varnames):
            ax = axs[ids,:][i]
            plot_param(ds, name, xs, ys, ax, lims[i]) #Drawing the variable
            print(name)

            title = '%s, $\mu M$' % name

            # TODO: check how to simplify this
            for unit, vnames in constants.UNITS.items():
                if name in vnames:
                    title = name + ', ' + unit
                    break
            ax.set_title(title)

    #adding text to y-axis
    [axis.set_ylabel('x ,m') for axis in axs.flatten()]
    fig.tight_layout()
    plt.savefig('%s_lev%i.png' % (picname, zlev)) #save the fig