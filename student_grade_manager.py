print("===================================")
print("       STUDENT GRADE MANAGER")
print("===================================")

student_name = input("Enter Student Name: ")

print("\nEnter marks for each subject (0 - 100)")

tamil = float(input("Tamil Marks   : "))
english = float(input("English Marks : "))
maths = float(input("Maths Marks   : "))
science = float(input("Science Marks : "))
social = float(input("Social Marks  : "))

total = tamil + english + maths + science + social

average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"

print("\n===================================")
print("           STUDENT RESULT")
print("===================================")

print(f"Student Name : {student_name}")
print("-----------------------------------")
print(f"Tamil        : {tamil}")
print(f"English      : {english}")
print(f"Maths        : {maths}")
print(f"Science      : {science}")
print(f"Social       : {social}")
print("-----------------------------------")
print(f"Total Marks  : {total} / 500")
print(f"Percentage   : {average:.2f}%")
print(f"Grade        : {grade}")
print("===================================")