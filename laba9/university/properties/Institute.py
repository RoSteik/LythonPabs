""" 
Created by RoSteik (Telegram: @Rosteik)
"""
from university.properties.EducationalPlace import EducationalPlace


class Institute(EducationalPlace):

    def __init__(self, name: str, specialty: str, specialization: str, cathedra: str, is_private: bool, location: str,
                 students_number: int):
        super().__init__(is_private, location, students_number)
        self.__specialty = specialty
        self.__specialization = specialization
        self.__cathedra = cathedra
        self.__name = name

    def enroll_student(self, name):
        print(f'Student {name} is enrolled')

    def make_schedule(self):
        print('Schedule is made')

    def calculate_average_progress_of_student(self, name: str, mark: int):
        print(f'{name} has progress -  {mark}')
