# ----------------------------------------------------------------------
# Name:     measurenumpy
# Purpose:  Measure and compare pure Python vs NumPy operations
#
# Date:     Spring 2019
# ----------------------------------------------------------------------
"""
Measure and compare pure Python vs NumPy operations.

1.  Looping over a Python list to add its elements.
2.  Using the built-in function sum to add the elements of a Python list
3.  Using the built-in function sum to add the elements of a NumPy array
4.  Using the NumPy function np.sum to add the elements of a NumPy array
"""
import timeit
import numpy as np

def loop_sum(sequence):
    """
    Compute the sum of the given sequence using a for loop.
    :param sequence: list of numbers
    :return: None
    """
    result = 0
    for each_number in sequence:
        result += each_number


def builtin_sum(sequence):
    """
    Compute the sum of the given sequence using built-in sum function.
    :param sequence: list of numbers
    :return: None
    """
    result = sum(sequence)


def builtin_numpy(sequence):
    """
    Compute the sum of the given sequence using built-in sum function.
    :param sequence: NumPy array containing numbers
    :return: None
    """
    result = sum(sequence)


def numpy_numpy(sequence):
    """
    Compute the sum of the given sequence using the NumPy sum function.
    :param sequence: NumPy array containing numbers
    :return: None
    """
    result = np.sum(sequence)


def main():

    print(f"""Loop Sum on Python list:     {
          min(timeit.repeat("loop_sum(seq)", number=1000, repeat=10, 
                            setup="seq=list(range(10000))",
                            globals=globals())):.4f}""")
    print(f"""Built-in Sum on Python list: {
          min(timeit.repeat("builtin_sum(seq)", number=1000, repeat=10, 
                            setup="seq=list(range(10000))",
                            globals=globals())):.4f}""")
    print(f"""Python Sum on NumPy array:   {
          min(timeit.repeat("builtin_numpy(seq)", number=1000, repeat=10, 
                            setup="seq=np.arange(10000)",
                            globals=globals())):.4f}""")

    print(f"""NumPy Sum on NumPy array:    {
          min(timeit.repeat("numpy_numpy(seq)", number=1000, repeat=10, 
                            setup="seq=np.arange(10000)",
                            globals=globals())):.4f}""")


if __name__ == "__main__":
    main()
