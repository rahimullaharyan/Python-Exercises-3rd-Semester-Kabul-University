import csv

students = [
    {"student_id": "101", "name": "Aryan Khan", "midterm": 35, "final": 45},
    {"student_id": "102", "name": "Ahmad Ali", "midterm": 20, "final": 25},
    {"student_id": "103", "name": "Ali, Mohammad", "midterm": 40, "final": 50},
    {"student_id": "104", "name": "Hamid Rahimi", "midterm": 15, "final": 20},
    {"student_id": "105", "name": "Farid Khan!", "midterm": 30, "final": 35}
]

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["student_id", "name", "midterm", "final"])
    writer.writeheader()
    writer.writerows(students)

results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        midterm = int(student["midterm"])
        final = int(student["final"])

        total = midterm + final
        average = total / 2

        results.append({
            "student_id": student["student_id"],
            "name": student["name"],
            "total": total,
            "average": average
        })

threshold = float(input("Enter passing threshold: "))

print("\nStudents who passed:")

for student in results:
    if student["average"] >= threshold:
        print(student["name"], student["average"])

with open("results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["student_id", "name", "total", "average"]
    )

    writer.writeheader()
    writer.writerows(results)

print("\nResults saved successfully!")