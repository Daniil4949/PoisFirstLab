import unittest
import plants.plant as plant
from animals.herbivores.roe import Roe
from animals.herbivores.rabbit import Rabbit


class TestRoe(unittest.TestCase):
    roe = Roe()

    def test_gender(self):
        self.assertEqual("male", self.roe.gender)

    def test_age(self):
        self.assertEqual(0, self.roe.age)

    def test_dying(self):
        self.roe.die()
        self.assertEqual(self.roe, self.roe)

    def test_multipy(self):
        male_roe = Roe(gender="male")
        self.assertEqual(self.roe.multipy(male_roe), None)


class TestRabbit(unittest.TestCase):
    rabbit = Rabbit()

    def test_gender(self):
        self.assertEqual("male", self.rabbit.gender)

    def test_age(self):
        self.assertEqual(0, self.rabbit.age)

    def test_dying(self):
        self.rabbit.die()
        self.assertEqual(self.rabbit, self.rabbit)

    def test_multipy(self):
        male_rabbit = Roe(gender="male")
        self.assertEqual(self.rabbit.multipy(male_rabbit), None)


if __name__ == "__main__":
    unittest.main()

