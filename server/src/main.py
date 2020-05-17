from algorithms.implementation.haar_algorithm import HaarAlgotithm


def main():
    input_signal = [220, 211, 212, 218, 217, 214, 210, 202]
    algorithm = HaarAlgotithm()
    result = algorithm.filter_signal(input_signal, 4)

    print(result)

if __name__ == "__main__":
    main()
