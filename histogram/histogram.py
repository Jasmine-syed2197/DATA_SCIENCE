import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.histplot(df['petal_length'],kde = False)
plt.show()

0.