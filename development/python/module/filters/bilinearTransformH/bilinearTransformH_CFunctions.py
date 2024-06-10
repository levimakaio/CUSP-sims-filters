from .bilinearTransformH_ClassMethods   import *                                #Member Definitions

#==============================  bilinearTransform_2ndOrderConjugate  ===============================
lib.bilinearTransform_2ndOrderConjugate.restype                            = B
lib.bilinearTransform_2ndOrderConjugate.argtypes                           = [D, D, D, D, D, P(D), P(D)]
def bilinearTransform_2ndOrderConjugate(x:D, y:D, ka:D, T:D, omega:D, pCoefOut:P(D), gainOut:P(D)):
	return lib.bilinearTransform_2ndOrderConjugate(x, y, ka, T, omega, pCoefOut, gainOut)

