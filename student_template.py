# Requirements
# 1. Setup virtual environment for python 3 and use that virtual env
# 2. Update the below script
#### Out put from "python student.py"
#### student name: John Doe
#### student age: 21
#### student average score: 85.0
# 3. Debug

import requests
from argparse import RawTextHelpFormatter
from getpass import getpass


class Student:
    # class attribute schoolname
    schoolName = 'XYZ School'

    # private class attribute to store average score
    -->

    # Constructor
    # Take 2 arguments: name, age
    # assign to instance attribute name and age
    # Has an extra attribute name "classes" (type dict) has these values "ENG 101":90, "MATH 101":80
    def __init__(self, name, age):


    # Display student's age
    # Print stdout EX: "student age: 34"
    def display_age(self):

    # Private method for calculating average score
    # read those score from dict classes and divide to number of classes
    # return average_score
    def __calculate_average_score(self):

    # Diplay average score
    # Ex: student average score
    # Call function _calculate_average_score()
    # and assign return value to __average_score
    def display_average_score(self):

if __name__ == "__main__":
    std =Student("John Doe", 21)
    print(f"student name: {std.name}")
    std.display_age()
    std.display_average_score()


