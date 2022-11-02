# Date of the first creation: 2022-11-01
# This file is for running functions
from parametric_simulation import run_one_parameter_parametric
from post_processor import plot_1D_results
import numpy

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
output_dir = 'param_exp_1'
parameter_key = ['WindowMaterial:SimpleGlazingSystem','SimpleWindow:DOUBLE PANE WINDOW','solar_heat_gain_coefficient']
parameter_vals = [(int(i*100)/100) for i in numpy.arange(0.25,0.75,0.02)]
plot_column_name = 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep) '
y_axis_title = 'Indoor Air Temperature (C)'
plot_title = 'Simulation of Indoor Air Temperature vs. SHGC'

output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key,parameter_vals)
print(output_paths)
plot_1D_results(output_paths,plot_column_name,y_axis_title,plot_title)
