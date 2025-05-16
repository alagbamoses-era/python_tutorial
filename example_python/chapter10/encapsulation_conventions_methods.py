#!/usr/bin/python3


# Public Method

class MyClass:
    def public_method(self):
        print('This is a Public methos.')

# Protected Method

class MyClass2:
    def _protected_method(self):
        return 'This is a protected method'
        

    def public_method_2(self):
        print(self._protected_method())

# Private method

class MyClass:
    def __private_method(self):
        return 'This is a private method.'
        

    def public_method(self):
        print(self.__private_method())

    
obj = MyClass()
#obj.__private_method() # Raises AttributeError

obj.public_method()

obj2 = MyClass2()
obj2.public_method_2()

