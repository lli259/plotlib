import matplotlib.pyplot as plt
import pandas as pd

time_ratio=pd.read_csv('a.csv')
time_ratio=time_ratio.set_index(time_ratio.columns.values[0])
time_ratio.index=range(len(time_ratio))

plt.axvline(x=30, color='b', linestyle='-')
plt.axvline(x=53, color='b', linestyle='-')
plt.axhline(y=1, color='r', linestyle='-')
time_ratio.plot()
plt.legend()

#plt.show()
plt.savefig('time_ratio.png')

plt.clf()

