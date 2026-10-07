import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv("E:\8th semester\data-science-journey\pandas\Mini Project\Company_Profit.csv")
# print(df)

line_style = dict(
        marker=".",
        ms=10,
        mfc="red",
        mec="red",
        linestyle="solid",
        linewidth=3,
        #color="orange"
        )
plt.plot(df['Company'], df["Total_Profit"], color="#61151e", **line_style)
# plt.plot(df['Company'], df["Sale_Count"], color="#1e291b", **line_style)
plt.title("Company and Profit")
plt.xlabel("Company")
plt.ylabel("Profit")

#plt.plot(x,y2,  **line_style)
plt.show()