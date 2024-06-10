#==================================================================================================
# complier to go from c.h to python header.
#
#    cmd line usage:
#
#        python createModule(*).py [optional flags]
#
#    flags:
#        -vl = Verbose (lexer)
#        -va = Verbose (analyser)
#        -vp = Verbose (parser)
#        -v  = Verbose (all)
#
#==================================================================================================
import os, sys

try:
	from directoryPaths import paths
	sys.path.append(paths.PYH.pyModule);
	sys.path.append(paths.projectTemplates.pyModule)
except:
	pass

from PYH              import createPyModule_typ
from projectTemplates import NewProject

if __name__ == "__main__":

	pathName    = 'CUSP_filters'
	projectName = 'filters'

	#ensure that all folders exist
	project = NewProject(projectName, os.path.dirname(paths.__dict__[f'{pathName}'].root))
	project.createFolderTree()

	#path to include files
	c_headerPathList     = [paths.CuspGantry.Filters]

	#files to Exclude or include
	method   = 'exclude' #. 'include'
	fileList = [
				'digitalFilters.h',
				'CW_rollingBuffer_typ.h',
				'CW_movingAverageFilter_typ.h',
				'CW_cascadedMovingAverageFilter_typ.h',
				'CW_biquadFilterTDF2_typ.h',
				'CW_SOSFilterTDF2_typ.h'
	]

	# pyModule Initilization order,
	# any module not specified will be initilized aphabetically
	init_Order = []

	#create a module object
	module                      = createPyModule_typ()
	module.projectName          = projectName
	module.dllPathVar           = fr'paths.CUSP_sims.Library'
	module.dllName              = fr'{module.projectName}'
	module.outputPath           = fr'{paths.__dict__[f'{pathName}'].pyModule}\\{module.projectName}'
	module.cfgPath              = fr'{module.outputPath}\_cfg_'
	module.CPPWrapperOutputPath = fr'{paths.__dict__[f'{pathName}'].CWrapper_SRC}'
	module.CHWrapperOutputPath  = fr'{paths.__dict__[f'{pathName}'].CWrapper_include}'

	#flag to create cWrapper files from cpp class methods
	module.createWrappers = False

#	hack in an extra file
	module.setFlags(sys.argv)
	module.PYH_SubmoduleDict.create(paths=[r'C:\Users\levim\Desktop\gitHub\Loupe\CUSP\BoeingCUSP\CuspGantry\Temp\Includes'], filesList=['Filters.h'], method='include')

	#run the module
	module.run(flags=sys.argv, paths=c_headerPathList, filesList=fileList, method = method, init_Order=init_Order)

	sys.exit()