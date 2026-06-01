# Write your solution here
exam = []
exercises = []
total_grade = []
while True:
    question = input("Exam points and exercises completed: ")
    if question == "":
        break
    question_format = int(question.split())
    exam.append(int(question_format[0]))
    exercises.append(int(question_format[1]))
    total_grade.append(sum(int(question_format)))

print("Statistics:")
print(f"Points average: {((sum(exam)+(float(sum(exercises)/10)))/len(exam)):.2f}")
print(f"Pass percentage: {total_grade}")

