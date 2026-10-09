import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")

att_gpa =pd.crosstab(df["Approximately what percentage of your classes do you attend?"],df["What was your approximate GPA/CGPA in your most recently completed semester?"])
att_gpa_pr =pd.crosstab(df["Approximately what percentage of your classes do you attend?"],df["What was your approximate GPA/CGPA in your most recently completed semester?"],normalize="index") * 100

print(att_gpa)
print(att_gpa_pr.round(1))
att_gpa.plot(
    kind="bar",
    # stacked=True,
    # figsize=(9, 5),
    title="Attendance vs GPA"
)
plt.legend()
plt.show()