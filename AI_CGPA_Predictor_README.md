# 🎯 AI-Based CGPA Predictor

An intelligent **CGPA prediction system** built using **Python** and
**Machine Learning**. This project uses a **Decision Tree Classifier**
to predict student grades and corresponding CGPA based on class
performance.

------------------------------------------------------------------------

## 🚀 Features

-   📊 Calculates **class mean** and **standard deviation**
-   🧠 Uses **AI (Decision Tree Model)** for prediction
-   🎓 Assigns grades based on **relative performance**
-   🔮 Predicts:
    -   Grade (S, A, B, C, D, E)
    -   CGPA (out of 10)
-   💡 Gives improvement tips to reach the next grade
-   🔁 Interactive loop for multiple predictions

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 🐍
-   NumPy
-   Scikit-learn (DecisionTreeClassifier)

------------------------------------------------------------------------

## 📌 How It Works

### 1. Data Input

-   User enters marks of all students in the class

### 2. Statistical Analysis

-   Calculates:
    -   Mean (average marks)
    -   Standard Deviation (spread of marks)

### 3. Grade Assignment (Rule-Based)

  Condition          Grade
  ------------------ -------
  ≥ Mean + 1.5×Std   S
  ≥ Mean + 0.5×Std   A
  ≥ Mean - 0.5×Std   B
  ≥ Mean - 1.0×Std   C
  ≥ Mean - 1.5×Std   D
  Else               E

------------------------------------------------------------------------

### 4. Machine Learning Model

-   Features used:
    -   Marks
    -   Deviation from mean
-   Model:
    -   Decision Tree Classifier

------------------------------------------------------------------------

### 5. Prediction

-   User inputs their marks
-   Model predicts:
    -   🎯 Grade
    -   📊 CGPA Points

------------------------------------------------------------------------

## 📈 Grade to CGPA Mapping

  Grade   CGPA
  ------- ------
  S       10
  A       9
  B       8
  C       7
  D       6
  E       5

------------------------------------------------------------------------

## ▶️ How to Run

1.  Install dependencies:

``` bash
pip install numpy scikit-learn
```

2.  Run the script:

``` bash
python your_file_name.py
```

------------------------------------------------------------------------

## 🌟 Future Improvements

-   Add GUI (Tkinter / Web App)
-   Use advanced ML models
-   Add subject-wise CGPA prediction

------------------------------------------------------------------------

## 👨‍💻 Author

**Jidnyesh Pujari**\
Engineering Student @ VIT Bhopal
