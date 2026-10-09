import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")


#cross-tabulation (contingency table) of two or more factors
comparison = pd.crosstab(df["On average, how many hours do you study outside classes per day?"],df["What was your approximate GPA/CGPA in your most recently completed semester?"])

print(comparison)

comparison.plot(
    kind="bar",
    #  stacked=True,
    #  figsize=(9, 9),
    title="GPA Range Distribution by Study Hours"
)
plt.xlabel("Daily study-hour category")
plt.ylabel("Number of Students")
plt.legend(title="GPA range", bbox_to_anchor=(1.02, 1))
plt.tight_layout() # Automatically fixes spacing so labels don't get cut off or overlap

plt.show()