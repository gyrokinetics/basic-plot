from basic-plot.simulation import Simulation
import pytest

class TestClass:

    @pytest.fixture(scope='function')
    def prius(self):
        return Simulation()


