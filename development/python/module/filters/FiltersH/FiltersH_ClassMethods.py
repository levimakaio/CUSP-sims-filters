from .FiltersH_ClassMembers             import *                                #Class Member definitions
from .CW_FiltersH_ClassMethods          import *                                #CWrapper Definitions

#bind methods to AS_RollingBuffer_typ
AS_RollingBuffer_typ.methods.bind(AS_RollingBuffer_typ)

#Redefine AS_RollingBuffer_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class AS_RollingBuffer_typ_typ(OLF_classModifier, AS_RollingBuffer_typ):
	pass

#bind methods to AS_MovingAverageFilter_typ
AS_MovingAverageFilter_typ.methods.bind(AS_MovingAverageFilter_typ)

#Redefine AS_MovingAverageFilter_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class AS_MovingAverageFilter_typ_typ(OLF_classModifier, AS_MovingAverageFilter_typ):
	pass

#bind methods to AS_CMAFilter_typ
AS_CMAFilter_typ.methods.bind(AS_CMAFilter_typ)

#Redefine AS_CMAFilter_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class AS_CMAFilter_typ_typ(OLF_classModifier, AS_CMAFilter_typ):
	pass

#bind methods to AS_BiquadFilter_typ
AS_BiquadFilter_typ.methods.bind(AS_BiquadFilter_typ)

#Redefine AS_BiquadFilter_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class AS_BiquadFilter_typ_typ(OLF_classModifier, AS_BiquadFilter_typ):
	pass

#bind methods to AS_SOSFilter_typ
AS_SOSFilter_typ.methods.bind(AS_SOSFilter_typ)

#Redefine AS_SOSFilter_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class AS_SOSFilter_typ_typ(OLF_classModifier, AS_SOSFilter_typ):
	pass

