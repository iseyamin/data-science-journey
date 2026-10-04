import pandas as pd

df = pd.read_json("E:\8th semester\data-science-journey\pandas\sample_Data.json")
print("Displaying the info:")
print(df.info()) #giving all basic information


data ={
    "Name":["Shakib", "Adib", 'Rayhan'],
    "Age":[26, 22, 24],
    "cgpa":[3.33,3.77,3.22]
}
#store data
dff = pd.DataFrame(data)
print(dff.info())