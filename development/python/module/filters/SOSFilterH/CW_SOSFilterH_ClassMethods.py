from .SOSFilterH_ClassMembers           import *                                #Class Member definitions
#=======================================  SOSFilterTDF2_typ  ========================================
#constructor(s)
lib.CW_SOSFilterTDF2_typ_create_OL0.restype                                = P(SOSFilterTDF2_typ)
lib.CW_SOSFilterTDF2_typ_create_OL0.argtypes                               = []
@SOSFilterTDF2_typ.methods.addFunction
def create():
	return lib.CW_SOSFilterTDF2_typ_create_OL0()

lib.CW_SOSFilterTDF2_typ_create_OL1.restype                                = P(SOSFilterTDF2_typ)
lib.CW_SOSFilterTDF2_typ_create_OL1.argtypes                               = [I, I]
@SOSFilterTDF2_typ.methods.addFunction
def create(_order:I, _dimension:I):
	return lib.CW_SOSFilterTDF2_typ_create_OL1(_order, _dimension)



#destrutor
lib.CW_SOSFilterTDF2_typ_delete.restype                                    = None
lib.CW_SOSFilterTDF2_typ_delete.argtypes                                   = [P(SOSFilterTDF2_typ)]
@SOSFilterTDF2_typ.methods.addFunction
def delete(ptr:P(SOSFilterTDF2_typ)):
	return lib.CW_SOSFilterTDF2_typ_delete(ptr)



#method(s)
lib.CW_SOSFilterTDF2_typ_init_OL0.restype                                  = P(D)
lib.CW_SOSFilterTDF2_typ_init_OL0.argtypes                                 = [P(SOSFilterTDF2_typ)]
@SOSFilterTDF2_typ.methods.addFunction
def init(ptr:SOSFilterTDF2_typ):
	return lib.CW_SOSFilterTDF2_typ_init_OL0(ptr)

lib.CW_SOSFilterTDF2_typ_init_OL1.restype                                  = P(D)
lib.CW_SOSFilterTDF2_typ_init_OL1.argtypes                                 = [P(SOSFilterTDF2_typ), P(D)]
@SOSFilterTDF2_typ.methods.addFunction
def init(ptr:SOSFilterTDF2_typ, pX:P(D)):
	return lib.CW_SOSFilterTDF2_typ_init_OL1(ptr, pX)

lib.CW_SOSFilterTDF2_typ_update.restype                                    = P(D)
lib.CW_SOSFilterTDF2_typ_update.argtypes                                   = [P(SOSFilterTDF2_typ), P(D)]
@SOSFilterTDF2_typ.methods.addFunction
def update(ptr:SOSFilterTDF2_typ, pX:P(D)):
	return lib.CW_SOSFilterTDF2_typ_update(ptr, pX)

lib.CW_SOSFilterTDF2_typ_lowPass.restype                                   = None
lib.CW_SOSFilterTDF2_typ_lowPass.argtypes                                  = [P(SOSFilterTDF2_typ), D, D]
@SOSFilterTDF2_typ.methods.addFunction
def lowPass(ptr:SOSFilterTDF2_typ, cutoffFrequency:D, sampleFrequency:D):
	return lib.CW_SOSFilterTDF2_typ_lowPass(ptr, cutoffFrequency, sampleFrequency)


