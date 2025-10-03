gradedict = {"abhishek": "A", "Nitin": "B", "Rohan": "C", "Rahul": "D"}

operation = input("Enter the operation (add/update): ")

print(gradedict)

if operation == "add":
    name = input("Enter the name: ")
    grade = input("Enter the grade: ")
    gradedict[name] = grade
    print("Grade added successfully.")
    print(gradedict)
elif operation == "update":
    name = input("Enter the name: ")
    if name in gradedict:
        grade = input("Enter the new grade: ")
        gradedict[name] = grade
        print("Grade updated successfully.")
        print(gradedict)

    else:
        print("Name not found.")
else:
    print("Invalid operation.")
