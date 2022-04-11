import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\DELL\PycharmProjects\mp-2\covid-cases-omicron.csv")
print(data.shape)
print(data.head(5))
x=data['Entity']
y=data['Omicron_percentage']
plt.xlabel('Entity')
plt.ylabel('Omicron_percentage')
plt.bar(x,y)
plt.show()
