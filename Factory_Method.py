"""
The factory finds the relevant class using some kind of logic
from the attributes of the request.
Then, it asks the subclass to initiate the new object and return it
to client.

Factory Method: is a method that used to create product objects
without specifying their concrete classes.
It is for adding extra abstraction between the object creation
and where it is used.
"""

class convert_to_binary():

    def convert(self, number):
        return f"bin({number}) = {bin(number)}"

class convert_to_hexadecimal():

    def convert(self, number):
        return f"hex({number}) = {hex(number)}"


def Factory(to: str) -> dict:
    "Factory method"
    converters = {
        "binary" : convert_to_binary(),
        "hexadecimal" : convert_to_hexadecimal()
    }

    return converters[to]



if __name__ == "__main__":

    b = Factory("binary")
    h = Factory("hexadecimal")

    numbers = [10,11,12,13,14,15,16]
    for num in numbers:
        print(b.convert(num))
        print(h.convert(num))