import seaborn as sb
import matplotlib.pyplot as plt
i=sb.load_dataset("iris")
sb.boxplot(x='petal_width',y='sepal_width',data=i)
plt.show()