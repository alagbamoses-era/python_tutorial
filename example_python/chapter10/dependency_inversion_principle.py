#!/usr/bin/python3 

from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f'{data}: Saving to MYSQL')

class Service:
    def __init__(self, db: Database):
        self.db = db

    def save_data(self, data):
        self.db.save(data)


sql_db = MySQLDatabase()
service = Service(sql_db)

service.save_data('userdata')


