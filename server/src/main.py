from algorithms.implementation.haar_algorithm import HaarAlgotithm


def main():
    input_signal = [220, 211, 212, 218, 217, 214, 210, 202]
    haar_algorithm = HaarAlgotithm()
    result = haar_algorithm.direct_transform(input_signal)

    print(result)

if __name__ == "__main__":
    main()
