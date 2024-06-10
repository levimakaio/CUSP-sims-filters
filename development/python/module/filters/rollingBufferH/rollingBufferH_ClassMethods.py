from .rollingBufferH_ClassMembers       import *                                #Class Member definitions
from .CW_rollingBufferH_ClassMethods    import *                                #CWrapper Definitions

#bind methods to rollingBuffer_typ
rollingBuffer_typ.methods.bind(rollingBuffer_typ)

#Redefine rollingBuffer_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class rollingBuffer_typ_typ(OLF_classModifier, rollingBuffer_typ):
	pass

