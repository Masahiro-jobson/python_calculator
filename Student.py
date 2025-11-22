# class student -> what student is
class Student:
    # self is an instance of object created by another class.py
    def __init__(this, name, age, major, gpa, is_on_probation ):
        this.name = name
        this.age = age
        this.major = major
        this.gpa = gpa
        this.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
