"""
Regenerate every figure in the paper.

Run this after changing any calculation or the style file:

    python calculations/make_all_figures.py

then recompile paper.tex. Months or years later, running this script
is also the fastest way to find the code behind a particular figure.
"""

import os
import runpy

calc_dir = os.path.dirname(os.path.abspath(__file__))

# List scripts in the order their figures appear in the paper
scripts = [
    'fig_demand_capacity.py',
    'fig_fragility_and_consequences.py',
]

for script in scripts:
    print(f'Running {script}')
    runpy.run_path(os.path.join(calc_dir, script), run_name='__main__')

print('Done. Recompile paper.tex to see the updated figures.')
