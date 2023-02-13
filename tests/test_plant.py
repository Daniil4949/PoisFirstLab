import unittest
import plants.plant as plant
from animals.herbivores.roe import Roe


class TestPlant(unittest.TestCase):
    flower = plant.Plant()

    def test_value(self):
        self.assertEqual(1, self.flower.value)

    def test_age(self):
        self.assertEqual(0, self.flower.age)

    def test_dying(self):
        self.flower.die()
        self.assertEqual(self.flower, self.flower)


if __name__ == '__main__':
    unittest.main()
