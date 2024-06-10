from .BiquadFilterH_ClassMembers        import *                                #Class Member definitions
from .CW_BiquadFilterH_ClassMethods     import *                                #CWrapper Definitions

#bind methods to biquadFilterTDF2_typ
biquadFilterTDF2_typ.methods.bind(biquadFilterTDF2_typ)

#Redefine biquadFilterTDF2_typ class definition with overloaded function modifier
#so that constructors and destructors defined in C fucntions work properly
#when mixed with constructors handled in python
class biquadFilterTDF2_typ_typ(OLF_classModifier, biquadFilterTDF2_typ):
	pass

