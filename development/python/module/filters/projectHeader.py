import os,sys

import ctypes
C  = ctypes.c_char
I  = ctypes.c_int
F  = ctypes.c_float
D  = ctypes.c_double
S  = ctypes.c_short
SU = ctypes.c_ushort
L  = ctypes.c_long
LU = ctypes.c_ulong
B  = ctypes.c_bool
P  = ctypes.POINTER

from directoryPaths import paths
#import pythonTools
sys.path.append(paths.DataLoader.pyModule);
sys.path.append(paths.FunctionOverLoading.pyModule);
from DataLoader          import DataLoader_typ
from FunctionOverLoading import OLF_Dict_typ
from FunctionOverLoading import OLF_classModifier
from FunctionOverLoading import OLF__del__

#link to C library
dllPath = paths.CUSP_sims.Library
if "64 bit" in sys.version:
	dllName = r'filters_64.dll'
else:
	dllName = r'filters_32.dll'
lib     = ctypes.CDLL(dllPath + '\\' + dllName)



#Forward Declarations:
class AS_RollingBuffer_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class AS_MovingAverageFilter_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class AS_CMAFilter_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class AS_BiquadFilter_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class AS_SOSFilter_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class biquadFilterTDF2_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class cascadedMovingAverageFilter_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class movingAverageFilter_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class rollingBuffer_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

class SOSFilterTDF2_typ(ctypes.Structure, DataLoader_typ):
	methods         = OLF_Dict_typ()
	printException  = []
	cfgExclude      = {}

