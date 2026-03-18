# Student Report Card - Python OOPs
# Author: B. Sriram

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, mark):
        if mark < 0 or mark > 100:
            print(f"Invalid mark for {subject}. Marks must be between 0 and 100.")
        else:
            self.marks[subject] = mark

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total() / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        else:
            return "F (Fail)"

    def display_report(self):
        print("\n=============================")
        print("        REPORT CARD          ")
        print("=============================")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print("-----------------------------")
        print(f"{'Subject':<20} {'Marks':>5}")
        print("-----------------------------")
        for subject, mark in self.marks.items():
            print(f"{subject:<20} {mark:>5}")
        print("-----------------------------")
        print(f"{'Total':<20} {self.calculate_total():>5}")
        print(f"{'Average':<20} {self.calculate_average():>5.2f}")
        print(f"{'Grade':<20} {self.get_grade():>5}")
        print("=============================\n")


class MedicalStudent(Student):
    def __init__(self, name, roll_number, internship_score):
        super().__init__(name, roll_number)
        self.internship_score = internship_score

    def display_report(self):
        print("\n=============================")
        print("   MEDICAL STUDENT REPORT    ")
        print("=============================")
        print(f"Name             : {self.name}")
        print(f"Roll Number      : {self.roll_number}")
        print(f"Internship Score : {self.internship_score}/100")
        print("-----------------------------")
        print(f"{'Subject':<20} {'Marks':>5}")
        print("-----------------------------")
        for subject, mark in self.marks.items():
            print(f"{subject:<20} {mark:>5}")
        print("-----------------------------")
        print(f"{'Total':<20} {self.calculate_total():>5}")
        print(f"{'Average':<20} {self.calculate_average():>5.2f}")
        print(f"{'Internship Score':<20} {self.internship_score:>5}")
        print(f"{'Grade':<20} {self.get_grade():>5}")
        print("=============================\n")


# Main Program
print("========== STUDENT REPORT CARD SYSTEM ==========\n")

# Student 1
s1 = Student("B. Sriram", "ECE001")
s1.add_marks("Mathematics", 92)
s1.add_marks("Physics", 88)
s1.add_marks("Chemistry", 76)
s1.add_marks("English", 85)
s1.add_marks("Programming", 95)

# Student 2
s2 = Student("Ravi Kumar", "ECE002")
s2.add_marks("Mathematics", 70)
s2.add_marks("Physics", 65)
s2.add_marks("Chemistry", 72)
s2.add_marks("English", 68)
s2.add_marks("Programming", 80)

# Student 3 - Medical Student
s3 = MedicalStudent("Priya Sharma", "MED001", 88)
s3.add_marks("Biology", 91)
s3.add_marks("Chemistry", 87)
s3.add_marks("Physics", 83)
s3.add_marks("English", 79)
s3.add_marks("Anatomy", 94)

# Display all report cards
s1.display_report()
s2.display_report()
s3.display_report()

# Find highest average
students = [s1, s2, s3]
topper = max(students, key=lambda s: s.calculate_average())
print(f"🏆 Highest Average: {topper.name} with {topper.calculate_average():.2f}%")
print("=================================================")