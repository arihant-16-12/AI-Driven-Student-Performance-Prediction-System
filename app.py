import streamlit as st
import matplotlib.pyplot as plt

from utils.predict import predict_student
from utils.gemini import generate_feedback

st.title("🎓 AI-Driven Student Performance Prediction System")

st.sidebar.title("Project Information")
st.sidebar.write("""
Course: Generative AI

Algorithm: Random Forest Classifier

Features:
- Attendance
- Assignment Score
- Quiz Score
- Midterm Score
- Study Hours
- GPA
""")

attendance = st.slider("Attendance", 0, 100, 75)
assignment = st.slider("Assignment Score", 0, 100, 70)
quiz = st.slider("Quiz Score", 0, 100, 65)
midterm = st.slider("Midterm Score", 0, 100, 70)
study = st.slider("Study Hours", 0, 10, 3)
gpa = st.slider("Current GPA", 0.0, 10.0, 7.0)

if st.button("Predict"):

    result = predict_student(
        attendance,
        assignment,
        quiz,
        midterm,
        study,
        gpa
    )

    st.success(f"Prediction: {result}")

    scores = [attendance, assignment, quiz, midterm, gpa * 10]
    labels = ["Attendance", "Assignment", "Quiz", "Midterm", "GPA"]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(labels, scores)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score")
    ax.set_title("Student Performance")

    st.pyplot(fig)

    st.subheader("📚 AI Recommendation")

    feedback = generate_feedback(result)

    st.markdown(feedback)