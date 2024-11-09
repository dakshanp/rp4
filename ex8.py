import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("D:\\Book.CSV")
print(data)
data.info()
x=[1,2,3,4,5]
y=[8000,9500,10256,12000,18600]
plt.plot(x,y)
plt.xlabel('number')
plt.ylabel('profits')
plt.title('Myfirst graph')
plt.show()
a=data.isnull().sum()
print(a)
number=[8000,9500,10256,12000,18600]
total=sum(number)
print(total)
column=[100,200,200,250,300]
max_value=max(column)
print(max_value)
