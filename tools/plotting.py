#---------------------------------
#
# A bunch of functions to make
# numpy histograms look better
#
#  Added marker style for error bar
#---------------------------------
import numpy as np
import matplotlib.pyplot as plt

def statBox(ax, entries, binEdges, x=0.96, y=0.98, fontsize='medium'):
    """
    Put a stat box on the histogram at coord x and y
    font = medium is appropriate for 1x1.  Other choices are
    size in points, 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'
    """
    en = len(entries)                   # number of entries
    ov = (entries>binEdges[-1]).sum()   # overflows
    uf = (entries<binEdges[0]).sum()    # underflows
    mn = entries.mean()                 # mean
    sd = entries.std()                  # standard deviation
    textstr = 'N=%i \nOverflow=%i \nUnderflow=%i \n$\mu=%.2f$ \n$\sigma=%.2f$' % (en, ov, uf, mn, sd)
    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    ax.text(x, y, textstr,
            transform=ax.transAxes,
            bbox=props,
            fontsize=fontsize,
            horizontalalignment='right',
            verticalalignment='top'  )


def plotErr(ax, y, binEdges, err=None, color='black', marker=''):
    """
    Add error bars on plot.  If err=None use sqrt(contents)
    """
    if err is None:
        dy = np.sqrt(y)
    else:
        dy = err

    binCenters = 0.5 * (binEdges[1:] + binEdges[:-1])
    ax.errorbar(binCenters, y, yerr=dy, linestyle="none", color=color,
                marker=marker)

