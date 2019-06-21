import matplotlib.pyplot as plt
import pandas as pd

#opening studen.csv

data=pd.read_csv('http://13.234.186.179/student.csv')
label=list(data[0:])[1:]
for i in range(len(data)):
    name=data.iloc[i][0]
    plot_data=data.iloc[i][1:]
    plt.pie(plot_data,labels=label)
    plt.title(name)
    plt.show()
