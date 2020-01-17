# ----------------------------------------------------------------------
# Name:        Homework 6
# Purpose:     Demonstrate class related functions, variables, methods.
#
# Date:        Spring 2019
# ----------------------------------------------------------------------
"""
The apocalypse is happening and you need to get your backpack in order!

The class Backpack allows for a bag to be created with the owner's name.
It will allow for items to be added and removed.
It will allow user to change the starter_item. (class variable)
It will compare (<, >) using total_space taken of each bag.
It will compare (==) bag items to see if they match.
It will add (+) two backpacks into one bigger one.
"""


class Backpack:

    """
    Representing a backpack to hold your items.
    Creating a backpack requires a Name and Bag Size.
    Length (len) will return the number of unique items in bag.
    Comparing two bags (<) will compare the total_space taken in each.
    For equal (==) it will compare the items in each bag.
    Adding two backpacks (+) will combine into a bigger backpack with
    items from both backpacks!

    Arguments:
    name: (string) contains name of owner of backpack
    size: (int) size of the backpack

    Attributes:
    name: (string) contains name of owner of backpack
    size: (int) size of backpack
    bag: (dict) contains contents of backpack with weight/quantity
    total_space: (int) contains the total space taken by items
    """

    # Class variable.
    starter_item = 'a knife'

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.bag = {}
        self.total_space = 0

    def __str__(self):
        label = [f"{self.name} carries {self.starter_item}.\n"
                 f"{self.name}'s backpack contains:"]

        for item in self.bag:
            label.append(f"{item} - Size: {self.bag[item][0]} - "
                         f"Quantity: {self.bag[item][1]}")

        label.append(f'Total: {self.total_space}/{self.size}')
        return '\n'.join(label)

    def __getitem__(self, item):
        if item in self.bag:
            return f'You have {self.bag[item][1]} {item} of size ' \
                   f'{self.bag[item][0]}'
        else:
            return f'{item} not found.'

    def __len__(self):
        return len(self.bag)

    # Less than (<)
    def __lt__(self, other):
        return self.total_space < other.total_space

    # Equal (==)
    def __eq__(self, other):
        return self.bag == other.bag

    # Add (+)
    def __add__(self, other):
        import copy
        new_bag = Backpack(self.name, self.size + other.size)
        new_bag.bag = copy.deepcopy(self.bag)
        new_bag.total_space = self.total_space

        for item in other.bag:
            new_bag.add_item(item, other.bag[item][0])
        return new_bag

    def add_item(self, item, size):
        """
        Add item to the backpack, if already exist, increase quantity,
        if not, add to dictionary of items. If there is not enough room,
        notify user and return.
        :param item: (string) contains name of the item
        :param size: (int) contains size of the item
        :return: none
        """
        if size + self.total_space > self.size:
            print(f"{item} too big. Not enough room.")
            return

        if item in self.bag:
            self.bag[item][1] += 1
        else:
            self.bag[item] = [size, 1]
        self.total_space += size

    def remove_item(self, item):
        """
        Remove an item from backpack, if it exists and there's only 1,
        pop the item out of dictionary. If more than 1, reduce quantity.
        Update total_space.
        :param item: (string) contains the name of the item
        :return: none
        """
        if item in self.bag and self.bag[item][1] == 1:
            self.total_space -= self.calc_total(item)
            self.bag.pop(item)
        else:
            self.bag[item][1] -= 1
            self.total_space -= self.bag[item][0]

    def calc_total(self, item):
        """
        Calculate total space taken by an item by multiplying size with
        quantity.
        :param item: (string) contains the name of the item
        :return: (int) the total space taken by the item
        """
        return self.bag[item][0] * self.bag[item][1]

    @classmethod
    def change_starter(cls, item):
        """
        Change the starting item that you carry.
        :param item: (string) contains the name of the item
        :return: none
        """
        if item[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            cls.starter_item = 'an ' + item.lower()


def main():
    print("Create my_bag:")
    my_bag = Backpack('Mike', 20)
    my_bag.add_item('Peanut Butter', 3)
    my_bag.add_item('Blanket', 2)
    my_bag.add_item('Food', 4)
    my_bag.add_item('Food', 4)
    print(my_bag)

    print("\nCalculate total space taken by Food:")
    print(f"Food takes up {my_bag.calc_total('Food')} space.")

    print("\nChanging starter_item:")
    Backpack.change_starter('book')
    print("Changed to " + my_bag.starter_item)

    print("\nRemoving items 'Food' and 'Peanut Butter':")
    my_bag.remove_item('Food')
    my_bag.remove_item('Peanut Butter')
    print(my_bag)

    print("\nTesting __getitem__ and __len__:")
    print("__getitem__: " + my_bag['Blanket'])
    print("__getitem__: " + my_bag['Rocket Launcher'])
    print(f"__len__: {len(my_bag)}")

    print("\nCreate second_bag:")
    second_bag = Backpack('William', 15)
    second_bag.add_item('Cell Phone', 2)
    second_bag.add_item('Camera', 5)
    second_bag.add_item('Food', 4)
    second_bag.add_item('Cell Phone', 2)
    print(second_bag)
    print(f"__len__: {len(second_bag)}")

    print("\nAttempt to add heavy Rocks Of No Reason to second_bag:")
    second_bag.add_item('Rocks', 20)
    second_bag.add_item('Rocks Of No Reason', 15)

    # create a third backpack as a copy of my_bag
    third_bag = my_bag

    # make fourth backpack from adding others together
    fourth_bag = my_bag + second_bag
    print("\nComparing bags:")
    print(f"{second_bag.name}'s bag of. size {second_bag.total_space} < "
          f"{my_bag.name}'s bag of size {my_bag.total_space}: " +
          str(second_bag < my_bag))
    print(f"{second_bag.name}'s bag of size {second_bag.total_space} > "
          f"{my_bag.name}'s bag of size {my_bag.total_space}: " +
          str(second_bag > my_bag))
    print("__eq__: third_bag == my_bag: " + str(third_bag == my_bag))
    print("__eq__: second_bag == my_bag: " + str(second_bag == my_bag))
    print("\n__add__: my_bag + second_bag = ")
    print(fourth_bag)

    print("\nTest to verify my_bag unmodified after:")
    print(my_bag)

    print("\nTest to verify second_bag unmodified after:")
    print(second_bag)


if __name__ == "__main__":
    main()
