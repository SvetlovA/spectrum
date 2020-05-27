from ..base_algorithm import BaseAlgorithm


class HaarAlgotithm(BaseAlgorithm):

    def direct_transform(self, signal: list) -> list:
        if signal is None:
            raise TypeError('Argument signal is None')

        if len(signal) <= 1:
            return signal

        if len(signal) % 2:
            raise Exception('Signal list count must be grade 2')

        detailed_coeficients = []
        aproximate_signal = []

        for i in range(0, len(signal), 2):
            detailed_coeficients.append((signal[i] - signal[i + 1]) / 2.0)
            aproximate_signal.append((signal[i] + signal[i + 1]) / 2.0)

        detailed_coeficients.extend(self.direct_transform(aproximate_signal))
        return detailed_coeficients


    def inverse_transform(self, transformed_signal: list) -> list:
        if transformed_signal is None:
            raise TypeError('Argument signal is None')

        if len(transformed_signal) <= 1:
            return transformed_signal

        if len(transformed_signal) % 2:
            raise Exception('Signal list count must be grade 2')

        signal_first_part, signal_second_part = HaarAlgotithm.__get_signal_parts(transformed_signal)
        signal_second_part = self.inverse_transform(signal_second_part)

        if len(signal_first_part) != len(signal_second_part):
            raise Exception('Second and first parts of signal mast be same')

        result_signal = []
        for first_point, second_point in zip(signal_first_part, signal_second_part):
            result_signal.append(second_point + first_point)
            result_signal.append(second_point - first_point)

        return result_signal

    @staticmethod
    def __get_signal_parts(input_signal: list) -> tuple:
        half_signal_length = len(input_signal) // 2
        return input_signal[:half_signal_length:], input_signal[half_signal_length::]
