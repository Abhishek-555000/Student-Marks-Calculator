print(" ============================== ")
print("   STUDENT MARKS CALCULATOR ")
print(" ============================== ")

name = input("\nEnter student name: ")
usn = input("Enter student USN: ")

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
m4 = int(input("Enter subject 4 marks: "))
m5 = int(input("Enter subject 5 marks: "))

if not all(0 <= mark <= 100 for mark in [m1, m2, m3, m4, m5]):
    print("\nInvalid marks! Enter marks between 0 and 100.")
    exit()

total = m1+m2+m3+m4+m5
percentage = (total/500)*100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >=70:
    grade = "B"
elif percentage >=60:
    grade = "C"
elif percentage >=40:
    grade = "D"
else:
    grade = "Fail"

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("\n =============================== ")
print("        RESULT SUMMARY        ")
print(" =============================== ")
print("\nStudent name: ", name)
print("\nSubject 1 marks: ", m1)
print("Subject 2 marks: ", m2)
print("Subject 3 marks: ", m3)
print("Subject 4 marks: ", m4)
print("Subject 5 marks: ", m5)
print("\nUSN: ", usn)
print("\nTotal marks: ", total, "/500")
print("\nPercentage: ", percentage, "%")
print("\nGrade: ", grade)
print("\nResult: ", result)
