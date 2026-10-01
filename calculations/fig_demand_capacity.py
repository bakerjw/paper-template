"""
Example calculation and single-panel figure: structural demand and
capacity distributions.

Output: figures/demand_capacity.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

from common import colors, save_figure

# --- Calculations ---
# Lognormal demand and capacity, in terms of story drift ratio
median_demand, beta_demand = 0.027, 0.5
median_capacity, beta_capacity = 0.064, 0.45

# --- Figure ---
drift = np.linspace(0.0005, 0.15, 500)
pdf_demand = lognorm.pdf(drift, beta_demand, scale=median_demand)
pdf_capacity = lognorm.pdf(drift, beta_capacity, scale=median_capacity)

fig, ax = plt.subplots()
ax.plot(drift, pdf_demand, color=colors[0])
ax.plot(drift, pdf_capacity, color=colors[1])

# Direct labels in place of a legend
ax.text(0.036, 29, 'Demand', color=colors[0])
ax.text(0.080, 13, 'Capacity', color=colors[1])

ax.set_xlabel('Story drift ratio')
ax.set_ylabel('Probability density')
ax.set_xlim(0, 0.15)
ax.set_ylim(bottom=0)

save_figure(fig, 'demand_capacity')
