""" 
Created by RoSteik (Telegram: @Rosteik)
"""
from abc import ABC, abstractmethod


class EducationalPlace(ABC):

    def __init__(self, is_private: bool, location: str, students_number: int):
        self.__is_private = is_private
        self.__location = location
        self.__students_number = students_number

    @abstractmethod
    def enroll_student(self, name: str):
        pass

    @abstractmethod
    def make_schedule(self):
        pass
