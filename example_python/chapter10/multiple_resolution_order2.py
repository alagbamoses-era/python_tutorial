#!/usr/bin/python3

class LoggingMixin:
    def save(self):
        print('Logging save')
        super().save()

class SaveMixin:
    def save(self):
        print('Saving data')
        super().save()

class Base:
    def save(self):
        print('Base save')
        

class MyModel(LoggingMixin, SaveMixin, Base):
    pass

obj = MyModel()
obj.save()
print(MyModel.mro())


