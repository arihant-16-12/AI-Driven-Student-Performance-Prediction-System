def generate_feedback(result):

    if result == "Excellent":
        return """
# 🎉 Excellent Performance

## 📚 Study Plan
- Continue studying 2–3 hours daily.
- Solve advanced problems.
- Revise every weekend.

## 💪 Strengths
- Excellent attendance.
- Good conceptual understanding.
- Strong academic performance.

## 🚀 Improvement Tips
- Participate in coding contests.
- Work on real-world projects.
- Learn new technologies.

## 🌟 Motivation
Keep up the great work! You are on the right track.

## 📅 Weekly Schedule
Monday-Friday:
• Study 2-3 hours
• Practice coding 1 hour

Saturday:
• Mock test
• Revision

Sunday:
• Rest
• Learn something new
"""

    elif result == "Good":
        return """
# 👍 Good Performance

## 📚 Study Plan
- Study 3 hours daily.
- Focus on weak subjects.

## ⚠ Weaknesses
- Minor mistakes in tests.
- Need more revision.

## 🚀 Improvement Tips
- Practice previous year papers.
- Improve time management.

## 🌟 Motivation
You are doing well. Small improvements can make a big difference.

## 📅 Weekly Schedule
Daily:
• Study 3 hours
• Practice questions

Weekend:
• Full revision
"""

    elif result == "Average":
        return """
# 😊 Average Performance

## 📚 Study Plan
- Study at least 4 hours daily.
- Revise after every class.

## ⚠ Weaknesses
- Low consistency.
- Needs better preparation.

## 🚀 Improvement Tips
- Improve attendance.
- Complete assignments on time.
- Practice quizzes.

## 🌟 Motivation
Every expert was once a beginner. Stay consistent.

## 📅 Weekly Schedule
Monday-Friday:
• Study 4 hours
• Revise notes

Weekend:
• Mock test
• Doubt solving
"""

    else:
        return """
# ⚠ Needs Improvement

## 📚 Study Plan
- Study 5 hours daily.
- Start from basic concepts.

## ⚠ Weaknesses
- Low attendance.
- Poor test performance.
- Lack of revision.

## 🚀 Improvement Tips
- Attend every lecture.
- Complete assignments.
- Ask teachers for help.
- Practice daily.

## 🌟 Motivation
Failure is not the end. Every day is a new opportunity to improve.

## 📅 Weekly Schedule
Daily:
• Study 5 hours
• Solve practice questions

Weekend:
• Full revision
• Mock test
"""