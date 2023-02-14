# Date of the first creation: 2022-12-1
# This file is for running simulation_part3.py

from simulation_part3 import run_two_parameter_parametric

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
output_dir = 'param_res'

# OOP Structure
class Parameter_key():
	def __init__(parameter_key1, parameter_key2):
		self._parameter_key1 = parameter_key1
		self._parameter_key2 = parameter_key2

	# getter
	@property
	def parameter_key1(self):
		return self._parameter_key1

	@property
	def parameter_key2(self):
		return self._parameter_key2

	# setter
	@parameter_key1.setter
	def parameter_key1(self, new_parameter_key1):
		if (type(new_parameter_key1) is float ):
			self._parameter_key1 = new_parameter_key1
		else:
			print('Wrong output')

	@parameter_key2.setter
	def parameter_key2(self, new_parameter_key2):
		if (type(new_parameter_key2) is float ):
			self._parameter_key2 = new_parameter_key2
		else:
			print('Wrong output')

parameter_key1 = ['WindowMaterial:SimpleGlazingSystem',
					'SimpleWindow:DOUBLE PANE WINDOW', 
					'solar_heat_gain_coefficient']
parameter_key2 = ['WindowMaterial:SimpleGlazingSystem',
					'SimpleWindow:DOUBLE PANE WINDOW', 
					'u_factor']

parameter_key1_vals = [x/100 for x in range(25, 75, 10)]
parameter_key2_vals = [y/10 for y in range(1, 5, 1)]

output_paths = run_two_parameter_parametric(eplus_run_path, 
							idf_path, output_dir,
							parameter_key1, parameter_key2,
							parameter_key1_vals, parameter_key2_vals)

"""
import numpy as np
arr = np.array(output_paths)
optimal = np.average(arr)
print(optimal)

"""

print(output_paths)







