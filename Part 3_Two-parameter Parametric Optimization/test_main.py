from parametric_simulation import run_one_parameter_parametric, run_two_parameter_parametric
from parameters_setting import EnergyPlusSetting
import csv

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'

# set two parameters
first_parameter_key = ['WindowMaterial:SimpleGlazingSystem',
                 'SimpleWindow:DOUBLE PANE WINDOW',
                 'solar_heat_gain_coefficient']

first_parameter_vals = [i / 100 for i in range(25, 75, 5)]

second_parameter_key = ['WindowMaterial:SimpleGlazingSystem',
                 'SimpleWindow:DOUBLE PANE WINDOW',
                 'u_factor']

second_parameter_vals = [i / 10 for i in range(10, 25, 1)]

energyPlusSetting = EnergyPlusSetting()
energyPlusSetting.set_keys_vals(keys=[first_parameter_key, second_parameter_key]
                                , vals=[first_parameter_vals, second_parameter_vals])

is_valid = energyPlusSetting.check_val_effective([(0.25, 0.75), (1.0, 2.5)])

if is_valid:
    keys, values = energyPlusSetting.get_key_val()
    key_names = energyPlusSetting.parameter_name_list

    output_dir = 'result'
    output_paths = run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                                keys[0], values[0], keys[1], values[1])

    max_temperature = 0.0
    max_setting_val = ''
    # read all csv result and analyse the max temperature corresponding the max setting val
    for parameter in output_paths.keys():
        print(output_paths[parameter])
        file = open('./' + output_paths[parameter], 'r')
        csv_reader = csv.reader(file)

        # indoor air temperature list with this parameter
        indoor_temperature = []
        line_number = 0
        for line in csv_reader:
            if line_number > 0:
                indoor_temperature.append(float(line[8]))
            line_number += 1

        if len(indoor_temperature) != 0:
            mean_temperature = sum(indoor_temperature) / len(indoor_temperature)
        else:
            mean_temperature = 0.0

        if mean_temperature > max_temperature:
            max_temperature = mean_temperature
            max_setting_val = parameter

    params_vals = max_setting_val.split('_')
    print('Max setting val is: window U=', params_vals[0], ' and window SHGC=', params_vals[1])



