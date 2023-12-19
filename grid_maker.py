import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

h = 0.4
w = 0.1

def create_gs22(gs, pos):
    return gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=gs[pos],
                                            hspace=h,wspace=w,height_ratios=[3,2],
                                            width_ratios = [50,1])

def create_gs32(gs, pos):
    return gridspec.GridSpecFromSubplotSpec(3, 2, subplot_spec=gs[pos],
                                            hspace=h,wspace=w,height_ratios=[3,3,2],
                                            width_ratios = [50,1])


def get_fig_axes(nrows,ncols, ngss, gstype='22'):
    '''
    TODO: Rewrite the function, it's really ugly now
    :param nrows:
    :param ncols:
    :param ngss:
    :param gstype:
    :return:
    '''
    if gstype == '22':
        fig = plt.figure(figsize=(5 * ncols, 2 * nrows))
        hspace = 0.5
    elif gstype == '32':
        fig = plt.figure(figsize=(5 * ncols, 3.5 * nrows))
        hspace = 0.35

    gs = gridspec.GridSpec(nrows, ncols)
    gs.update(left=0.07, right=0.93,
              bottom=0.08, top=0.95,
              wspace=0.2, hspace=hspace)

    axes = []
    axes_cb = []
    axes_sed = []
    axes_sed_cb = []

    if gstype == '22':
        gss = [create_gs22(gs, n) for n in range(ngss)]

        for g in gss:
            ax, ax_cb, ax_sed, ax_sed_cb = [fig.add_subplot(a) for a in list(g)]
            axes.append(ax)
            axes_cb.append(ax_cb)
            axes_sed.append(ax_sed)
            axes_sed_cb.append(ax_sed_cb)

        ax_sets = (axes, axes_cb, axes_sed, axes_sed_cb)

    elif gstype == '32':
        gss = [create_gs32(gs, n) for n in range(ngss)]
        axes_1d = []

        for g in gss:
            ax1d, _, ax, ax_cb, ax_sed, ax_sed_cb = [fig.add_subplot(a) for a in list(g)]
            _.remove()
            axes_1d.append(ax1d)
            axes.append(ax)
            axes_cb.append(ax_cb)
            axes_sed.append(ax_sed)
            axes_sed_cb.append(ax_sed_cb)

        ax_sets = (axes_1d, axes, axes_cb, axes_sed, axes_sed_cb)

    return fig, ax_sets