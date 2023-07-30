import unittest

from src.entities.devices.fertilizer.fertilizer_model import FertilizerModel
from src.exceptions.no_fertilizer_exception import NoFertilizerException


class TestFertilizerModel(unittest.TestCase):

    def test_get_available_fertilizer(self):
        fertilizer = FertilizerModel()

        self.assertEqual(fertilizer.get_available_fertilizer(), 500)  # Überprüfen, ob 500 Einheiten Dünger verfügbar sind

    def test_refill(self):
        fertilizer = FertilizerModel()

        fertilizer.refill()
        self.assertEqual(fertilizer.get_available_fertilizer(), 1000)  # Überprüfen, ob der Dünger auf 1000 Einheiten aufgefüllt wurde

    def test_fertilize_with_available_fertilizer(self):
        fertilizer = FertilizerModel()

        fertilizer.fertilize()
        self.assertEqual(fertilizer.get_available_fertilizer(), 499)  # Überprüfen, ob eine Einheit Dünger verbraucht wurde

    def test_fertilize_with_no_available_fertilizer(self):
        fertilizer = FertilizerModel()

        for _ in range(500):
            fertilizer.fertilize()

        with self.assertRaises(NoFertilizerException):
            fertilizer.fertilize()  # Überprüfen, ob eine Ausnahme geworfen wird, wenn kein Dünger mehr verfügbar ist