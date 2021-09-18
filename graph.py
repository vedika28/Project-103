import pandas as pd, plotly.express as pe

#Reading the CSV as a DataFrame.
data=pd.read_csv("data2.csv")
data2=pd.DataFrame(data)

#Creating a scatter plot with:
#X-axis as date, Y-axis as cases and Color based on the country.
graph=pe.scatter(data2, x="date", y="cases",color="country")
graph.show()