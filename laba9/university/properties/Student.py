"""
Created by RoSteik (Telegram: @Rosteik)
"""
from university.properties.Group import Group


class Student:

    def __init__(self, name: str, surname: str, group: Group, progress: float):
        self.__progress = progress
        self.__surname = surname
        self.__name = name
        self.__group = group

    def __repr__(self):
        return f'Student - {self.__name} {self.__surname} has average progress {self.__progress}'

    def do_homework(self):
        print('Homework is done')


