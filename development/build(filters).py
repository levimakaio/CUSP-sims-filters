#==================================================================================================
# This file needs to be called from cmd line after the build environment has been set up
# with either:
#
#                vcvars64.bat
#                vcvars32.bat
#
# depending on if you are building a 32 or 64 bit build. These .bat files are typically found 
# in C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build, but the
# location may vary depending on how VS was installed in the system.  
#
# a traget for the build (32, 64) should be passed to the script and the optional arguments:
#
#                '-clean'
#                '-rebuild'
#
# may be used.  if both flags are present the system will rebuild.
#
#==================================================================================================
import sys
import shutil

from directoryPaths import paths

sys.path.append(paths.CompileScripts.pyModule)
from CompileScripts import C_complie_typ

#==================================================================================================

pathName        = 'CUSP_filters'
projectName     = 'filters'
target          = sys.argv[1]
build           =  C_complie_typ(Name=f'{projectName}_{target}', rootDir=paths.__dict__[f'{pathName}'].C_Dir, target=target)

#inputPaths
build.paths.inputs.SRC = [
                          paths.CuspGantry.Filters,
                          paths.__dict__[f'{pathName}'].C_SRC,
                          paths.__dict__[f'{pathName}'].CWrapper_SRC]

build.paths.inputs.INC = [paths.__dict__[f'{pathName}'].C_include,
                          paths.__dict__[f'{pathName}'].CWrapper_include,
                          paths.__dict__['CUSP_sims'].C_include]

build.paths.inputs.LIB = []

#outputPaths
build.paths.outputs.DLL = paths.__dict__[f'{pathName}'].C_bin
build.paths.outputs.LIB = paths.__dict__[f'{pathName}'].C_bin
build.paths.outputs.OBJ = paths.__dict__[f'{pathName}'].C_obj
build.paths.outputs.DEP = paths.__dict__[f'{pathName}'].C_dep

build.LinkerFlags = [fr'/DEF:{paths.__dict__[f'{pathName}'].C_def}\\export.def']

if '-rebuild' in sys.argv:
	build.rebuild()
	sys.exit()

if '-clean' in sys.argv:
	build.clean()
	sys.exit()

build.build()
