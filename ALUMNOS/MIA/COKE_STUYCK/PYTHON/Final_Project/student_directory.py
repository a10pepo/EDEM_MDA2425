import pandas as pd
import time
from termcolor import colored
from functions import make_header, ask_input
from faker import Faker

class StudentDirectory:
    def __init__(self):
        # Initialize an empty DataFrame for students
        self.students = pd.DataFrame(columns=['NIF', 'Name', 'Last Name', 'Phone', 'Email', 'Approved'])
        self.faker = Faker()  # Initialize Faker for random data generation
        print("Initialized Student Directory with columns:", self.students.columns.tolist())

    def generate_random_students(self, count=18):
        for _ in range(count):
            nif = self.faker.ssn()  # Generate a random NIF (SSN for demonstration)
            name = self.faker.first_name()
            last_name = self.faker.last_name()
            phone = self.faker.phone_number()
            
            # Create the email in the format: name.lastname@domain.com
            email = f"{name.lower()}.{last_name.lower()}@example.com"
            
            new_student = {
                'NIF': nif, 
                'Name': name, 
                'Last Name': last_name, 
                'Phone': phone, 
                'Email': email, 
                'Approved': self.faker.boolean()
            }
            # Use pd.concat to add new student to DataFrame
            self.students = pd.concat([self.students, pd.DataFrame([new_student])], ignore_index=True)
        print(f"{count} random students added successfully.")

    def add_student(self):
        nif = input("Enter the NIF: ")
        name = input("Enter the Name: ")
        last_name = input("Enter the Last Name: ")
        phone = input("Enter the Phone: ")
        
        # Create the email in the format: name.lastname@domain.com
        email = f"{name.lower()}.{last_name.lower()}@example.com"
        
        new_student = {
            'NIF': nif, 
            'Name': name, 
            'Last Name': last_name, 
            'Phone': phone, 
            'Email': email, 
            'Approved': False
        }
        # Use pd.concat to add new student to DataFrame
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
        # Email is not updated here as it is generated from Name and Last Name
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
        if self.students.empty:
            print("No students available.")
            return
        approved_students = self.students[self.students['Approved'] == True]
        if not approved_students.empty:
            print("List of approved students:")
            print(approved_students)
        else:
            print("No approved students found.")

    def show_suspended_students(self):
        if self.students.empty:
            print("No students available.")
            return
        suspended_students = self.students[self.students['Approved'] == False]
        if not suspended_students.empty:
            print("List of suspended students:")
            print(suspended_students)
        else:
            print("No suspended students found.")


def menu():
    
    menu_titles = {
        '0': "Generate Random Students",
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
    
    print('''
-----------------------
''')
    for key in menu_titles.keys():
        print(f"({key}) {menu_titles[key]}")
    print("(X) Exit Program")
    print('''
-----------------------
''')
def student_directory_app():
    directory = StudentDirectory()
    options = {
        '0': directory.generate_random_students,  # Added option for random students
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
    
    firstTime = True
    while True:
        if firstTime:
            make_header("STUDENT DIRECTORY", "View and manage student data.", bg_color='cyan')    
            menu()
            print('What would you like to do?')
            firstTime = False
        else:
            time.sleep(1)
            menu()
            print('What would you like to do now?')

        option = input("Choose an option: ").lower()

        if option == 'x':
            print("Exiting the program...")
            print('''
-----------------------
''')
            break
        elif option in options:
            if option == '0':  # If option 0 is selected, call with count parameter
                options[option](count=18)  # Call with count of 18
            else:
                options[option]()
        else:
            print(colored("Oops! That's not a valid option. Try again...\n", 'red'))

if __name__ == "__main__":
    student_directory_app()
