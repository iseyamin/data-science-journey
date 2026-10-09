import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")

dept_gpa = pd.crosstab(df["Which academic discipline are you studying?"],df["What was your approximate GPA/CGPA in your most recently completed semester?"])
print(dept_gpa)

dept_gpa.plot(kind='bar', title='Department wise CGPA', xlabel='Faculty/Department', ylabel='CGPA count')
plt.legend(title="CGPA")
plt.show()