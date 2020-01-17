# ----------------------------------------------------------------------
# Name:        demoargs
# Purpose:     demonstrate the use of the argparse module
#
# Author:      Rula Khayrallah
#
# ----------------------------------------------------------------------
"""
Demonstrate the use of the argparse module.

usage: demoargs.py [-h] [-v] {blue,yellow,green} [name] [size] [score]
positional arguments:
  {blue,yellow,green}  What background color would you like?
  name                 What is the name of the main character?
  size                 How many columns/rows in the grid?
  score                File to be used to save the score

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Print details?
"""
import argparse
import sys


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the name (string), size (int),
         color (string), score (file object) and the verbose
         option (boolean).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What background color would you like?',
                        choices=['blue', 'yellow', 'green'])

    parser.add_argument('name',
                        help='What is the name of the main character?',
                        nargs='?',
                        default='Sammy the Spartan')

    parser.add_argument('size',
                        help='How many columns/rows in the grid?',
                        type=int,
                        nargs='?',
                        default=10)

    parser.add_argument('score',
                        help='File to be used to save the score',
                        type=argparse.FileType('x', encoding='UTF-8'),
                        nargs='?',
                        default=sys.stdout)

    parser.add_argument('-v', '--verbose',
                        help='Print details?',
                        action='store_true')

    arguments = parser.parse_args()
    name = arguments.name
    size = arguments.size
    color = arguments.color
    score = arguments.score
    verbose = arguments.verbose
    return name, size, color, score, verbose


def main():
    name, size, color, score, verbose = get_arguments()
    if verbose:
        print(f'Starting a {color} game with {name} in a grid of size {size}')


if __name__ == '__main__':
    main()
