from ..base_algorithm import BaseAlgorithm


class HaarAlgotithm(BaseAlgorithm):

    def direct_transform(self, signal):
        if len(signal) <= 1:
            return signal

        detailed_coeficients = []
        aproximate_signal = []

        for i in range(0, len(signal), 2):
            detailed_coeficients.append((signal[i] - signal[i + 1]) / 2.0)
            aproximate_signal.append((signal[i] + signal[i + 1]) / 2.0)

        detailed_coeficients.extend(self.direct_transform(aproximate_signal))
        return detailed_coeficients


    def inverse_transform(self, transformed_signal):
        raise NotImplementedError
