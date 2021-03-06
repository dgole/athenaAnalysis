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
nStart       = 15
nEnd         = 21
ks           = [[248,265],[64,73],[440,449]]
pathBase   = "../../data/prodRuns/run100/"
pathSave     = pathBase + 'plots/pspec/'
if not os.path.exists(pathSave): os.makedirs(pathSave)
plt.figure(0)
################################################################################
vExpo = -1.833
eExpo = 2.0*(vExpo)+2.0
print("velocity spectrum PL exponent is " + str(vExpo))
print("KE power spectrum PL exponent is " + str(eExpo))
################################################################################
# SI run
pathBase   = "../../data/prodRuns/run100/"
pathIn     = pathBase + 'pspecData/'
# mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[0][0])+"_"+str(ks[0][1])+".npy"
inData     = np.load(pathIn + fileName)
freqs      = inData[0,:]
pskMid     = inData[1,:]
pskMid    *= np.power(freqs, -eExpo)
divByThis  = np.mean(pskMid)
pskMid    /= divByThis
# off mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[1][0])+"_"+str(ks[1][1])+".npy"
inData     = np.load(pathIn + fileName)
pskLow     = inData[1,:]
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[2][0])+"_"+str(ks[2][1])+".npy"
inData     = np.load(pathIn + fileName)
pskHigh    = inData[1,:]
pskOff     = (pskLow + pskHigh) / 2.0
pskOff    *= np.power(freqs, -eExpo)
pskOff    /= divByThis

plt.loglog(freqs, pskMid, label='Just SI, mid-plane',     color='k', lineStyle='-')
#plt.loglog(freqs, pskOff, label='Just SI, off-mid-plane', color='k', lineStyle=':')

#plt.loglog(freqs, pskMid, label='Just SI, mid-plane', color='k', lineStyle='-')


# Driven run
pathBase   = "../../data/prodRuns/run101/"
pathIn     = pathBase + 'pspecData/'
# mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[0][0])+"_"+str(ks[0][1])+".npy"
inData     = np.load(pathIn + fileName)
freqs      = inData[0,:]
pskMid     = inData[1,:]
pskMid    *= np.power(freqs, -eExpo)
pskMid    /= divByThis
# off mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[1][0])+"_"+str(ks[1][1])+".npy"
inData     = np.load(pathIn + fileName)
pskLow     = inData[1,:]
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[2][0])+"_"+str(ks[2][1])+".npy"
inData     = np.load(pathIn + fileName)
pskHigh    = inData[1,:]
pskOff     = (pskLow + pskHigh) / 2.0
pskOff    *= np.power(freqs, -eExpo)
pskOff    /= divByThis

#plt.loglog(freqs, pskMid, label='Driven ('+r"$\alpha=10^{-3.5}$"+'), mid-plane',     color='b', lineStyle='-')
#plt.loglog(freqs, pskOff, label='Driven ('+r"$\alpha=10^{-3.5}$"+'), off-mid-plane', color='b', lineStyle=':')


# Driven run
pathBase   = "../../data/prodRuns/run103/"
pathIn     = pathBase + 'pspecData/'
# mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[0][0])+"_"+str(ks[0][1])+".npy"
inData     = np.load(pathIn + fileName)
freqs      = inData[0,:]
pskMid     = inData[1,:]
pskMid    *= np.power(freqs, -eExpo)
pskMid    /= divByThis
# off mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[1][0])+"_"+str(ks[1][1])+".npy"
inData     = np.load(pathIn + fileName)
pskLow     = inData[1,:]
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[2][0])+"_"+str(ks[2][1])+".npy"
inData     = np.load(pathIn + fileName)
pskHigh    = inData[1,:]
pskOff     = (pskLow + pskHigh) / 2.0
pskOff    *= np.power(freqs, -eExpo)
pskOff    /= divByThis

plt.loglog(freqs, pskMid, label='Driven ('+r"$\alpha=1 \times 10^{-4}$"+'), mid-plane',     color='g', lineStyle='-')
#plt.loglog(freqs, pskOff, label='Driven ('+r"$\alpha=1 \times 10^{-4}$"+'), off-mid-plane', color='g', lineStyle=':')

#plt.loglog(freqs, pskMid, label='Driven ('+r"$\alpha=1 \times 10^{-4}$"+'), mid-plane',     color='k', lineStyle=':')


# Driven run
pathBase   = "../../data/prodRuns/run102/"
pathIn     = pathBase + 'pspecData/'
# mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[0][0])+"_"+str(ks[0][1])+".npy"
inData     = np.load(pathIn + fileName)
freqs      = inData[0,:]
pskMid     = inData[1,:]
pskMid    *= np.power(freqs, -eExpo)
pskMid    /= divByThis
# off mid-plane slices
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[1][0])+"_"+str(ks[1][1])+".npy"
inData     = np.load(pathIn + fileName)
pskLow     = inData[1,:]
fileName   = "pspecData_" + str(nStart)+"_"+str(nEnd)+"_"+str(ks[2][0])+"_"+str(ks[2][1])+".npy"
inData     = np.load(pathIn + fileName)
pskHigh    = inData[1,:]
pskOff     = (pskLow + pskHigh) / 2.0
pskOff    *= np.power(freqs, -eExpo)
pskOff    /= divByThis

plt.loglog(freqs, pskMid, label='Driven ('+r"$\alpha=1 \times 10^{-3}$"+'), mid-plane',     color='r', lineStyle='-')
#plt.loglog(freqs, pskOff, label='Driven ('+r"$\alpha=1 \times 10^{-3}$"+'), off-mid-plane', color='r', lineStyle=':')




plt.xlabel(r'$|\mathbf{k}|$')
plt.ylabel('Power')
plt.ylim(5.e-3,1.e2)
plt.xlim(freqs[1],freqs[-1])
#plt.legend(loc=(1.01,0.0))
plt.legend()
tools.saveAndClear(pathSave + 'adjustedPspec_2D_multi.png', figNum=0)








#
