students=[{"name": "Alice", "marks": 90, "grade": "O"}, {"name": "Bob", "marks": 85, "grade": "A"}, {"name": "Charlie", "marks": 78, "grade": "B"}, {"name": "David", "marks": 92, "grade": "O"}]
class Student:
    def add_student(students, name, marks, grade):
        students.append({"name": name, "marks": marks, "grade": grade})
    def show_all(students):
        for student in students:
            print("Name: "+student["name"]+", Marks: "+str(student["marks"])+", Grade: "+student["grade"])
        return students
    def find_topper(students):
        topper = max(students, key=lambda x: x["marks"])
        print("Topper: "+topper["name"]+", Marks: "+str(topper["marks"])+", Grade: "+topper["grade"])
        return topper

    def find_average(students):
        average_marks = sum(student["marks"] for student in students) / len(students)
        print("Average Marks: "+str(average_marks))
print(Student.add_student(students,"madhesh",87,"A"))
print(Student.show_all(students))
print(Student.find_topper(students))
print(Student.find_average(students))