# Grade calculator

student_grade =int(input("Enter the student's percentage: "))
if student_grade >= 90:
    print("This scudent is has A grade")
elif student_grade >= 80 and student_grade < 90:
    print("This student's grade is B")
elif student_grade >= 70 and student_grade < 80:
    print("This student's grade is C")
elif student_grade >= 60 and student_grade < 70:
    print("This student's grade is D")
else:
    print("This student flunked the test with F grade")