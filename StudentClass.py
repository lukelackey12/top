"""
Create a student class (name the file StudentClass.py). The class
should have 4 attributes. StudentID, Name, DOB and classification
(F,S,Jr,Sr).
• Create a method that will calculate the student’s current age
• Create a method that will determine when the student can
register –
• Seniors – 4/1 thru 4/3
• Juniors – 4/4 thru 4/6
• Sophomores – 4/7 thru 4/9
• Freshmen – 4/10 thru 4/12
• Create a method to return the age and another method to return
the registration dates.
Create a program file (name the file StudentProgram.py) that will
create an instance of the student class and display the age of the
student and when they can register.
"""
from datetime import datetime, timedelta


class student:

    def __init__(self, id, name, dob, year):
        self.studentID = id
        self.name = name
        self.date = dob
        self.year = year

    def calc_age(self):
        now = datetime.now()
        birthday = datetime.strptime(self.date, "%m-%d-%Y")
        difference = now - birthday
        self.date = difference.days // 365
        return self.date
    
    def get_registration(self):
        if self.year == 'Senior':
            return '4/1 to 4/3'
        elif self.year == 'Junior':
            return '4/4 to 4/6.'
        elif self.year == 'Sophomore':
            return '4/7 to 4/9.'
        elif self.year == 'Freshman':
            return '4/10 to 4/12'
        else:
            print('Invalid year. Please enter Senior, Junior, Sophomore, or Freshman.')


