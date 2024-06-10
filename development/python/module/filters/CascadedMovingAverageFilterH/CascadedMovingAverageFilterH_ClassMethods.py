from .CascadedMovingAverageFilterH_ClassMembers import *                        #Class Member definitions
from .CW_CascadedMovingAverageFilterH_ClassMethods import *                     #CWrapper Definitions

#bind methods to cascadedMovingAverageFilter_typ
cascadedMovingAverageFilter_typ.methods.bind(cascadedMovingAverageFilter_typ)

#Redefine cascadedMovingAverageFilter_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class cascadedMovingAverageFilter_typ_typ(OLF_classModifier, cascadedMovingAverageFilter_typ):
	pass

