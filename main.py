import numpy as np


def generate_matrix(size: int):
    np.savetxt('important_square.txt', np.random.randint(10, 100, (10, 10)), fmt='%.0f')


if __name__ == '__main__':
    generate_matrix(size=10)
