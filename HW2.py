"""
A calculator calculates compound interest.

It shows the total amount of money after N years.
The money includes principal and compound interest.
"""


def valid_input():
    """
    It prompts a user to enter principal and interest until these values are
    valid.
    : return : (list) principal and interest.
    """
    valid = False
    while not valid:
        principal = float(input("Please enter principal amount: $"))
        if principal < 0 or principal > 1000000:
            print("Invalid amount. ", end="")
            print("Principal must be between $0 and $1,000,000.00")
        else:
            valid = True
    valid = False
    while not valid:
        interest = float(input("Please enter interest rate: %"))
        if interest < 0 or interest > 100:
            print("Invalid rate. Interest rate must be between 0 and 100")
        else:
            valid = True
    return principal, interest


def calculate_compound_total(principal, interest, n):
    """
    It calculates compounded total amount after n years.
    : param principal: (float) user's principal
    : param interest: (float) interest applied to a user
    : param n: (int) n years
    : return (float) total amount of money after n years
    """
    return principal * (1 + interest / 100) ** n


if __name__ == "__main__":
    principal, interest = valid_input()
    for i in range(5, 55, 5):
        result = f'${calculate_compound_total(principal, interest, i):,.2f}'
        print(f'Accrued amount after {i:>3} years: {result: >14}')


