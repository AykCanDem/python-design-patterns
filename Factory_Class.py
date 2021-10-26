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


class Creator():
    "Factory class"

    def create_object(type):
        if(type=='binary'):
            return convert_to_binary()
        elif(type=="hexadecimal"):
            return convert_to_hexadecimal()



if __name__ == "__main__":

    b = Creator.create_object("binary")
    h = Creator.create_object("hexadecimal")

    numbers = [10,11,12,13,14,15,16]
    for num in numbers:
        print(b.convert(num))
        print(h.convert(num))