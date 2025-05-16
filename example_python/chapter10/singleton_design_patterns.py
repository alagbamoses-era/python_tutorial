#!/usr/bin/python3



class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj = Singleton()
obj2 = Singleton()
print(obj is obj2)



class House:
    _living_room = None

    def __new__(cls):
        if cls._living_room is None:
            cls._living_room = 10
        return cls._living_room

house = House()

house2 = House()

print(house is house2)
print(house)






