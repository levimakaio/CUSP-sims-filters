from .butterworthH_ClassMethods         import *                                #Member Definitions

#==========================================  butterPoles  ===========================================
lib.butterPoles.restype                                                    = None
lib.butterPoles.argtypes                                                   = [SU, D, P(D), P(D)]
def butterPoles(filterOrder:SU, cutoffFrequency:D, gain:P(D), pPoles:P(D)):
	return lib.butterPoles(filterOrder, cutoffFrequency, gain, pPoles)

