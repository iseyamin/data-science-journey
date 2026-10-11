import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")

# Define preliminary risk categories
high_concern = ["2.00–2.49"]
needs_attention = ["2.50–2.99"]

# Classify each student based on GPA
df["Risk_Level"] = "No GPA-based flag"

df.loc[
    df["What was your approximate GPA/CGPA in your most recently completed semester?"].isin(needs_attention),
    "Risk_Level"
] = "Needs Attention"

df.loc[
    df["What was your approximate GPA/CGPA in your most recently completed semester?"].isin(high_concern),
    "Risk_Level"
] = "High Concern"

# Display students who need attention
at_risk = df[df["Risk_Level"].isin(
    ["High Concern" , "Needs Attention"]
)]

print(at_risk.count())

# at_risk.to_csv("AcademicRiskStudents.csv")