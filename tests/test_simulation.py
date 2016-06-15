import subprocess

import pytest
import numpy as np

from basic_plot.simulation import Simulation

class TestClass:

    def setup_class(self):
        subprocess.call("tar -xzf tests/gs2_test.tar.gz -C tests/.", shell=True)

    def teardown_class(self):
        subprocess.call("rm -rf tests/gs2_test", shell=True)

    @pytest.fixture(scope='function')
    def options(self):
        options = {'ipath':'tests/gs2_test/v/id_1',
                   'opath':'tests/gs2_test/v/id_1'
                  }

        return options

    @pytest.fixture(scope='function')
    def simulation(self, options):
        return Simulation(options)

    def test_get_graph_1d(self, simulation, options):
        options['var'] = 'heat_flux_tot'
        data = simulation.get_graph_data(options)

        assert data['x'].shape[0] == 51
        assert data['y'].shape[0] == 51
