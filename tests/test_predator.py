import unittest
from animals.herbivores.roe import Roe
from animals.herbivores.rabbit import Rabbit
from animals.predators.bear import Bear
from animals.predators.wolf import Wolf
from animals.predators.fox import Fox


class TestFox(unittest.TestCase):
    fox = Fox()

    def test_gender(self):
        self.assertEqual("female", self.fox.gender)

    def test_age(self):
        self.assertEqual(0, self.fox.age)

    def test_dying(self):
        self.fox.die()
        self.assertEqual(self.fox, self.fox)

    def test_multipy(self):
        female_fox = Fox(gender="female")
        self.assertEqual(self.fox.multipy(female_fox), None)


class TestBear(unittest.TestCase):
    bear = Bear()

    def test_gender(self):
        self.assertEqual("male", self.bear.gender)

    def test_age(self):
        self.assertEqual(0, self.bear.age)

    def test_dying(self):
        self.bear.die()
        self.assertEqual(self.bear, self.bear)

    def test_multipy(self):
        male_bear = Bear(gender="male")
        self.assertEqual(self.bear.multipy(male_bear), None)


class TestWolf(unittest.TestCase):
    wolf = Wolf()


if __name__ == "__main__":
    unittest.main()
