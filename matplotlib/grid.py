import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv("E:\8th semester\data-science-journey\pandas\Mini Project\Company_Profit.csv")
# print(df)

line_style = dict(
        marker=".",
        ms=10,
        mfc="red",
        mec="red",
        linestyle="None",
        linewidth=3,
        #color="orange"
        )
#Add grid
plt.grid(axis="both",
         linewidth=1.5,
         color="#0b041a",
         linestyle="solid")

plt.plot(df['Company'], df["Total_Profit"], color="#61151e", **line_style)

plt.title("Company and Profit",
          fontsize=15,
          family="Arial",
          color="#6a8f0b")
plt.xlabel("Company")
plt.ylabel("Profit")

plt.show()