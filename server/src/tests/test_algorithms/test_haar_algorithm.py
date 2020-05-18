import unittest
from src.algorithms.implementation.haar_algorithm import HaarAlgotithm


class TestHaarAlgorithm(unittest.TestCase):

    def test_direct_transform_happy_path(self):
        input_signal = [220, 211, 212, 218, 217, 214, 210, 202]
        algorithm = HaarAlgotithm()

        expected_result = [4.5, -3, 1.5, 4, 0.25, 4.75, 2.25, 213]
        actual_result = algorithm.direct_transform(input_signal)

        self.assertEqual(expected_result, actual_result)

    def test_direct_transform_happy_path_one_element(self):
        input_signal = [220]
        algorithm = HaarAlgotithm()

        expected_result = [220]
        actual_result = algorithm.direct_transform(input_signal)

        self.assertEqual(expected_result, actual_result)

    def test_direct_transform_happy_path_empty_array(self):
        input_signal = []
        algorithm = HaarAlgotithm()

        expected_result = []
        actual_result = algorithm.direct_transform(input_signal)

        self.assertEqual(expected_result, actual_result)

    def test_direct_transform_none(self):
        input_signal = None
        algorithm = HaarAlgotithm()

        with self.assertRaises(TypeError):
            algorithm.direct_transform(input_signal)

    def test_direct_transform_non_grade_two(self):
        input_signal = [220, 211, 212]
        algorithm = HaarAlgotithm()

        with self.assertRaises(Exception):
            algorithm.direct_transform(input_signal)

    def test_inverse_transform_happy_path(self):
        input_signal = [4.5, -3, 1.5, 4, 0.25, 4.75, 2.25, 213]
        algorithm = HaarAlgotithm()

        expected_result = [220, 211, 212, 218, 217, 214, 210, 202]
        actual_result = algorithm.inverse_transform(input_signal)

        self.assertEqual(expected_result, actual_result)

    def test_inverse_transform_happy_path_one_element(self):
        input_signal = [220]
        algorithm = HaarAlgotithm()

        expected_result = [220]
        actual_result = algorithm.inverse_transform(input_signal)

        self.assertEqual(expected_result, actual_result)

    def test_inverse_transform_happy_path_empty_array(self):
        input_signal = []
        algorithm = HaarAlgotithm()

        expected_result = []
        actual_result = algorithm.inverse_transform(input_signal)

        self.assertEqual(expected_result, actual_result)

    def test_inverse_transform_none(self):
        input_signal = None
        algorithm = HaarAlgotithm()

        with self.assertRaises(TypeError):
            algorithm.inverse_transform(input_signal)

    def test_inverse_transform_non_grade_two(self):
        input_signal = [220, 211, 212]
        algorithm = HaarAlgotithm()

        with self.assertRaises(Exception):
            algorithm.inverse_transform(input_signal)

    def test_filter_signal_happy_path(self):
        input_signal = [220, 211, 212, 218, 217, 214, 210, 202]
        algorithm = HaarAlgotithm()

        expected_result = [217.5, 208.5, 213, 213, 217.75, 217.75, 212.25, 204.25]
        actual_result = algorithm.filter_signal(input_signal, 4)

        self.assertEqual(expected_result, actual_result)

    def test_filter_signal_happy_path_one_element(self):
        input_signal = [220]
        algorithm = HaarAlgotithm()

        expected_result = [220]
        actual_result = algorithm.filter_signal(input_signal, 4)
        self.assertEqual(expected_result, actual_result)

    def test_filter_signal_happy_path_empty_array(self):
        input_signal = []
        algorithm = HaarAlgotithm()

        expected_result = []
        actual_result = algorithm.filter_signal(input_signal, 4)
        self.assertEqual(expected_result, actual_result)

    def test_filter_signal_input_signal_none(self):
        algorithm = HaarAlgotithm()

        with self.assertRaises(TypeError):
            algorithm.filter_signal(None, 4)

    def test_filter_signal_threshold_none(self):
        algorithm = HaarAlgotithm()

        with self.assertRaises(TypeError):
            algorithm.filter_signal([], None)

    def test_filter_signal_input_signal_threshold_none(self):
        algorithm = HaarAlgotithm()

        with self.assertRaises(TypeError):
            algorithm.filter_signal(None, None)

    def test_filter_signal_non_grade_two(self):
        input_signal = [220, 211, 212]
        algorithm = HaarAlgotithm()

        expected_result = [218.25, 209.25, 213.75, 213.75]
        actual_result = algorithm.filter_signal(input_signal, 4)
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
