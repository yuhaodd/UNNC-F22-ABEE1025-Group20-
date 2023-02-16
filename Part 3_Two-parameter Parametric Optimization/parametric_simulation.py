# Date of the first creation: 2022-10-25
# This file is for EnergyPlus parametric simulation
import os
import json
import copy
from StaticEplusEngine import run_eplus_model, convert_json_idf


def run_one_simulation_helper(eplus_run_path, idf_path, output_dir,
                              parameter_key, parameter_val):
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
    #			 				'SimpleWindow:DOUBLE PANE WINDOW',
    #			 				'solar_heat_gain_coefficient']
    inner_dict = epjson_dict
    for i in range(len(parameter_key)):
        if i < len(parameter_key) - 1:
            inner_dict = inner_dict[parameter_key[i]]
    inner_dict[parameter_key[-1]] = parameter_val

    ######### step 4: dump the JSON dict to JSON file #########
    with open(epjson_path, 'w') as epjson:
        json.dump(epjson_dict, epjson)

    ######### step 5: convert JSON file to IDF file #########
    convert_json_idf(eplus_run_path, epjson_path)

    ######### step 6: run simulation #########
    run_eplus_model(eplus_run_path, idf_path, output_dir)
    return output_dir + '/eplusout.csv'


def run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                 parameter_key, parameter_vals):
    res_dict = {}
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    for parameter_val in parameter_vals:
        this_output_dir = output_dir + f'/{parameter_val}'
        this_res_path = run_one_simulation_helper(eplus_run_path, idf_path,
                                                  this_output_dir, parameter_key,
                                                  parameter_val)
        res_dict[parameter_val] = this_res_path

    return res_dict  # TO-DO!


def run_two_simulation_helper(eplus_run_path, idf_path, output_dir,
                              parameter_key1, parameter_val1,
                              parameter_key2, parameter_val2):
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
    #			 				'SimpleWindow:DOUBLE PANE WINDOW',
    #			 				'solar_heat_gain_coefficient']
    inner_dict = epjson_dict
    for i in range(len(parameter_key1)):
        if i < len(parameter_key1) - 1:
            inner_dict = inner_dict[parameter_key1[i]]

    inner_dict[parameter_key1[-1]] = parameter_val1
    inner_dict[parameter_key2[-1]] = parameter_val2

    ######### step 4: dump the JSON dict to JSON file #########
    with open(epjson_path, 'w') as epjson:
        json.dump(epjson_dict, epjson)

    ######### step 5: convert JSON file to IDF file #########
    convert_json_idf(eplus_run_path, epjson_path)

    ######### step 6: run simulation #########
    run_eplus_model(eplus_run_path, idf_path, output_dir)
    return output_dir + '/eplusout.csv'


def run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                 parameter_key1, parameter_vals1,
                                 parameter_key2, parameter_vals2):
    res_dict = {}
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    for parameter_val1 in parameter_vals1:
        for parameter_val2 in parameter_vals2:
            sub_path = str(parameter_val1) + '_' + str(parameter_val2)
            this_output_dir = output_dir + f'/{sub_path}'
            this_res_path = run_two_simulation_helper(eplus_run_path,
                                                      idf_path,
                                                      this_output_dir,
                                                      parameter_key1,
                                                      parameter_val1,
                                                      parameter_key2,
                                                      parameter_val2)
            res_dict[sub_path] = this_res_path

    return res_dict

    """
	Args:
	----------
	eplus_run_path: string type, the path to EnergyPlus executable
	idf_path: string type, the path to EnergyPlus IDF file
	output_dir: string type, the directory to store all simulation results.
	 			Note: the simulation results from different simulations 
	 					must not overwrite each other. 
	parameter_key: list type, each item in the list represents the key
				 at different levels.
				 For example, ['WindowMaterial:SimpleGlazingSystem', 
				 				'SimpleWindow:DOUBLE PANE WINDOW', 
				 				'solar_heat_gain_coefficient'] 
				 means (assume json_model is the EnergyPlus JSON model) 
				 json_model['WindowMaterial:SimpleGlazingSystem']\
				 			['SimpleWindow:DOUBLE PANE WINDOW']\
				 			['solar_heat_gain_coefficient'] 
				 is the innermost key to be accessed.
	parameter_vals: list type, each item in the list is corresponding to
					the one simulation in the parametric simulation. 
					For example, [0.1, 0.2, 0.3, 0.4, 0.5] 
					means five simulations will be run, 
					and the first simulation will change the value 
					of the key in parameter_key to 0.1, 
					the second will be 0.2, etc. 

	Output:
	---------- 
	output_paths: dict type, the key in the dict is the parameter 
					values corresponding to parameter_vals, 
					and the value is the path to the corresponding 
					eplusout.csv file. 
				For example, {0.1: ‘param_sim_res/run_1/eplusout.csv’,
				0.2: ‘param_sim_res/run_2/eplusout.csv’,
				0.3: ‘param_sim_res/run_3/eplusout.csv’,
				0.4: ‘param_sim_res/run_4/eplusout.csv’,
				0.5: ‘param_sim_res/run_5/eplusout.csv’}

	"""

# return None # TO-DO!
