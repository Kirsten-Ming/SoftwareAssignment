import matplotlib.pyplot as plt
import pandas as pd

iris_data=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris_data

plt.scatter(iris_data['sepal_length'], iris_data['sepal_width'])

plt.savefig('iris_scatter.png')
plt.savefig('iris_scatter.jpeg')