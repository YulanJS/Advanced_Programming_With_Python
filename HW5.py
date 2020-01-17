# ----------------------------------------------------------------------
# Name:        HW5
# Purpose:     Practice lambda, decorator, and generator
#
# Date:       Spring 2019
# ----------------------------------------------------------------------
"""
Five questions to practice lambda, decorator, and generator.

For specific functionality of each function, please see each function's
document.
"""

import string


def most_e(*args):
    """
    From arbitrary number of strings, pick up the string with the most
    occurrences of letter 'e' (case insensitive).
    :param args: (string) arbitrary number of strings
    :return: (string ) string with the most occurrences of the letter
    'e' (upper or lower)
    """
    if not args:
        return None
    return max(args, key=lambda string: string.lower().count('e'))


def top_midterm(grades, n=4):
    """
    Get a list of names of n students with highest midterm grades
    sorted from highest grade to lowest grade.
    :param grades: (dictionary) Keys are students' names. Values are
    lists of grades: [homework grade, question of the week grade,
    midterm grade]. Three types of grades must be in that order.
    :param n: (number) top n students
    :return: (list) A list of names of the top n students with highest
    midterm grade. The student with the highest midterm grade should
    be put in the first one in the list.
    """
    return sorted(grades, key=lambda student: grades[student][2],
                  reverse=True)[:n]


def shout(function):
    """
    decorate function: change all letters in strings returned from
    function into uppercase, and add !!! to the end.
    :param function: the function to be decorated, it returns strings.
    :return: decorated function.
    """
    def wrapper(*args):
        return function(*args).upper() + "!!!"
    return wrapper


@shout
def greet(name):
    """
    Return a personalized hello message.
    :param name: (string)
    :return: (string)
    """
    return f'Hello {name}'


@shout
def repeat(phrase, n):
    """
    Repeat the specified string n times
    with a space character in between.
    :param phrase: (string)
    :param n: number of times the phrase will be repeated
    :return:
    """
    words = phrase.split()
    return ' '.join(n * words)


def repeat_character(string, n):
    """
    Generate string of length n, one for each character in the string
    specified.
    :param string: (string)
    :param n: (number) repeat each character in the given string n times
    :return: (string) generates string of length n, one for each
    character in the string specified
    """
    for letter in string:
        yield letter * n


def alpha_labels(start_label='A'):
    """
    Generates labels alphabetically, starting with the star_label, then
    increasing the length after reaching Z.
    :param start_label:(string) a string of repeated uppercase letters,
    default value is 'A'
    :return: (strings) Generates labels alphabetically,
    starting with the star_label, then increasing the length after
    reaching Z.
    """
    alphabet = string.ascii_uppercase
    curr_length = len(start_label)
    yield from repeat_character(alphabet[ord(start_label[0]) - ord('A'):],
                                curr_length)
    while True:
        curr_length += 1
        yield from repeat_character(alphabet, curr_length)


def main():
    print("question 1: ")
    print(most_e())
    print(most_e('Go', 'Spartans', 'Take', 'Selfies', 'eat',
                 'APPLES'))
    print(most_e('Go', 'Spartans', 'APPLES'))
    print(most_e('Go', 'Spartans', 'Eat'))
    print(most_e('Go', 'Spartans', 'Take', 'Selfies', 'degree'))
    print(most_e('Spartans'))
    print()
    print("question 2: ")
    empty_class = {}
    cs122 = {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
             'Dan': [90, 60, 70], 'Anna': [60, 80, 100],
             'Ryan': [100, 95, 80], 'Bella': [79, 70, 99]}
    print(top_midterm(cs122, 2))
    print(top_midterm(cs122))
    print(top_midterm(cs122, 10))
    print(top_midterm(empty_class, 6))
    print(cs122)
    print()
    print("question 3: ")
    print(greet('Rula'))
    print(repeat('Python is fun!', 3))
    print(repeat('Go Spartans!', 5))
    print()
    print("question 4: ")
    vocabulary = repeat_character('ACGT', 3)
    print(next(vocabulary))  # AAA
    print(next(vocabulary))  # CCC
    print(next(vocabulary))  # GGG
    print(next(vocabulary))  # TTT
    # print(next(vocabulary))  # StopIteration
    import string
    labels = repeat_character(string.ascii_uppercase, 2)
    for each_label in labels:
        print(each_label)  # AA through ZZ is printed.
    print()
    print("question 5: ")
    infinite_generator = alpha_labels("XXX")
    print(next(infinite_generator))
    print(next(infinite_generator))
    print(next(infinite_generator))
    print(next(infinite_generator))
    print(next(infinite_generator))


if __name__ == "__main__":
    main()


