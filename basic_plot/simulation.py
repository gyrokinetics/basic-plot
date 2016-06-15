"""
.. class:: Simulation
   :platform: Unix
   :synopsis: Simulation class representing a single GS2 simulation.

"""

import os

import numpy as np
from netCDF4 import Dataset


class Simulation(object):
    """ Represents a single GS2 simulation."""

    def __init__(self, options):
        """
        Instantiate the Simulation object.

        Parameters
        ----------

        options : dict
            Dictionary of options. The options required for initialization are
            documented below.
        'ifile' : str, optional
            Path to GS2 input file. If not specified, need ipath.
        'ipath' : str, optional
            Path to GS2 run directory. If not specified, need ifile.
        'opath' : str, optional
            Path where output should be written. Default will be in the GS2 run
            folder determined either from 'ifile' or 'ipath'.
        """

        if 'ifile' in options:
            self.nc_file = Dataset(options['ifile'], 'r')

            if 'opath' not in options:
                slash_idx = options['ifile'].rfind('/')
                options['opath'] = options['ifile'][:slash_idx]

        elif 'ipath' in options:
            input_file_path = self.find_gs2_input_file(options['ipath'])
            self.nc_file = Dataset(input_file_path, 'r')

            if 'opath' not in options:
                options['opath'] = options['ipath']

    def find_gs2_input_file(self, run_dir_path):
        """
        Find the GS2 output file given the path to the run directory.

        Parameters
        ----------

        run_dir_path : str
            Path to the directory containing the GS2 output file.

        Returns
        -------

        str
            Full path to the GS2 output file.

        """
        files = os.listdir(run_dir_path)

        for f in files:
            if f.find('.out.nc') != -1:
                return run_dir_path + '/' + f

    def run(self, options):
        """Run some commands."""
        pass

    def plot(self, options):
        """Plot data from a GS2 output file."""
        graph_data = get_graph_data(options)

    def write(self, options):
        """Write GS2 data to a file in the output directory."""
        pass

    def return_results(self, options):
        """Return results to the caller."""
        pass

    def get_graph_data(self, options):
        """
        Read data for an individual graph.

        Returns:
        --------

        graph_data : dict
            A dictionary containing all the data for the graph specified in
            the options dictionary.

        """
        graph_data = {}

        var_obj = self.nc_file.variables[options['var']]
        dims = var_obj.dimensions

        graph_data['x'] = self.nc_file.variables[dims[0]][:]
        graph_data['y'] = var_obj[:]

        return graph_data
