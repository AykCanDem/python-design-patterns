"""
An abstract class is partially implemented and defines the requirements
that its child classes should have and some generic child behavior
as well as what functions they should have. Concrete classes extend
abstract classes and provide the unimplemented functionality,
while inheriting the common functionalities.

The abstract factory pattern adds an abstract layer over multiple
factory method implementations. The abstract factory contains 


Abstract Factory:
Abstract Factory defines an interface for creating all distinct products
but leaves the actual product creation to concrete factory classes. 
Each factory type corresponds to a certain product variety.


Concrete Factory:
Concrete Factories create Concrete Products as directed by the Abstract Factories.
The concrete factories are only capable of creating those products that are
specified in them.
Each concrete factory corresponds to a specific variant of products and
creates only those product variants.

Abstract Product:
These classes contain abstract methods that are mandatory for the construction
of the products. These abstract classes are referred to as interfaces.

Concrete Product:
Concrete products inherit the abstract methods from the abstract products.
Using the interfaces, different families of products can be created.

"""
from __future__ import annotations
from abc import ABC, ABCMeta
from abc import abstractmethod


class AbstractFactory_OS(ABC):
    
    # method valid for both OS
    # this will not be defined in the Concrete Classes
    # since it doesnt differ for different OS, but same for all.
    def __init__(self):
        print("Operating System: " + type(self).__name__[-3:])

    @abstractmethod
    def create_button(self) -> AbstractFactory_Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> AbstractFactory_Checkbox:
        pass


class ConcreteFactory_Win(AbstractFactory_OS):


    # Although concrete factories instantiate concrete products,
    # signatures of their creation methods must return corresponding abstract products. 
    def create_button(self) -> AbstractFactory_Button:
        print("WindowsButton is created")
        return ConcreteFactory_WindowsButton()

    def create_checkbox(self) -> AbstractFactory_Checkbox:
        print("WindowsCheckbox is created")
        return ConcreteFactory_WindowsCheckbox()


class ConcreteFactory_Mac(AbstractFactory_OS):

    def create_button(self) -> AbstractFactory_Button:
        print("MacButton is created")
        return ConcreteFactory_MacButton()

    def create_checkbox(self) -> AbstractFactory_Checkbox:
        print("MacCheckbox is created")
        return ConcreteFactory_MacCheckbox()


#button
class AbstractFactory_Button(ABC):
    
    @abstractmethod
    def click(self):
        pass

"""
Concrete Products are created by corresponding Concrete Factories.
"""

class ConcreteFactory_WindowsButton(AbstractFactory_Button):

    def click(self):
        print("WindowsButton is clicked")


class ConcreteFactory_MacButton(AbstractFactory_Button):

    def click(self):
        print("MacButton is clicked")


# checkbox

class AbstractFactory_Checkbox(ABC):

    @abstractmethod
    def check(self):
        pass

class ConcreteFactory_WindowsCheckbox(AbstractFactory_Checkbox):

    def check(self):
        print("WindowsCheckbox is checked")


class ConcreteFactory_MacCheckbox(AbstractFactory_Checkbox):

    def check(self):
        print("MacCheckbox is checked")


def client(factory: AbstractFactory_OS):

    button = factory.create_button()
    button.click()

    checkbox = factory.create_checkbox()
    checkbox.check()



if __name__ == '__main__':

    os1 = ConcreteFactory_Win()
    client(os1)

    os2 = ConcreteFactory_Mac()
    client(os2)