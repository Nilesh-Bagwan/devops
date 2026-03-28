def student_grades():
    
    # initial dictionary to store student names and their grades
    student_dict = {}
    
    while True:
        
        print("\n--- Student Grade Manager ---")
        print("1. Add student and grade")
        print("2. Update/Modify any existing student's grade")
        print("3. View all students and grades")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n--- Add Student and Grade ---")
            new_student = input("Enter student name: ")
            try:
                new_grade = float(input(f"Enter grade for {new_student}: "))    
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
                continue
            student_dict[new_student] = new_grade
            print(f"Added {new_student} with grade {new_grade}.")
            
        elif choice == '2':
            print("\n--- Update Student Grade ---")
            print("\nList of students:")
            for name in student_dict:
                print(f"- {name}")
                
            student_name = input("\nEnter the name of the student to update: ")
            if student_name in student_dict:
                try:
                    new_grade = float(input(f"Enter the new grade for {student_name}: "))
                    student_dict[student_name] = new_grade
                    print(f"Grade for {student_name} updated successfully.")
                except ValueError:
                    print("Invalid grade. Please enter a numeric value.")
            else:
                print(f"Student {student_name} not found.")

        elif choice == '3':
            if student_dict:
                print("\n--- Student Grades ---")
                for name, grade in student_dict.items():
                    print(f"{name}: {grade}")
            else:
                print("No students found.")
                break
        
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
        
if __name__ == "__main__":
    student_grades()
