# SPDX-License-Identifier: LGPL-3.0-or-later

# Name: Figure 2: Size-synergy combinations in MGS I with game theoretic situations
# Description: The Python script identifies and plots size-synergy combinations in
#  MGS I in which agents can face game theoretic situations.
# Author: Garry Sotnik

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange

# Set the limit for effort (e) that an agent can contribute when in a group and
#  create an 8x100 matrix of zeroes (GT) to store the results.

e = 1
GT = np.zeros((8, 100))

# Simulate through all the (group) size-synergy (from prosocial common-pool behavior)
# combinations to identify those in which agents can face Prisoner's Dilemma (T > R > P > S)
# or coordination game (R > T, R > P) situations.

for size in range(2,10):
    for v in arange(0.5, 10, 0.1):
        v = round(v, 3)
        T = round(e+(v*(e*1/size)), 3)
        R = round(v*(e*size/size), 3)
        P = e
        S = round(v*(e*1/size), 3)
        if((T > R) and (R > P) and (P > S)):
            s = int(v*10)
            GT[9-size][s] = .5
        if((R > T) and (P > S)):
            s = int(v*10)
            GT[9-size][s] = 1
            
# Plot the matrix in gray scale and output the result as a .jpg file. The size-synergy
#  combinations in which agents can face a Prisoner's Dilemma are plotted in gray, those
#  in which agents can face a coordination game are in black, and other situations are plotted in white.

fig, ax = plt.subplots()
ax.set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], minor = False)
ax.set_xticklabels([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.xaxis.grid(True, which='major')

ax.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], minor = True)
ax.set_yticklabels([10, 9, 8, 7, 6, 5, 4, 3, 2])
ax.yaxis.grid(True, which = 'minor')

plt.ylabel('Size', fontsize = 12)
plt.xlabel('Synergy', fontsize = 12)
plt.imshow(GT, cmap='gray_r', interpolation='none', aspect = 'auto')
plt.savefig("GT situations.jpg", dpi = 600)
