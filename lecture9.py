# ----------------------------------------------------------------------
# Name:        lecture9
# Purpose:     Demonstrate the use of classes
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing some class definitions to be used in lecture 9.

The FruitShop class definition is used to illustrate a basic class
definition.
The Account class definition is used to illustrate methods, instance and
class variables.
The Student class definition is used to illustrate static and class
methods.
The SavingsAccount, PremiumAccount and PremiumSavingsAccount classes
are used to illustrate inheritance.
"""


class FruitShop:

    """
    Represent a shop that sells fruits.
    """


class Account(object):

    """
    Represent a bank account.

    Argument:
    account_holder (string): account holder's name.

    Attributes:
    holder (string): account holder's name.
    balance (number): account balance in dollars.
    """

    currency = '$'  # class variable

    def __init__(self, account_holder):
        self.holder = account_holder
        self._balance = 0
        self._country = 'US'
        self.__note = 'OK'

    def __str__(self):
        return f'Name: {self.holder}\nBalance: ${self.balance: ,.2f}'

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance and self.holder == other.holder

    def __add__(self, other):
        new_holder = f'{self.holder} & {other.holder}'
        new_account = Account(new_holder)
        new_account.deposit(self.balance + other.balance)
        return new_account

    def deposit(self, amount):
        """
        Deposit the given amount to the account.
        :param amount: (number) the amount to be deposited in dollars.
        """
        self._balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if possible.
        :param amount: (number) the amount to be withdrawn in dollars.
        :return: (boolean) True if the withdrawal is successful
                False otherwise
        """
        if self._balance >= amount:
            self._balance = self._balance - amount
            return True
        else:
            return False

    @property
    def credit_limit(self):
        """
        The credit limit available for the account holder
        :return: (float) maximum credit
        """
        return self._balance / 2

    @property
    def balance(self):
        return self._balance


class Student:
    """
    Represent a student in a college setting.

    Arguments:
    name (string): student name
    sid (integer): student id - 8 digits

    Attributes:
    name (string): student name
    sid (integer): student id - 8 digits
    """

    enrollment = 0  # Class variable

    def __init__(self, name, sid):
        self.name = name
        if self.valid(sid):  # invoke the static method
            self.sid = sid
        else:
            self.sid = 99999999
        self.add_student()  # invoke the class method

    @staticmethod
    def valid(some_id):
        """
         A valid student id starts with 2019.
        :param some_id: (integer)
        :return: (boolean) True id id is valid and False otherwise.
        """
        return some_id // 10000 == 2019

    @classmethod
    def add_student(cls):
        """
        Update the enrollment total.
        """
        cls.enrollment += 1  # update the class variable


class SavingsAccount(Account):

    """
    Represent a savings bank account with a withdrawal fee.
    Inherits from:  Account

    Argument:
    account_holder (str): account holder's name.

    Attributes:
    holder (str): account holder's name.
    balance (number): account balance in dollars.
    """

    # class variable
    fee = 1

    def withdraw(self, amount):
        super.withdraw(amount)
        self._balance -= self.fee


class PremiumAccount(Account):

    """
    Represent a premium interest bearing bank account.
    Inherits from Account

    Argument:
    account_holder (str): account holder's name.
    rate (float): interest rate

    Attributes:
    holder (str): account holder's name.
    balance (number): account balance in dollars.
    interest_rate (float): interest rate
    """
    def __init__(self, account_holder, rate):
        super.__init__(account_holder)
        self.interest_rate = rate


class PremiumSavingsAccount(PremiumAccount, SavingsAccount):

    """
    Represent a premium interest bearing bank account
    with a withdrawal fee.
    Inherits from PremiumAccount, SavingsAccount

    Argument:
    account_holder (str): account holder's name.
    rate (float): interest rate

    Attributes:
    holder (str): account holder's name.
    balance (number): account balance in dollars.
    interest_rate (float): interest rate

    """
