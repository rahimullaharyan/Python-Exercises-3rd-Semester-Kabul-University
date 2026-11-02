students = [
    "101, Aryan, Computer Science",
    "102, Ahmad, Mathematics",
    "103, Ali, Physics",
    "104, Hamid, Chemistry",
    "105, Farid, Biology"
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

try:
    with open("students.txt", "r") as file:
        records = file.readlines()

    for record in records:
        print(record.strip())

except FileNotFoundError:
    print("File does not exist!")

search_id = input("Enter student ID to search: ")

try:
    with open("students.txt", "r") as file:
        found = False

        for record in file:
            student = record.strip().split(",")

            if student[0] == search_id:
                print("Student Found:", record.strip())
                found = True
                break

        if not found:
            print("Student not found!")

except FileNotFoundError:
    print("File does not exist!")

new_student = "106, Bilal, Computer Science"

with open("students.txt", "a") as file:
    file.write(new_student + "\n")

print("New student added successfully!")

try:
    with open("students.txt", "r") as file:
        total = sum(1 for record in file)

    print("Total Student Records:", total)

except FileNotFoundError:
    print("File does not exist!")