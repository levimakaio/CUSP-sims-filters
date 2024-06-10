from .rollingBufferH_ClassMembers       import *                                #Class Member definitions
#=======================================  rollingBuffer_typ  ========================================
#constructor(s)
lib.CW_rollingBuffer_typ_create_OL0.restype                                = P(rollingBuffer_typ)
lib.CW_rollingBuffer_typ_create_OL0.argtypes                               = []
@rollingBuffer_typ.methods.addFunction
def create():
	return lib.CW_rollingBuffer_typ_create_OL0()

lib.CW_rollingBuffer_typ_create_OL1.restype                                = P(rollingBuffer_typ)
lib.CW_rollingBuffer_typ_create_OL1.argtypes                               = [LU, LU]
@rollingBuffer_typ.methods.addFunction
def create(dim:LU, bufferSize:LU):
	return lib.CW_rollingBuffer_typ_create_OL1(dim, bufferSize)

lib.CW_rollingBuffer_typ_create_OL2.restype                                = P(rollingBuffer_typ)
lib.CW_rollingBuffer_typ_create_OL2.argtypes                               = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def create(toCopy:P(rollingBuffer_typ)):
	return lib.CW_rollingBuffer_typ_create_OL2(toCopy)



#destrutor
lib.CW_rollingBuffer_typ_delete.restype                                    = None
lib.CW_rollingBuffer_typ_delete.argtypes                                   = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def delete(ptr:P(rollingBuffer_typ)):
	return lib.CW_rollingBuffer_typ_delete(ptr)



#method(s)
lib.CW_rollingBuffer_typ_getData.restype                                   = D
lib.CW_rollingBuffer_typ_getData.argtypes                                  = [P(rollingBuffer_typ), LU, L]
@rollingBuffer_typ.methods.addFunction
def getData(ptr:rollingBuffer_typ, signalIndex:LU, bufferIndexFromCurrent:L):
	return lib.CW_rollingBuffer_typ_getData(ptr, signalIndex, bufferIndexFromCurrent)

lib.CW_rollingBuffer_typ_getDataPointer.restype                            = P(D)
lib.CW_rollingBuffer_typ_getDataPointer.argtypes                           = [P(rollingBuffer_typ), L]
@rollingBuffer_typ.methods.addFunction
def getDataPointer(ptr:rollingBuffer_typ, bufferIndexFromCurrent:L):
	return lib.CW_rollingBuffer_typ_getDataPointer(ptr, bufferIndexFromCurrent)

lib.CW_rollingBuffer_typ_setData.restype                                   = B
lib.CW_rollingBuffer_typ_setData.argtypes                                  = [P(rollingBuffer_typ), LU, L, D]
@rollingBuffer_typ.methods.addFunction
def setData(ptr:rollingBuffer_typ, signalIndex:LU, bufferIndexFromCurrent:L, value:D):
	return lib.CW_rollingBuffer_typ_setData(ptr, signalIndex, bufferIndexFromCurrent, value)

lib.CW_rollingBuffer_typ_getBufferSize.restype                             = LU
lib.CW_rollingBuffer_typ_getBufferSize.argtypes                            = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def getBufferSize(ptr:rollingBuffer_typ):
	return lib.CW_rollingBuffer_typ_getBufferSize(ptr)

lib.CW_rollingBuffer_typ_dim.restype                                       = LU
lib.CW_rollingBuffer_typ_dim.argtypes                                      = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def dim(ptr:rollingBuffer_typ):
	return lib.CW_rollingBuffer_typ_dim(ptr)

lib.CW_rollingBuffer_typ_getNumValid.restype                               = LU
lib.CW_rollingBuffer_typ_getNumValid.argtypes                              = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def getNumValid(ptr:rollingBuffer_typ):
	return lib.CW_rollingBuffer_typ_getNumValid(ptr)

lib.CW_rollingBuffer_typ_incrementIndex.restype                            = P(D)
lib.CW_rollingBuffer_typ_incrementIndex.argtypes                           = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def incrementIndex(ptr:rollingBuffer_typ):
	return lib.CW_rollingBuffer_typ_incrementIndex(ptr)

lib.CW_rollingBuffer_typ_incrementData.restype                             = B
lib.CW_rollingBuffer_typ_incrementData.argtypes                            = [P(rollingBuffer_typ), P(D)]
@rollingBuffer_typ.methods.addFunction
def incrementData(ptr:rollingBuffer_typ, pValues:P(D)):
	return lib.CW_rollingBuffer_typ_incrementData(ptr, pValues)

lib.CW_rollingBuffer_typ_copy.restype                                      = B
lib.CW_rollingBuffer_typ_copy.argtypes                                     = [P(rollingBuffer_typ), P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def copy(ptr:rollingBuffer_typ, toCopy:P(rollingBuffer_typ)):
	return lib.CW_rollingBuffer_typ_copy(ptr, toCopy)

lib.CW_rollingBuffer_typ_reset.restype                                     = None
lib.CW_rollingBuffer_typ_reset.argtypes                                    = [P(rollingBuffer_typ)]
@rollingBuffer_typ.methods.addFunction
def reset(ptr:rollingBuffer_typ):
	return lib.CW_rollingBuffer_typ_reset(ptr)


