print("===== AI BASED CGPA PREDICTOR =====")

import numpy as np
from sklearn.tree import DecisionTreeClassifier

n = int(input("Enter number of students: "))
marks_list = [float(input(f"Enter marks of student {i+1}: ")) for i in range(n)]

marks_arr = np.array(marks_list)
mean = np.mean(marks_arr)
std  = np.std(marks_arr, ddof=0) 

print(f"\nClass Mean: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")

def assign_grade(m, mean, std):
    if   m >= mean + 1.5 * std: return "S"
    elif m >= mean + 0.5 * std: return "A"
    elif m >= mean - 0.5 * std: return "B"
    elif m >= mean - 1.0 * std: return "C"
    elif m >= mean - 1.5 * std: return "D"
    else:                        return "E"

grades = [assign_grade(m, mean, std) for m in marks_list]

X = np.column_stack([marks_arr, marks_arr - mean]) 
y = grades

model = DecisionTreeClassifier(max_depth=6, random_state=42)
model.fit(X, y)
print("\nAI Model Trained Successfully!")

grade_to_cgpa = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5}

while True:
    your_marks = float(input("\nEnter your marks to predict grade: "))
    deviation  = your_marks - mean
    
    predicted_grade = model.predict([[your_marks, deviation]])[0]
    cgpa_points     = grade_to_cgpa[predicted_grade]
    
    print(f"Predicted Grade : {predicted_grade}")
    print(f" CGPA Points     : {cgpa_points}/10")
    
    if predicted_grade != "S":
        next_grade_marks = mean + 0.5 * std   # rough target for next band
        gap = round(next_grade_marks - your_marks, 1)
        if gap > 0:
            print(f" Tip: You need ~{gap} more marks to reach the next grade band.")

    if input("Continue? (y/n): ").lower() != 'y':
        break

print("\nThank you for using AI CGPA Predictor!")                           