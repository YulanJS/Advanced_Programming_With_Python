import re


def main():
    greeting_pattern = r'Hello'
    greeting_match = re.match(greeting_pattern, 'Hello World!')
    print(greeting_match.group())
    print(greeting_match.start())
    print(greeting_match.end())
    print(greeting_match.span())


if __name__ == "__main__":
    main()
