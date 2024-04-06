#CTI-110
#P2HW2 - Lists
#Landon Smith
#10/10/2023
#Line 7 creates a list for the grades to be stored in.
Grades = []
#All odd numbered lines from line 9 - 19 simply asks for the users input of their grade All even numbered lines from lines 10-20 put each user input into the list created above..
Module1 = float(input("Enter grade for Module 1:"))
Grades.append(Module1)
Module2 = float(input("Enter grade for Module 2:"))
Grades.append(Module2)
Module3 = float(input("Enter grade for Module 3:"))
Grades.append(Module3)
Module4 = float(input("Enter grade for Module 4:"))
Grades.append(Module4)
Module5 = float(input("Enter grade for Module 5:"))
Grades.append(Module5)
Module6 = float(input("Enter grade for Module 6:"))
Grades.append(Module6)
#Lines 22-26 find the specefics of the list such as the average, sum, min, and max of the given values.
lowest_grade = min(Grades)
highest_grade = max(Grades)
total_sum = sum(Grades)
average_grades = sum(Grades)/len(Grades)
rounded_grades= round(average_grades,2)
#Lines 28-32 simply print the users grade information which is created fromlines 17-21.
print("---------Results---------")
print("Lowest Grade:",lowest_grade)
print("Highest Grade:", highest_grade)
print("Sum of Grades:", total_sum)
print("Average:", rounded_grades)