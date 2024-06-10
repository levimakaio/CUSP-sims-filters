from .MovingAverageFilterH_ClassMembers import *                                #Class Member definitions
#====================================  movingAverageFilter_typ  =====================================
#constructor(s)
lib.CW_movingAverageFilter_typ_create_OL0.restype                          = P(movingAverageFilter_typ)
lib.CW_movingAverageFilter_typ_create_OL0.argtypes                         = []
@movingAverageFilter_typ.methods.addFunction
def create():
	return lib.CW_movingAverageFilter_typ_create_OL0()

lib.CW_movingAverageFilter_typ_create_OL1.restype                          = P(movingAverageFilter_typ)
lib.CW_movingAverageFilter_typ_create_OL1.argtypes                         = [I, I]
@movingAverageFilter_typ.methods.addFunction
def create(_windowSize:I, _dim:I):
	return lib.CW_movingAverageFilter_typ_create_OL1(_windowSize, _dim)



#destrutor
lib.CW_movingAverageFilter_typ_delete.restype                              = None
lib.CW_movingAverageFilter_typ_delete.argtypes                             = [P(movingAverageFilter_typ)]
@movingAverageFilter_typ.methods.addFunction
def delete(ptr:P(movingAverageFilter_typ)):
	return lib.CW_movingAverageFilter_typ_delete(ptr)



#method(s)
lib.CW_movingAverageFilter_typ_reset.restype                               = None
lib.CW_movingAverageFilter_typ_reset.argtypes                              = [P(movingAverageFilter_typ)]
@movingAverageFilter_typ.methods.addFunction
def reset(ptr:movingAverageFilter_typ):
	return lib.CW_movingAverageFilter_typ_reset(ptr)

lib.CW_movingAverageFilter_typ_update.restype                              = P(D)
lib.CW_movingAverageFilter_typ_update.argtypes                             = [P(movingAverageFilter_typ), P(D)]
@movingAverageFilter_typ.methods.addFunction
def update(ptr:movingAverageFilter_typ, pX:P(D)):
	return lib.CW_movingAverageFilter_typ_update(ptr, pX)


