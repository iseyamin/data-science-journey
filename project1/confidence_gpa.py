import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")

conf_cg = pd.crosstab(df["How confident are you about your academic performance this semester?"],df["What was your approximate GPA/CGPA in your most recently completed semester?"])
conf_cg.plot(kind="bar")
plt.legend(title="CGPA")

# plt.hist(df["How confident are you about your academic performance this semester?"], bins=5, color='orange')
plt.xlabel("Confidence Label")
plt.ylabel("Number of students")
plt.show()