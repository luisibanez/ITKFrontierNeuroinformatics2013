#!/usr/bin/env python

import json
import sys
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from prettyplotlib import hist
import numpy as np

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'large'
mpl.rcParams['ytick.labelsize'] = 'large'
mpl.rcParams['figure.dpi'] = 900


def plot_patchset_histogram(changes, outputfile=None):
    number_of_patchsets = []
    for change in changes:
        number_of_patchsets.append(len(change['patchSets']))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    hist(ax, number_of_patchsets, bins=np.max(number_of_patchsets))
    ax.set_xlabel('Number of Patch Sets')
    ax.set_ylabel('Change Count')
    ax.set_xlim(0, 20)
    if outputfile:
        fig.savefig(outputfile)
    else:
        plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ' + sys.argv[0] +
              ' <gerrit_data.json> [output_file.eps]')
        sys.exit(1)

    gerrit_data = sys.argv[1]
    with open(gerrit_data, 'r') as fp:
        data = json.load(fp)
    if len(sys.argv) > 2:
        outputfile = sys.argv[2]
        dirname = os.path.dirname(outputfile)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
    else:
        outputfile = None
    plot_patchset_histogram(data['changes'], outputfile)
