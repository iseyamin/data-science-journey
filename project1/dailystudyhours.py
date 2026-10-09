import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")


# Count students in each study-hour category
study_counts = df["On average, how many hours do you study outside classes per day?"].value_counts()

print(study_counts)
study_percentage = df["On average, how many hours do you study outside classes per day?"].value_counts(normalize=True) * 100

print(study_percentage.round(2))


study_counts.plot(
    kind="pie",
    title="Distribution of Daily Study Hours",
    xlabel="Study-hour category",
    ylabel="Number of students"
)
plt.legend()

# plt.tight_layout()  # Automatically fixes spacing so labels don't get cut off or overlap
plt.show()