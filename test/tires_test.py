import unittest
from tire import Tire
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime


class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire = Carrigan([0,0,0,.98])
        self.assertTrue(tire.needs_service())
    def test_tires_should_not_be_serviced(self):
        tire = Carrigan([.5,.5,0,.89])
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire = Octoprime([.8,.8,.8,.8])
        self.assertTrue(tire.needs_service())
    def test_tires_should_not_be_serviced(self):
        tire = Octoprime([.2,0,.1,0])
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()