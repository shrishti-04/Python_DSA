# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

# Examples

# grades = 84 round to 85 (85 - 84 is less than 3)
# grades = 29 do not round (result is less than 40)
# grades = 57 do not round (60 - 57 is 3 or higher)
# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

# Sample Input 0

# 4
# 73
# 67
# 38
# 33
# Sample Output 0

# 75
# 67
# 40
# 33

def gradingRound(grades):
    for i in range(len(grades)):
        if(grades[i] < 38):
            continue
        elif(5-grades[i]%5 >= 3):
            continue
        else:
            grades[i] += 5-grades[i]%5
            
    print(grades)

gradingRound([58, 74, 35, 98, 86])
    
