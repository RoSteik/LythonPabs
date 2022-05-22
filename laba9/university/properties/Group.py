""" 
Created by RoSteik (Telegram: @Rosteik)
"""
from university.properties import Institute


class Group:

    def __init__(self, institute: Institute, name: str, number_of_students: int, average_progress: float,
                 schedule: str):
        self.__institute = institute
        self.__name = name
        self.__average_progress = average_progress
        self.__number_of_students = number_of_students
        self.__schedule = schedule

    def organize_a_trip(self):
        print('Pay 1000$ and we will say information later')
