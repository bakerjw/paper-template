"""
Example calculation and two-panel figure: (a) a fragility function and
(b) consequence distributions.

Output: figures/fragility_and_consequences.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, norm

from common import colors, full_width, save_figure

# --- Calculations ---
# Lognormal fragility function
theta, beta_im = 0.5, 0.4  # median [g] and logarithmic standard deviation
im = np.linspace(0.001, 1.5, 300)
p_fail = norm.cdf(np.log(im / theta) / beta_im)

# Beta-distributed consequences, for several parameter values
c = np.linspace(0.001, 0.999, 300)
params = [(0.5, 4), (2, 7), (4, 4), (7, 2)]

# --- Figure ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(full_width, 2.3))

# (a) Fragility function, with the median marked
ax1.plot(im, p_fail, color=colors[0])
ax1.plot([0, theta, theta], [0.5, 0.5, 0], ':k', linewidth=1)
ax1.set_xlabel('Intensity measure, IM [g]')
ax1.set_ylabel('P(F | IM = x)')
ax1.set_xlim(0, 1.5)
ax1.set_ylim(0, 1)

# (b) Consequence distributions
for (r, q), color in zip(params, colors):
    ax2.plot(c, beta.pdf(c, r, q), color=color, label=f'r = {r}, q = {q}')
ax2.set_xlabel('Consequence, C')
ax2.set_ylabel('$f_C(c)$')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 6)
ax2.legend(loc='upper center')

# Panel labels
for ax, label in zip((ax1, ax2), ('(a)', '(b)')):
    ax.text(-0.22, 1.0, label, transform=ax.transAxes,
            va='bottom', fontweight='bold')

save_figure(fig, 'fragility_and_consequences')
