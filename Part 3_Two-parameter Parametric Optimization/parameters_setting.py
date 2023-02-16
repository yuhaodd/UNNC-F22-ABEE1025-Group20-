# two parameters class for EnergyPlus simulation
class EnergyPlusSetting(object):
    # construction function
    def __init__(self):
        self.keys_list = []
        self.vals_list = []
        self.parameter_name_list = []

    # setter method: set window U/SHGC key and values to list
    def set_keys_vals(self, keys, vals):
        for key, val in zip(keys, vals):
            self.keys_list.append(key)
            self.vals_list.append(val)
            # the last key name
            self.parameter_name_list.append(key[-1])

    # getter method: Get the key and values according to the parameter name
    def get_key_val(self):
        return self.keys_list, self.vals_list

    # Validity of check value
    def check_val_effective(self, valid_range_list):
        # default all vals is valid
        IS_ALL_VALID = True
        for vals, range_of_vals in zip(self.vals_list, valid_range_list):
            for val in vals:
                if val < range_of_vals[0] or val > range_of_vals[1]:
                    IS_ALL_VALID = False
                    return IS_ALL_VALID
        return IS_ALL_VALID