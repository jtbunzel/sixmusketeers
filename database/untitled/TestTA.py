from django.test import TestCase
from Skeleton_Classes.TA import *

class AnimalTestCase(TestCase):
    def setUp(self):
        TA.objects.create(name="lion", sound="roar")
        TA.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = TA.objects.get(name="lion")
        cat = TA.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

if __name__ == '__main__':
    unittest.main()
