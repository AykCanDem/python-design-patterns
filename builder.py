"""
The Builder Pattern is a creational pattern whose intent is to
 separate the construction of a complex object from its representation
 so that you can use the same construction process to create different representations.

Solves: How can a class create differnet representations of a complex object?



Product: The Product being built.
Builder: Builds the concrete product. Implements the IBuilder interface.
Builder Interface: The Interface that the Concrete builder should implement.
Director: Has a construct() method that when called creates a customized product.
"""

from abc import ABCMeta, abstractmethod

class IBuilder(metaclass = ABCMeta):

    @staticmethod
    @abstractmethod
    def build_walls():
        """Build walls"""
        pass

    @staticmethod
    @abstractmethod
    def build_windows():
        """Build windows"""
        pass

    @staticmethod
    @abstractmethod
    def build_ceiling():
        """Build ceiling"""
        pass



class Builder(IBuilder):
    """Concrete builder"""

    def __init__(self):
        self.product = Product()

    def build_walls(self):
        self.product.parts.append("walls")
        return self

    def build_windows(self):
        self.product.parts.append("windows")
        return self

    def build_ceiling(self):
        self.product.parts.append("ceiling")
        return self

    def get_product(self):
        return self.product


class Product():

    def __init__(self):
        self.parts = []



class Director():
    """The Director, building a complex representation"""

    @staticmethod
    def construct():
        builder = Builder()

        return builder\
            .build_walls()\
                .build_windows()\
                    .build_ceiling()\
                        .get_product()


if __name__ == "__main__":

    PRODUCT = Director().construct()
    print(PRODUCT.parts)


                
    



    





