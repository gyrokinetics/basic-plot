import pytest
import numpy as np

from basic_plot.simulation import Simulation

class TestClass:

    @pytest.fixture(scope='function')
    def options(self):
        options = {'ipath':'test_run/v/id_1',
                   'opath':'test_run/v/id_1'
                  }

        return options

    @pytest.fixture(scope='function')
    def simulation(self, options):
        return Simulation(options)

    def test_get_graph_1d(self, simulation):
        options['var'] = 'heat_flux_tot'
        data = simulation.get_graph_data(options)

        assert data['x'].shape[0] == 51
        assert data['y'].shape[0] == 51
