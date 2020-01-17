"""
Five functions about dictionary.

For those functions' specific goals, please the function docstrings.
"""


def top_students(grades, n=3):
    """
    Ranking students from highest scores to lowest scores, and get the
        students' names with top n grades
    :param grades: (dictionary) represents student grades.
        Keys are names, values are grades.
    :param n: (integer) n top students
    :return: (a list) the names of the top n students with the highest
        grades
    """
    return sorted(grades, key=grades.get, reverse=True)[:n]


def extra_credit(grades, extra_credit=1):
    """
    :param grades: (dictionary) students names are keys, and grades are
        values
    :param extra_credit: the extra_credit to add to students' original
        grades
    :return: (a dictionary) a dictionary with keys of names and values
        of updated grades.
    """
    return {name: grades[name] + extra_credit for name in grades}


def adjusted_grade(iclicker_grades, midterm_grades):
    """
    Add one point to midterm_grade if a student's iclicker points are
        more than average iclicker points.
    :param iclicker_grades: (dictionary) students' names are the keys
        and iclicker scores are the values
    :param midterm_grades: (dictionary) students' names are the keys
        and midterm scores and the values
    :return: (dictionary) students' names are the keys, adjusted grades
        are the values
    """
    if not iclicker_grades:
        return midterm_grades
    iclicker_avg = sum(iclicker_grades.values()) / len(iclicker_grades)
    students = set(iclicker_grades).union(set(midterm_grades))
    extra_credit = {student: 1 for student in iclicker_grades
                    if iclicker_grades[student] >= iclicker_avg}
    return {student: midterm_grades.get(student, 0)
            + extra_credit.get(student, 0) for student in students}


def sum_of_inverse_odd(n):
    """
    Adding the inverse of the odd numbers from 1 to n (inclusive)
    :param n: (number) the bound that should be included
    :return: (number) sum of inverse of odd numbers from 1 to n
        (inclusive)
    """
    return sum(1 / odd for odd in range(1, n + 1, 2))


def same_length(*args):
    """
    It determines whether all strings in the argument have the same
    length
    :param args: an arbitrary number of strings
    :return: (boolean) True if these strings are all of the same length
        Otherwise, return False
    """
    return all(len(string) == len(args[0]) for string in args)


def main():
    empty_class = {}
    cs122 = {'Zoe': 90, "Alex": 93, "Dan": 79, "Anna": 100}
    print(top_students(cs122, 2))
    print(top_students(cs122))
    print(top_students(cs122, 10))
    print(top_students(empty_class, 6))
    print(cs122)
    print()
    print(extra_credit(cs122))
    print(extra_credit(cs122, 2))
    print(cs122)
    print(extra_credit(empty_class, 5))
    print()
    iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110, 'Bryan': 2,
                'Andrea': 110}
    exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64, 'Bryan': 95,
            'Andrea': 86}
    print(adjusted_grade(iclicker, exam))
    print(adjusted_grade({}, exam))
    print(adjusted_grade(iclicker, {}))
    print(adjusted_grade({}, {}))
    print()
    print(sum_of_inverse_odd(0))
    print(sum_of_inverse_odd(1))
    print(sum_of_inverse_odd(2))
    print(sum_of_inverse_odd(3))
    print(sum_of_inverse_odd(2000))
    print()
    print(same_length())
    print(same_length('hi', 'ha', 'it', 'quiet'))
    print(same_length('hi', 'ha', 'it'))
    print(same_length('hello', 'ha', 'it', 'ok'))
    print(same_length('Spartan'))


if __name__ == "__main__":
    main()
