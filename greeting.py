# ----------------------------------------------------------------------
# Name:        greeting
# Purpose:     A gentle introduction to Python
#
# Date:       Spring 2019
# ----------------------------------------------------------------------
"""
Print a personalized greeting.

Prompt the user for their name.
Print a customized Hello message.
"""


def main():
    name = input('Please enter your name: ')  # Prompt user
    print('Hello', name or 'Friend')  # Print a personalized greeting



if __name__ == "__main__":
    main()
