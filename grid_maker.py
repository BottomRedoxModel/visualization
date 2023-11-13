import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

h = 0.4
w = 0.1

def create_gs(gs, pos):
    return gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=gs[pos],
                                            hspace=h,wspace=w,height_ratios=[3,2],
                                            width_ratios = [50,1])


def get_fig_axes(nrows,ncols, ngss):
    fig = plt.figure(figsize=(5 * ncols, 2 * nrows), dpi=100)

    gs = gridspec.GridSpec(nrows, ncols)
    gs.update(left=0.07, right=0.93,
              bottom=0.08, top=0.95,
              wspace=0.2, hspace=0.5)

    gss = [create_gs(gs, n) for n in range(ngss)]

    axes = []
    axes_cb = []
    axes_sed = []
    axes_sed_cb = []
    for g in gss:
        ax, ax_cb, ax_sed, ax_sed_cb = [fig.add_subplot(a) for a in list(g)]
        axes.append(ax)
        axes_cb.append(ax_cb)
        axes_sed.append(ax_sed)
        axes_sed_cb.append(ax_sed_cb)
    return fig, (axes, axes_cb, axes_sed, axes_sed_cb)