# ----------------------------------------------------------------------
# Name:        Homework 4
# Purpose:     Dictionaries, generator expressions, and *args
#
# Date:       Spring 2019
# ----------------------------------------------------------------------

"""
This program is designed to answer questions 1-5 of homework #4

The program contains functions that work with dictionaries, generator
expressions, and arbitrary parameters
"""


def top_students(grade_book, num_students=3):
    """
    The function returns the top n students
    :param grade_book: (dictionary) representing students and grades
    :param num_students: (integer) number of students to be returned
    :return: (dictionary) sorted slice of varying size
    """
    return sorted(grade_book, key=grade_book.get, reverse=True)[:num_students]


def extra_credit(grade_book, extra_points=1):
    """
    The function creates a dictionary with updated student grades
    :param grade_book: (dictionary) representing students and grades
    :param extra_points: (integer) number representing 0 or 1 for EC
    :return: (dictionary) new dictionary updated to reflect EC points
    """
    return {name: grade_book[name]+extra_points for name in grade_book}


def adjusted_grade(clicker_points, midterm_grade):
    """
    The function creates a dictionary with updated midterm scores
    :param clicker_points: (dictionary) iclicker scores for students
    :param midterm_grade: (dictionary) midterms scores for students
    :return: (dictionary) updated midterm scores with extra credit
    """
    if not clicker_points:
        return midterm_grade
    avg_clicker_points = sum(clicker_points.values())/len(clicker_points)
    joint_set = set(clicker_points).union(set(midterm_grade))
    clicker_extra_points = {student: 1 if clicker_points.get(student)
                            >= avg_clicker_points else 0 for
                            student in clicker_points}
    return {name: midterm_grade.get(name, 0) +
            clicker_extra_points.get(name, 0)
            for name in joint_set}


def sum_of_inverse_odd(number):
    """
    This function uses a generator to return the sum of inverse in range
    :param number: (number) positive integer that serves as upper bound
    :return: (number) the sum of inverse numbers
    """
    return sum(1/x for x in range(1, number+1, 2))


def same_length(*args):
    """
    This function compares the length of an arbitrary amount of strings
    :param args: (string) arbitrary number of strings
    :return: (boolean) indicates whether the strings are the same length
    """
    if len({len(word) for word in args}) <= 1:
        return True
    return False


def main():
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    print(top_students(cs122, 2))  # ['Anna', 'Alex']
    print(top_students(cs122))  # ['Anna', 'Alex', 'Zoe']
    print(top_students(cs122, 10))  # ['Anna', 'Alex', 'Zoe', 'Dan']

    print(top_students(empty_class, 6))  # []
    print(cs122)  # {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}
    print()
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    print(extra_credit(cs122))
    # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(extra_credit(cs122, 2))
    # {'Zoe':92, 'Alex': 95, 'Dan':81, 'Anna':102}
    print(cs122)  # {'Zoe':90, 'Alex': 93, 'Dan':79, 'Anna':100}
    print(extra_credit(empty_class, 5))  # {}
    print()
    iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                'Bryan': 2, 'Andrea': 110}
    exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
            'Bryan': 95, 'Andrea': 86}
    adjusted_grade(iclicker, exam)
    # {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96, 'Ryan': 90,
    # 'Andrea': 87, 'Dan': 89}
    adjusted_grade({}, exam)
    # {'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64, 'Dan': 89,
    # 'Alex': 95}
    adjusted_grade(iclicker, {})
    {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0, 'Anna': 1, 'Alex': 1}
    adjusted_grade({}, {}) # {}
    print()
    print(sum_of_inverse_odd(0))  # 0
    print(sum_of_inverse_odd(1))  # 1.0
    print(sum_of_inverse_odd(2))  # 1.0
    print(sum_of_inverse_odd(3))  # 1.3333333333333333
    print(sum_of_inverse_odd(2000))  # 4.435632673335106
    print()
    print(same_length())  # True
    print(same_length('hi', 'ha', 'it', 'quiet'))  # False
    print(same_length('hi', 'ha', 'it'))  # True
    print(same_length('hello', 'ha', 'it', 'ok'))  # False
    print(same_length('Spartan'))  # True


if __name__ == "__main__":
    main()

