pathName   = 'CUSP_filters'
moduleName = 'filters'

import os, sys
import importlib

from directoryPaths import paths
sys.path.append(paths.__dict__[f'{pathName}'].pyModule)
module = importlib.import_module(moduleName)

sys.path.append(paths.DataLoader.pyModule)
from DataLoader import indentString
from DataLoader import DataLoader_typ

def displayClass(class_typ):
	print(f'\n{class_typ.__name__}')
	print(indentString('Members:',4))
	print(indentString(str(class_typ()),8))
	print(indentString('Methods:',4))
	print(indentString(class_typ.methods.__str__(),8))
	input('\n\n')

os.system('cls')
for each, object in module.__dict__.items():

	if isinstance(module.__dict__[each], type):
		if issubclass(object, DataLoader_typ):
			displayClass(module.__dict__[each])
	else:
		input(each)