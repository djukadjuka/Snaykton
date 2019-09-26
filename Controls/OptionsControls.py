import sys
import os
import pickle
from Models.OptionsModel import Options


__SNAYKTON_OPTIONS_FILENAME = os.getcwd() + '\\snaykton_options.options'


def load_options():
    # -- Check if the file doesn't exists
    if os.path.isfile(__SNAYKTON_OPTIONS_FILENAME) is not True:
        # -- Create default options file
        ops = Options()
        # -- Open the default file and dump the options file
        with open(__SNAYKTON_OPTIONS_FILENAME, 'wb') as snaykton_options_file:
            pickle.dump(ops, snaykton_options_file)
        return ops

    # -- Options file found and can be opened and read
    with open(__SNAYKTON_OPTIONS_FILENAME, 'rb') as snaykton_options_file:
        ops = pickle.load(snaykton_options_file)
        return ops


def save_options(ops: Options):
    if type(ops) is not Options:
        raise TypeError('Only objects that are of type \'Options\' can be saved using this method')
    with open(__SNAYKTON_OPTIONS_FILENAME, 'wb') as snaykton_options_file:
        pickle.dump(ops, snaykton_options_file)

