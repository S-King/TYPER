#!/usr/bin/env python3
"""
=================
Multiple subplots
=================

Simple demo with multiple subplots.
"""

# Stuff for plotting #
import matplotlib # so that you can save images out
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib as mpl
######################


import numpy as np


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.savefig('plottest.svg') # Any filename will do