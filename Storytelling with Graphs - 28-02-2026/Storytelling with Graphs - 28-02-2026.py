# Storytelling with Graphs

import matplotlib.pyplot as plt

# Sample Data

subjects = ['Math', 'Science', 'English', 'Computer', 'Social']
marks = [85, 78, 92, 88, 75]

# 1. Bar Chart

plt.figure(figsize=(8, 5))
plt.bar(subjects, marks)
plt.title("Student Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 2. Pie Chart

plt.figure(figsize=(7, 7))
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution by Subject")
plt.show()

# 3. Histogram

student_scores = [45, 55, 60, 65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.figure(figsize=(8, 5))
plt.hist(student_scores, bins=5, edgecolor='black')
plt.title("Distribution of Student Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.show()