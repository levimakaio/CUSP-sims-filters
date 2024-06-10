from .SOSFilterH_ClassMembers           import *                                #Class Member definitions
from .CW_SOSFilterH_ClassMethods        import *                                #CWrapper Definitions

#bind methods to SOSFilterTDF2_typ
SOSFilterTDF2_typ.methods.bind(SOSFilterTDF2_typ)

#Redefine SOSFilterTDF2_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class SOSFilterTDF2_typ_typ(OLF_classModifier, SOSFilterTDF2_typ):
	pass

