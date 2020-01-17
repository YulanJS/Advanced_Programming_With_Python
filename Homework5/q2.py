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
