students = {}

#____________DEFINING NECESSARY FUNCTIONS____________

def S_add_stud():
    stud_id = input("Enter Student ID: ")
    
    if stud_id in students:
        print("Student ID already exists..")
        return
    
    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            break
        except ValueError:
            print("Please enter valid numbers for age...")
    
    students[stud_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    
    print("Student added successfully!")

def S_del_stud():
    stud_id = input("Enter Student ID: ")
    
    if stud_id in students:
        confirm = input("Are you sure you want to remove student " + stud_id + "? (y/n): ")
        if confirm.lower() == 'y':
            del students[stud_id]
            print("Student removed successfully!")
        else:
            print("Removal cancelled.")
    else:
        print("Student ID not found!")

def S_update_stud():
    stud_id = input("Enter Student ID: ")
    
    if stud_id in students:
        print("What would you like to update?")
        print("1.Name")
        print("2.Age")
        print("3.Grade")
        
        choice = input("Enter your choice (1-3):")
        
        if choice == "1":
            new_name = input("Enter new name: ")
            students[stud_id]["name"] = new_name
            print("Name updated successfully!")
        elif choice == "2":
            while True:
                try:
                    new_age = int(input("Enter new age: "))
                    students[stud_id]["age"] = new_age
                    print("Age updated successfully.")
                    break
                except ValueError:
                    print("Please enter a valid integer for age.")
        elif choice == "3":
            new_grade = input("Enter new grade: ")
            students[stud_id]["grade"] = new_grade
            print("Grade updated successfully!")
        else:
            print("Invalid choice!")
    else:
        print("Error: Student ID not found!")

def S_search_stud():
    print("Search by:")
    print("1. ID")
    print("2. Name")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        stud_id = input("Enter Student ID: ")
        if stud_id in students:
            S_show_stud(stud_id, students[stud_id])
        else:
            print("Error: Student ID not found!")

    elif choice == "2":
        name = input("Enter student name: ")
        found = False
        for stud_id, info in students.items():
            if info["name"].lower() == name.lower():
                S_show_stud(stud_id, info)
                found = True
        if not found:
            print("Error: No student found with that name!")
    else:
        print("Invalid choice!")

def S_show_stud(stud_id, info):
    print("ID: " + stud_id + " | Name: " + info['name'] + " | Age: " + str(info['age']) + " | Grade: " + info['grade'])

def S_show_all():
    if len(students)==0:
        print("No students in the system.")
        return
    
    print("\n--- Student List ---")
    for stud_id, info in students.items():
        S_show_stud(stud_id, info)
    print("-------------------")

#_____________________ACTUAL PROGRAM______________________________

print("Welcome to the Student Management System")
print("Made by: Shaurya Pratap Singh : CC-51")
print("----------------------------------------")

while True:
    print("1.Add Student")
    print("2.Remove Student")
    print("3.Update Student")
    print("4.Search Student")
    print("5.Display All Students")
    print("6.Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        S_add_stud()
    elif choice == "2":
        S_del_stud()
    elif choice == "3":
        S_update_stud()
    elif choice == "4":
        S_search_stud()
    elif choice == "5":
        S_show_all()
    elif choice == "6":
        print("Exiting...")
        print("Goodbye!")
        print("----------------------------------------")
        break
    else:
        print("Invalid choice! Please try again.")
    
    print("-------------------------------------------")