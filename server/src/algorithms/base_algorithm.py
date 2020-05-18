from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):

    @abstractmethod
    def direct_transform(self, signal: list) -> list:
        pass

    @abstractmethod
    def inverse_transform(self, transformed_signal: list) -> list:
        pass

    def filter_signal(self, input_signal: list, threshold: int) -> list:
        if input_signal is None or not threshold:
            raise TypeError

        BaseAlgorithm.__complete_signal(input_signal)
        transformed_signal = self.direct_transform(input_signal)
        filtered_transformed_signal = [0 if abs(x) < threshold else x for x in transformed_signal]

        return self.inverse_transform(filtered_transformed_signal)

    @staticmethod
    def __complete_signal(signal: list) -> None:
        if len(signal) <= 1:
            return

        while len(signal) % 2 != 0:
            signal.append(signal[-1])
