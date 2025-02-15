import pandas as pd
import time
from faker import Faker

class StudentDirectory:
    def __init__(self):
        self.students = pd.DataFrame(columns=['NIF', 'Name', 'Last Name', 'Phone', 'Email', 'Approved'])
        self.faker = Faker()

    def add_student(self):
        nif = input("Enter the NIF: ")
        name = input("Enter the Name: ")
        last_name = input("Enter the Last Name: ")
        phone = input("Enter the Phone: ")
        email = input("Enter the Email: ")
        
        new_student = {
            'NIF': nif, 
            'Name': name, 
            'Last Name': last_name, 
            'Phone': phone, 
            'Email': email, 
            'Approved': False
        }
        self.students = pd.concat([self.students, pd.DataFrame([new_student])], ignore_index=True)
        print("Student added successfully!")

    def remove_student(self):
        nif = input("Enter the NIF of the student to remove: ")
        if self.students[self.students['NIF'] == nif].empty:
            print(f"Student with NIF {nif} not found.")
        else:
            self.students = self.students[self.students['NIF'] != nif]
            print(f"Student with NIF {nif} removed.")

    def update_student(self):
        nif = input("Enter the NIF of the student to update: ")
        if self.students[self.students['NIF'] == nif].empty:
            print(f"Student with NIF {nif} not found.")
            return

        print("Updating student information:")
        idx = self.students[self.students['NIF'] == nif].index[0]
        self.students.at[idx, 'Name'] = input(f"Enter new Name (current: {self.students.at[idx, 'Name']}): ") or self.students.at[idx, 'Name']
        self.students.at[idx, 'Last Name'] = input(f"Enter new Last Name (current: {self.students.at[idx, 'Last Name']}): ") or self.students.at[idx, 'Last Name']
        self.students.at[idx, 'Phone'] = input(f"Enter new Phone (current: {self.students.at[idx, 'Phone']}): ") or self.students.at[idx, 'Phone']
        self.students.at[idx, 'Email'] = input(f"Enter new Email (current: {self.students.at[idx, 'Email']}): ") or self.students.at[idx, 'Email']
        print(f"Student with NIF {nif} updated successfully.")

    def show_student_by_nif(self):
        nif = input("Enter the NIF: ")
        student = self.students[self.students['NIF'] == nif]
        if student.empty:
            print(f"Student with NIF {nif} not found.")
        else:
            print(student)

    def show_student_by_email(self):
        email = input("Enter the Email: ")
        student = self.students[self.students['Email'] == email]
        if student.empty:
            print(f"Student with Email {email} not found.")
        else:
            print(student)

    def list_all_students(self):
        if self.students.empty:
            print("No students available.")
        else:
            print("List of all students:")
            print(self.students)

    def approve_student(self):
        nif = input("Enter the NIF of the student to approve: ")
        if self.students[self.students['NIF'] == nif].empty:
            print(f"Student with NIF {nif} not found.")
        else:
            self.students.loc[self.students['NIF'] == nif, 'Approved'] = True
            print(f"Student with NIF {nif} approved.")

    def suspend_student(self):
        nif = input("Enter the NIF of the student to suspend: ")
        if self.students[self.students['NIF'] == nif].empty:
            print(f"Student with NIF {nif} not found.")
        else:
            self.students.loc[self.students['NIF'] == nif, 'Approved'] = False
            print(f"Student with NIF {nif} suspended.")

    def show_approved_students(self):
        approved_students = self.students[self.students['Approved']]
        if approved_students.empty:
            print("No approved students found.")
        else:
            print("List of approved students:")
            print(approved_students)

    def show_suspended_students(self):
        suspended_students = self.students[~self.students['Approved']]
        if suspended_students.empty:
            print("No suspended students found.")
        else:
            print("List of suspended students:")
            print(suspended_students)


def menu():
    menu_titles = {
        '1': "Add New Student",
        '2': "Remove Student",
        '3': "Update Student Information",
        '4': "Show Student by NIF",
        '5': "Show Student by Email",
        '6': "List All Students",
        '7': "Approve Student",
        '8': "Suspend Student",
        '9': "Show Approved Students",
        '10': "Show Suspended Students"
    }
    
    print('\n-----------------------')
    for key, title in menu_titles.items():
        print(f"({key}) {title}")
    print("(X) Exit Program")
    print('-----------------------\n')

def student_directory_app():
    directory = StudentDirectory()
    options = {
        '1': directory.add_student,
        '2': directory.remove_student,
        '3': directory.update_student,
        '4': directory.show_student_by_nif,
        '5': directory.show_student_by_email,
        '6': directory.list_all_students,
        '7': directory.approve_student,
        '8': directory.suspend_student,
        '9': directory.show_approved_students,
        '10': directory.show_suspended_students,
    }
    
    print("\n=== STUDENT DIRECTORY ===")
    print("=== View and manage student data ===\n")
    
    while True:
        menu()
        print('What would you like to do?')
        option = input("Choose an option: ").lower()

        if option == 'x':
            print("\nExiting the program...")
            print('-----------------------')
            break
        elif option in options:
            options[option]()
            time.sleep(0.5)  # Pequeña pausa entre operaciones
        else:
            print("Oops! That's not a valid option. Try again...\n")

if __name__ == "__main__":
    student_directory_app()