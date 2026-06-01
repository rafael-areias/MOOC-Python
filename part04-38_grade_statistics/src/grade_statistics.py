# Write your solution here
def input_from_user():
    exam = []
    exercises = []
    total_grade = []
    while True:
        question = input("Exam points and exercises completed: ")
        if question == "":
            break
        question_format = question.split()
        exam.append(int(question_format[0]))
        exercises.append(int(float(question_format[1])/10))
        total_grade.append(int(question_format[0])+int(float(question_format[1])/10))

    return exam, exercises, total_grade

def analyse_grades(exam, exercises, total_grade):
    pass_perc = []
    G5 = ""
    G4 = ""
    G3 = ""
    G2 = ""
    G1 = ""
    G0 = ""
    for i in range(len(total_grade)):
        if total_grade[i] > 14 and exam[i] >= 10:
            pass_perc.append(i)
        if total_grade[i] <= 14 or exam[i] < 10:
            G0 += "*"
        elif total_grade[i] <= 17 and exam[i] >= 10:
            G1 += "*"
        elif total_grade[i] <= 20 and exam[i] >= 10:
            G2 += "*"
        elif total_grade[i] <= 23 and exam[i] >= 10:
            G3 += "*"
        elif total_grade[i] <= 27 and exam[i] >= 10:
            G4 += "*"
        else:
            G5 += "*"
    
    return G0, G1, G2, G3, G4, G5, pass_perc


def print_result(exam, exercises, total_grade,G0, G1, G2, G3, G4, G5, pass_perc):
    print("Statistics:")
    print(f"Points average: {((sum(exam)+(float(sum(exercises))))/len(exam)):.1f}")
    print(f"Pass percentage: {(len(pass_perc)/len(total_grade))*100:.1f}")
    print("Grade distribution:")
    print(f"  5: {G5}")
    print(f"  4: {G4}")
    print(f"  3: {G3}")
    print(f"  2: {G2}")
    print(f"  1: {G1}")
    print(f"  0: {G0}")

def main ():
    exam, exercises, total_grade = input_from_user()
    G0, G1, G2, G3, G4, G5, pass_perc = analyse_grades(exam, exercises, total_grade)
    print_result(exam, exercises, total_grade,G0, G1, G2, G3, G4, G5, pass_perc)

main()









## Solution

def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]
 
def exercise_points(amount):
    return amount // 10
 
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
 
def mean(points):
    return sum(points) / len(points)
 
def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()
 
