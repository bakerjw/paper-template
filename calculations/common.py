"""
Shared settings for all figure scripts.

Every script imports this module, so figure formatting and output
locations are defined in one place. Change the style file or the paths
here, rerun make_all_figures.py, and every figure in the paper updates.
"""

import os
import matplotlib.pyplot as plt

# --- Paths ---
calc_dir = os.path.dirname(os.path.abspath(__file__))
paper_dir = os.path.join(calc_dir, '..')
figure_dir = os.path.join(paper_dir, 'figures')
# If you write on Overleaf with Dropbox sync, point this at the figures
# folder of the synced project instead, so new figures go straight to
# Overleaf. For example:
# figure_dir = os.path.expanduser('~/Dropbox/Apps/Overleaf/My paper/figures')
os.makedirs(figure_dir, exist_ok=True)

# --- Style ---
# One style file controls fonts, sizes, line widths, and colors for
# every figure. See figure.mplstyle for details.
plt.style.use(os.path.join(calc_dir, 'figure.mplstyle'))
plt.rcParams['font.size'] = 10  # a bit larger, to suit 11 pt paper text
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Width of the paper's text block, for full-width figures [inches]
full_width = 6.0


def save_figure(fig, name):
    """Save a figure to the paper's figures folder as a PDF."""
    fig.savefig(os.path.join(figure_dir, name + '.pdf'))
    plt.close(fig)

