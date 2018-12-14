#!/usr/bin/python
import numpy as np
import matplotlib as m
m.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
import math
import sys
sys.path.append('../python')
import athenaReader3d as reader3d
import athenaTools as tools
from matplotlib.backends.backend_pdf import PdfPages
################################################################################
pathBase = str(sys.argv[1])
################################################################################
path3d   = pathBase + '3d/'
pathSave = pathBase + 'plots/slices/'
if not os.path.exists(pathSave): os.makedirs(pathSave)
do3d = reader3d.Data3d(path3d)
################################################################################
# midplane slices
for key in ['drho', 'rho', 'vx', 'vy', 'vz']:
    for n in range(10, do3d.nt, 10):
        reader3d.slicePlot(do3d, key, n=n, figNum=0)
        tools.saveAndClear(pathSave + 'midplaneSlice_' + key + '_' + str(n) + '.png', figNum=0)
################################################################################
for key in ['dpar']:
    for n in range(10, do3d.nt, 1):
        reader3d.slicePlot(do3d, key, n=n, figNum=0)
        tools.saveAndClear(pathSave + 'midplaneSlice_' + key + '_' + str(n) + '.png', figNum=0)















#
