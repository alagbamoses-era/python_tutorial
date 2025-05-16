#!/usr/bin/python3

###behavioural patters

class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class Observer:
    def update(self, data):
        print('Got data: ', data)


subject = Subject()
observer = Observer()
updated = observer.update('maths')


maths = subject.register(updated)
print(subject.self.observers)

updated_subject = subject.notify(maths)

print(updated_subject)

