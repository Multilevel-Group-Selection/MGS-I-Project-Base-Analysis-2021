# Name: Contour plots
# Description: Python script for creating Figure 6 in the manuscript,
#  which includes four contour maps that depict the results of sweeps.
# Author: Garry Sotnik

import pandas as pd
import numpy as np

contour1_data = pd.read_csv("final IPC 0.3 D 0.3 w move.csv")
contour2_data = pd.read_csv("final IPC 0.3 D 0.7 w move.csv")
contour3_data = pd.read_csv("final IPC 0.3 D 0.3 w move.csv")
contour4_data = pd.read_csv("final IPC 0.3 D 0.7 wo move.csv")

Z1 = contour1_data.pivot_table(index='x', columns='y', values='z').T.values
Z2 = contour2_data.pivot_table(index='x', columns='y', values='z').T.values
Z3 = contour3_data.pivot_table(index='x', columns='y', values='z').T.values
Z4 = contour4_data.pivot_table(index='x', columns='y', values='z').T.values

X1_unique = np.sort(contour1_data.x.unique())
Y1_unique = np.sort(contour1_data.y.unique())
X1, Y1 = np.meshgrid(X1_unique, Y1_unique)

X2_unique = np.sort(contour2_data.x.unique())
Y2_unique = np.sort(contour2_data.y.unique())
X2, Y2 = np.meshgrid(X2_unique, Y2_unique)

X3_unique = np.sort(contour3_data.x.unique())
Y3_unique = np.sort(contour3_data.y.unique())
X3, Y3 = np.meshgrid(X3_unique, Y3_unique)

X4_unique = np.sort(contour4_data.x.unique())
Y4_unique = np.sort(contour4_data.y.unique())
X4, Y4 = np.meshgrid(X4_unique, Y4_unique)

pd.DataFrame(Z1).round(3)
pd.DataFrame(Z2).round(3)
pd.DataFrame(Z3).round(3)
pd.DataFrame(Z4).round(3)

pd.DataFrame(X1).round(3)
pd.DataFrame(X2).round(3)
pd.DataFrame(X3).round(3)
pd.DataFrame(X4).round(3)

pd.DataFrame(Y1).round(3)
pd.DataFrame(Y2).round(3)
pd.DataFrame(Y3).round(3)
pd.DataFrame(Y4).round(3)

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('svg')

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Initialize plot objects
fig = plt.figure()
ax = fig.add_subplot(111)    # The big plot
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

# Generate a color mapping of the levels we've specified
import matplotlib.cm as cm # matplotlib's color map library
cpf1 = ax1.contourf(Y1,X1,Z1, cmap=cm.Oranges)
cpf2 = ax2.contourf(Y2,X2,Z2, cmap=cm.Oranges)
cpf3 = ax3.contourf(Y3,X3,Z3, cmap=cm.Oranges)
cpf4 = ax4.contourf(Y4,X4,Z4, cmap=cm.Oranges)

# Set common labels
ax.set_xlabel('Synergy')
ax.set_ylabel('Pressure')

ax1.tick_params(bottom=True, top=True, left=True, right=True)
plt.setp(ax1, xticks=range(0,11,1), yticks=range(0,11,1))
plt.setp(ax2, xticks=range(0,11,1), yticks=range(0,11,1))
plt.setp(ax3, xticks=range(0,11,1), yticks=range(0,11,1))
plt.setp(ax4, xticks=range(0,11,1), yticks=range(0,11,1))

ax1.tick_params(bottom=True, top=True, left=True, right=True, labelbottom=False, labeltop=True, labelleft=True, labelright=False)
ax2.tick_params(bottom=True, top=True, left=True, right=True, labelbottom=False, labeltop=True, labelleft=False, labelright=True)
ax3.tick_params(bottom=True, top=True, left=True, right=True, labelbottom=True, labeltop=False, labelleft=True, labelright=False)
ax4.tick_params(bottom=True, top=True, left=True, right=True, labelbottom=True, labeltop=False, labelleft=False, labelright=True)
fig.tight_layout()

ax1.text(2.1, .2, r'D: 0.3, move', fontsize=10)
ax2.text(2.1, .2, r'D: 0.7, move', fontsize=10)
ax3.text(2.1, .2, r'D: 0.3, no move', fontsize=10)
ax4.text(2.1, .2, r'D: 0.7, no move', fontsize=10)

ax1.axhline(1,color='black',ls='--', linewidth=1)
ax2.axhline(1,color='black',ls='--', linewidth=1)
ax3.axhline(1,color='black',ls='--', linewidth=1)
ax4.axhline(1,color='black',ls='--', linewidth=1)

cbaxes = inset_axes(ax1, width="10%", height="60%", loc=2)
plt.colorbar(cpf1, cax=cbaxes, ticks=range(0,101,50), orientation='vertical')

plt.savefig('Contour plots.jpg', dpi = 300)