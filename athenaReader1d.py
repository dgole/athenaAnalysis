#!/usr/bin/python
import numpy as np
import matplotlib as m
import matplotlib.pyplot as plt
import os
import matplotlib.colors as colors

#m.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

def getTimeStepString(i):
	if i > 999:	 zstring = ""
	elif i > 99: zstring = "0"
	elif i > 9:  zstring = "00"
	elif i > -1: zstring = "000"
	return zstring+str(i)

####################################################################
# Data class ###############################################
####################################################################
class Data1d:
	def __init__(self, path, baseName="Par_Strat3d", dt=0.1):
		print("initializing 1d data structure from " + path)
		self.path    = path
		fileList     = os.listdir(self.path)
		nFiles       = len(fileList)
		names        = [baseName + "." + getTimeStepString(n) + ".1d" for n in range(nFiles)]
		files        = [np.loadtxt(path+names[n]) for n in range(nFiles)]
		dataArray    = np.asarray(files)
		self.data    = {'rho'     : dataArray[:,:,1],
						'P'       : dataArray[:,:,2],
						'KEx'     : dataArray[:,:,3],
						'KEy'     : dataArray[:,:,4],
						'KEz'     : dataArray[:,:,5],
						'KE'      : dataArray[:,:,6],
						'reynolds': dataArray[:,:,7]}
		self.header  = {'rho'     : r"$\rho$",
						'P'       : r"$P$",
						'KEx'     : r"$KE_x$",
						'KEy'     : r"$KE_y$",
						'KEz'     : r"$KE_z$",
						'KE'      : r"$KE$",
						'reynolds': r"$\rho v_x \delta v_y$"}
		self.z      = dataArray[0,:,0]
		self.nt     = self.data['rho'].shape[0]
		self.nz     = self.data['rho'].shape[1]
		self.zmax   = np.round(-self.z[0],1)
		self.tmax   = dt*self.nt
		self.t      = np.arange(0, self.tmax, dt)
		del files, dataArray
		print("data of shape " + str(self.data['rho'].shape) + " imported")
	def getzindex(self, z):
		return (np.abs(self.z-z)).argmin()
	def gettindex(self, t):
		return (np.abs(self.t-t)).argmin()
	def addCol(self, funcName, key, headerLabel, *args, **kwargs):
		print(self.path + ": adding data with key " + key)
		self.data[key]   = funcName(self)
		self.header[key] = headerLabel

####################################################################
# plotting functions ###############################################
####################################################################
def stPlot(do, key, figNum=0):
	print (do.path + ": making ST plot for key " + key)
	plt.figure(figNum)
	title = do.header[key]
	extent = [0,do.tmax,-do.zmax,do.zmax]
	aspect  = 0.2*do.tmax/do.zmax
	plotData = np.transpose(np.fliplr(do.data[key]))
	if np.amin(plotData) < 0.0:
		cmapType = 'coolwarm'
		maxVal   = np.amax(np.absolute(plotData))
		norm     = colors.SymLogNorm(maxVal/100.0, linscale=2.0)
	else:
		cmapType = 'viridis'
		norm     = colors.LogNorm()
	plt.imshow(plotData, extent=extent, aspect=aspect, cmap=plt.get_cmap(cmapType), norm=norm)
	plt.title(title);
	plt.xlabel(r"$t \Omega$");
	plt.ylabel(r"$z/H$");
	plt.colorbar(shrink=0.5)
	plt.tight_layout()

def profile(do, key, figNum=0, tStart=None, tEnd=None, legendLabel=None):
	print(do.path + ": making profile plot for key " + key)
	plt.figure(figNum)
	if tStart == None: tStart = do.t[-1]/2.0
	if tEnd   == None: tEnd   = do.t[-1]
	nStart   = do.gettindex(tStart)
	nEnd     = do.gettindex(tEnd)
	plotData = np.mean(do.data[key][nStart:nEnd,:], axis=0)
	title    = do.header[key]
	plt.semilogy(do.z, np.absolute(plotData), label=legendLabel)
	plt.ylabel(do.header[key]);
	plt.xlabel(r"$z/H$");
	plt.tight_layout()

def timeEvo(do, key, figNum=0, legendLabel=None):
	print(do.path + ": making timeEvo plot for key " + key)
	plt.figure(figNum)
	plotData = np.mean(do.data[key], axis=1)
	if 10.0*np.amin(np.absolute(plotData[2:])) < np.amax(np.absolute(plotData[2:])):
		plt.semilogy(do.t, np.absolute(plotData), label=legendLabel)
	else:
		plt.plot(do.t, np.absolute(plotData), label=legendLabel)
	plt.ylabel(do.header[key]);
	plt.xlabel(r"$t \Omega$");
	plt.tight_layout()

def dv(do):
	return np.sqrt(2.0*do.data['KE']/do.data['rho'])
