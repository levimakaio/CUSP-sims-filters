from .CascadedMovingAverageFilterH_ClassMembers import *                        #Class Member definitions
#================================  cascadedMovingAverageFilter_typ  =================================
#constructor(s)
lib.CW_cascadedMovingAverageFilter_typ_create_OL0.restype                  = P(cascadedMovingAverageFilter_typ)
lib.CW_cascadedMovingAverageFilter_typ_create_OL0.argtypes                 = []
@cascadedMovingAverageFilter_typ.methods.addFunction
def create():
	return lib.CW_cascadedMovingAverageFilter_typ_create_OL0()

lib.CW_cascadedMovingAverageFilter_typ_create_OL1.restype                  = P(cascadedMovingAverageFilter_typ)
lib.CW_cascadedMovingAverageFilter_typ_create_OL1.argtypes                 = [I, I, P(I)]
@cascadedMovingAverageFilter_typ.methods.addFunction
def create(_numFilteres:I, _dim:I, pWindowSize:P(I)):
	return lib.CW_cascadedMovingAverageFilter_typ_create_OL1(_numFilteres, _dim, pWindowSize)



#destrutor
lib.CW_cascadedMovingAverageFilter_typ_delete.restype                      = None
lib.CW_cascadedMovingAverageFilter_typ_delete.argtypes                     = [P(cascadedMovingAverageFilter_typ)]
@cascadedMovingAverageFilter_typ.methods.addFunction
def delete(ptr:P(cascadedMovingAverageFilter_typ)):
	return lib.CW_cascadedMovingAverageFilter_typ_delete(ptr)



#method(s)
lib.CW_cascadedMovingAverageFilter_typ_reset.restype                       = None
lib.CW_cascadedMovingAverageFilter_typ_reset.argtypes                      = [P(cascadedMovingAverageFilter_typ)]
@cascadedMovingAverageFilter_typ.methods.addFunction
def reset(ptr:cascadedMovingAverageFilter_typ):
	return lib.CW_cascadedMovingAverageFilter_typ_reset(ptr)

lib.CW_cascadedMovingAverageFilter_typ_update.restype                      = P(D)
lib.CW_cascadedMovingAverageFilter_typ_update.argtypes                     = [P(cascadedMovingAverageFilter_typ), P(D)]
@cascadedMovingAverageFilter_typ.methods.addFunction
def update(ptr:cascadedMovingAverageFilter_typ, pX:P(D)):
	return lib.CW_cascadedMovingAverageFilter_typ_update(ptr, pX)


