import json
from pathlib import Path
import shutil

FILE = Path("students.json")
BACKUP = Path("students_backup.json")


def load_students():
    if not FILE.exists():
        return []

    try:
        with FILE.open("r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("File is missing or corrupted!")
        return []


def save_students(students):
    if FILE.exists():
        shutil.copy(FILE, BACKUP)

    with FILE.open("w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student_id = input("Enter student ID: ")

    if not student_id.isdigit():
        print("Invalid student ID!")
        return

    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter name: ").strip()
    department = input("Enter department: ").strip()
    semester = input("Enter semester: ").strip()

    if not name or not department or not semester:
        print("All fields are required!")
        return

    student = {
        "student_id": student_id,
        "name": name,
        "department": department,
        "semester": semester
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def list_students():
    students = load_students()

    if not students:
        print("No students found!")
        return

    for student in students:
        print("\nID:", student["student_id"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Semester:", student["semester"])


def search_student():
    students = load_students()

    student_id = input("Enter student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["student_id"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Semester:", student["semester"])
            return

    print("Student not found!")


def update_student():
    students = load_students()

    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["student_id"] == student_id:
            name = input("Enter new name: ").strip()
            department = input("Enter new department: ").strip()
            semester = input("Enter new semester: ").strip()

            if not name or not department or not semester:
                print("All fields are required!")
                return

            student["name"] = name
            student["department"] = department
            student["semester"] = semester

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student():
    students = load_students()

    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found!")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. List Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            list_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main()