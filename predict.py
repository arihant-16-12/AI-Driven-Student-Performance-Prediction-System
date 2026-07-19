import joblib

model = joblib.load("models/student_model.pkl")

def predict_student(att, assignment, quiz, midterm, study, gpa):
    prediction = model.predict([[att, assignment, quiz, midterm, study, gpa]])
    return prediction[0]