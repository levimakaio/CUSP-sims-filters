from .MovingAverageFilterH_ClassMembers import *                                #Class Member definitions
from .CW_MovingAverageFilterH_ClassMethods import *                             #CWrapper Definitions

#bind methods to movingAverageFilter_typ
movingAverageFilter_typ.methods.bind(movingAverageFilter_typ)

#Redefine movingAverageFilter_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class movingAverageFilter_typ_typ(OLF_classModifier, movingAverageFilter_typ):
	pass

