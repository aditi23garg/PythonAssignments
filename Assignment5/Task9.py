students = {"Aman": 92, "Shalu": 56, "Alice": 67, "John": 45, "Rohan": 82,"Lina": 90}
student = input("Enter the student's name:")
if student in students:
    print(student+"'s marks:",students[student])
else:
    print("Student not found.")