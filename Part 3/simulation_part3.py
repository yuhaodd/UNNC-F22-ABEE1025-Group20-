# Date of the first creation: 2022-12-01
# This file is for EnergyPlus parametric simulation

import json
import copy
from StaticEplusEngine import run_eplus_model, convert_json_idf

def run_one_simulation_helper(eplus_run_path, idf_path, output_dir,
							parameter_key1, parameter_key2,
							parameter_key1_val, parameter_key2_val):
	"""
	This is a helper function to run one simulation with the changed
	value of the parameter_key
	"""
	######### step 1: convert an IDF file into JSON file #########
	convert_json_idf(eplus_run_path, idf_path)
	epjson_path = idf_path.split('.idf')[0] + '.epJSON'

	######### step 2: load the JSON file into a JSON dict #########
	with open(epjson_path) as epJSON:
		epjson_dict = json.load(epJSON)

	######### step 3: change the JSON dict value #########
	# ['WindowMaterial:SimpleGlazingSystem', 
	#		'SimpleWindow:DOUBLE PANE WINDOW', 
	#		'solar_heat_gain_coefficient']
	inner_dict = epjson_dict
	for x in range(len(parameter_key1)):
		if x < len(parameter_key1) - 1:
			inner_dict = inner_dict[parameter_key1[x]]
	inner_dict[parameter_key1[-1]] = parameter_key1_val

	#['WindowMaterial:SimpleGlazingSystem',
	#		'SimpleWindow:DOUBLE PANE WINDOW', 
	#		'u_factor']
	inner_dict = epjson_dict
	for y in range(len(parameter_key2)):
		if y < len(parameter_key2) - 1:
			inner_dict = inner_dict[parameter_key2[y]]
	inner_dict[parameter_key2[-1]] = parameter_key2_val

	######### step 4: dump the JSON dict to JSON file #########
	with open(epjson_path, 'w') as epjson:
		json.dump(epjson_dict, epjson)

	######### step 5: convert JSON file to IDF file #########
	convert_json_idf(eplus_run_path, epjson_path)

	######### step 6: run simulation #########
	run_eplus_model(eplus_run_path, idf_path, output_dir)


def run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
							parameter_key1, parameter_key2,
							parameter_key1_vals, parameter_key2_vals):
	
	res_dict = {}

	import os
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)

	for parameter_key1_val in parameter_key1_vals:
		for parameter_key2_val in parameter_key2_vals:

			this_output_dir = output_dir + f'/{parameter_key1_val, parameter_key2_val}'
			this_res_path = run_one_simulation_helper(eplus_run_path, idf_path,
								this_output_dir, parameter_key1, parameter_key2, 
								parameter_key1_val, parameter_key2_val)
			res_dict[parameter_key1_val, parameter_key2_val] = this_res_path

	return res_dict



