from .BiquadFilterH_ClassMembers        import *                                #Class Member definitions
#======================================  biquadFilterTDF2_typ  ======================================
#constructor(s)
lib.CW_biquadFilterTDF2_typ_create_OL0.restype                             = P(biquadFilterTDF2_typ)
lib.CW_biquadFilterTDF2_typ_create_OL0.argtypes                            = []
@biquadFilterTDF2_typ.methods.addFunction
def create():
	return lib.CW_biquadFilterTDF2_typ_create_OL0()

lib.CW_biquadFilterTDF2_typ_create_OL1.restype                             = P(biquadFilterTDF2_typ)
lib.CW_biquadFilterTDF2_typ_create_OL1.argtypes                            = [I]
@biquadFilterTDF2_typ.methods.addFunction
def create(_dimension:I):
	return lib.CW_biquadFilterTDF2_typ_create_OL1(_dimension)

lib.CW_biquadFilterTDF2_typ_create_OL2.restype                             = P(biquadFilterTDF2_typ)
lib.CW_biquadFilterTDF2_typ_create_OL2.argtypes                            = [I, P(D)]
@biquadFilterTDF2_typ.methods.addFunction
def create(_dimension:I, _coef:P(D)):
	return lib.CW_biquadFilterTDF2_typ_create_OL2(_dimension, _coef)



#destrutor
lib.CW_biquadFilterTDF2_typ_delete.restype                                 = None
lib.CW_biquadFilterTDF2_typ_delete.argtypes                                = [P(biquadFilterTDF2_typ)]
@biquadFilterTDF2_typ.methods.addFunction
def delete(ptr:P(biquadFilterTDF2_typ)):
	return lib.CW_biquadFilterTDF2_typ_delete(ptr)



#method(s)
lib.CW_biquadFilterTDF2_typ_dim.restype                                    = I
lib.CW_biquadFilterTDF2_typ_dim.argtypes                                   = [P(biquadFilterTDF2_typ)]
@biquadFilterTDF2_typ.methods.addFunction
def dim(ptr:biquadFilterTDF2_typ):
	return lib.CW_biquadFilterTDF2_typ_dim(ptr)

lib.CW_biquadFilterTDF2_typ_setCoef_OL0.restype                            = None
lib.CW_biquadFilterTDF2_typ_setCoef_OL0.argtypes                           = [P(biquadFilterTDF2_typ), P(D)]
@biquadFilterTDF2_typ.methods.addFunction
def setCoef(ptr:biquadFilterTDF2_typ, pCoef:P(D)):
	return lib.CW_biquadFilterTDF2_typ_setCoef_OL0(ptr, pCoef)

lib.CW_biquadFilterTDF2_typ_setCoef_OL1.restype                            = None
lib.CW_biquadFilterTDF2_typ_setCoef_OL1.argtypes                           = [P(biquadFilterTDF2_typ), D, D, D, D, D, D]
@biquadFilterTDF2_typ.methods.addFunction
def setCoef(ptr:biquadFilterTDF2_typ, c0:D, c1:D, c2:D, c3:D, c4:D, c5:D):
	return lib.CW_biquadFilterTDF2_typ_setCoef_OL1(ptr, c0, c1, c2, c3, c4, c5)

lib.CW_biquadFilterTDF2_typ_init_OL0.restype                               = P(D)
lib.CW_biquadFilterTDF2_typ_init_OL0.argtypes                              = [P(biquadFilterTDF2_typ)]
@biquadFilterTDF2_typ.methods.addFunction
def init(ptr:biquadFilterTDF2_typ):
	return lib.CW_biquadFilterTDF2_typ_init_OL0(ptr)

lib.CW_biquadFilterTDF2_typ_init_OL1.restype                               = P(D)
lib.CW_biquadFilterTDF2_typ_init_OL1.argtypes                              = [P(biquadFilterTDF2_typ), P(D)]
@biquadFilterTDF2_typ.methods.addFunction
def init(ptr:biquadFilterTDF2_typ, pX:P(D)):
	return lib.CW_biquadFilterTDF2_typ_init_OL1(ptr, pX)

lib.CW_biquadFilterTDF2_typ_update.restype                                 = P(D)
lib.CW_biquadFilterTDF2_typ_update.argtypes                                = [P(biquadFilterTDF2_typ), P(D)]
@biquadFilterTDF2_typ.methods.addFunction
def update(ptr:biquadFilterTDF2_typ, pX:P(D)):
	return lib.CW_biquadFilterTDF2_typ_update(ptr, pX)


