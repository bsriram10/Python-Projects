class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def add_marks(self,subject,mark):
        self.marks[subject] = mark
    def calculate_average(self):
        total_marks = sum(self.marks.values())
        average = total_marks / len(self.marks)
        return average
    def calculate_total_marks(self):
        total_marks = sum(self.marks.values())
        return total_marks
    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Average Marks: {self.calculate_average()}")
        print(f"Total Marks: {self.calculate_total_marks()}")
        print(f"Grade: {self.get_grade()}")
class MedicalStudent(Student):
    def __init__(self,name,roll_number,marks,medical_field):
        super().__init__(name,roll_number,marks)
        self.medical_field = medical_field
    def display_info(self,internship_status):
        super().display_info()
        print(f"Medical Field: {self.medical_field}")
        print(f"Internship Status: {internship_status}")

# Example usage
student1 = Student("Alice", 101, {"Math": 85, "Science": 90, "English": 78})
student1.display_info()

medical_student1 = MedicalStudent("Bob", 102, {"Math": 80, "Science": 85, "English": 82}, "Cardiology")
medical_student1.display_info("Completed")