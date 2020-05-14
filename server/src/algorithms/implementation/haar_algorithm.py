from ..base_algorithm import BaseAlgorithm


class HaarAlgotithm(BaseAlgorithm):

    def direct_transform(self, signal):
        if signal is None:
            raise TypeError('Argument signal is None')

        if len(signal) <= 1:
            return signal

        if len(signal) % 2 != 0:
            raise Exception('Signal list count must be grade 2')

        detailed_coeficients = []
        aproximate_signal = []

        for i in range(0, len(signal), 2):
            detailed_coeficients.append((signal[i] - signal[i + 1]) / 2.0)
            aproximate_signal.append((signal[i] + signal[i + 1]) / 2.0)

        detailed_coeficients.extend(self.direct_transform(aproximate_signal))
        return detailed_coeficients


    def inverse_transform(self, transformed_signal):
        raise NotImplementedError
