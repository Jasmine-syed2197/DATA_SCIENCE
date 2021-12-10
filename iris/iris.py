import matplotlib.pyplot as m
import seaborn as ca
i=ca.load_dataset("iris")
ca.displot(x="petal_width", y="sepal_length",data=i)
m.show

