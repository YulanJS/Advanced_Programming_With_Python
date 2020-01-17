import string

"""
def adjusted_grade(iclicker, exam):
    if not iclicker:
        return exam
    iclicker_avg = sum(iclicker.values()) / len(iclicker)
    boost = {name: 1 if iclicker[name] >= iclicker_avg else 0
             for name in iclicker}
    all_students = set(iclicker) | set(exam)
    return {name: boost.get(name, 0) + exam.get(name, 0)
            for name in all_students}
"""


def main():
    zen = "SPECIAL CASES aren't special enough to break the rules."
    print(zen)
    plural = [word.strip(string.punctuation) for word in zen.split()
              if word.lower().strip(string.punctuation)[-1] == 's']
    print(plural)


if __name__ == "__main__":
    main()
