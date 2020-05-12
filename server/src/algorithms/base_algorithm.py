from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):

    @abstractmethod
    def direct_transform(self, signal):
        pass

    @abstractmethod
    def inverse_transform(self, transformed_signal):
        pass

    def filter_signal(self, threshold):
        transformed_signal = self.direct_transform(threshold)
        filtered_transformed_signal = [0 if abs(x) < threshold else x for x in transformed_signal]

        return self.inverse_transform(filtered_transformed_signal)
