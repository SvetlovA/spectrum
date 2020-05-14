import unittest
from src.algorithms.implementation.haar_algorithm import HaarAlgotithm


class TestHaarAlgorithm(unittest.TestCase):

    def test_direct_transform_happy_path(self):
        input_signal = [220, 211, 212, 218, 217, 214, 210, 202]
        algorithm = HaarAlgotithm()

        expected_results = [4.5, -3, 1.5, 4, 0.25, 4.75, 2.25, 213]
        actual_result = algorithm.direct_transform(input_signal)

        self.assertEqual(expected_results, actual_result)

    def test_direct_transform_happy_path_one_element(self):
        input_signal = [220]
        algorithm = HaarAlgotithm()

        expected_results = [220]
        actual_result = algorithm.direct_transform(input_signal)

        self.assertEqual(expected_results, actual_result)

    def test_direct_transform_happy_path_empty_array(self):
        input_signal = []
        algorithm = HaarAlgotithm()

        expected_results = []
        actual_result = algorithm.direct_transform(input_signal)

        self.assertEqual(expected_results, actual_result)

    def test_direct_transform_none(self):
        input_signal = None
        algorithm = HaarAlgotithm()

        with self.assertRaises(TypeError):
            algorithm.direct_transform(input_signal)


if __name__ == "__main__":
    unittest.main()
