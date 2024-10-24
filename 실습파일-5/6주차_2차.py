
import pandas as pd
df = pd.read_csv('mpg.csv')

import matplotlib.pyplot as plt
df1 = df[['mpg', 'acceleration']].iloc[:20]
plt.style.use('ggplot')


df1.plot(kind='bar', figsize=(14, 5), width=0.7,
          color=['skyblue', 'blue'])

plt.title('MPG & ACCELERATION', size=30)
plt.xlabel('Index', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()





import matplotlib.pyplot as plt
plt.style.use('ggplot')

df3 = df['origin'].value_counts()

df3.plot(kind='bar', figsize=(7, 5), width=0.7,
          color='skyblue')

plt.title('ORIGIN', size=30)
plt.xlabel('Origin', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()






import matplotlib.pyplot as plt
df1 = df[['mpg', 'weight']].iloc[:20]
plt.style.use('ggplot')

ax = df1['mpg'].plot(kind='bar', figsize=(14, 5), width=0.7,
          color = 'skyblue', label = 'mpg')

ax1 = ax.twinx()
ax1.plot(df1.index, df1['weight'], marker='o', markersize=8, label='weight')

ax.set_title('MPG & WEIGHY', size=30, color='brown', weight='bold')
ax.set_ylabel('mpg', size=20, color='blue')
ax1.set_ylabel('weight', size=20, color='blue')
ax.legend(loc='upper left', fontsize=15)
ax1.legend(loc='upper right', fontsize=15)

plt.show()





import matplotlib.pyplot as plt
plt.style.use('ggplot')

df4 = df['mpg']

df4.plot(kind='hist', figsize=(7, 5), bins=10,
          color='skyblue')

plt.title('HISTOGRAM', size=30)
plt.xlabel('Index', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()





import matplotlib.pyplot as plt
df1 = df[['mpg', 'weight']]
plt.style.use('ggplot')

df1.plot(kind='scatter', x='weight', y='mpg',
         figsize=(14, 10), color = 'skyblue')

plt.title('MPG & WEIGHY', size=30, color='brown', weight='bold')
plt.ylabel('mpg', size=20, color='blue')
plt.xlabel('weight', size=20, color='blue')
plt.show()



import matplotlib.pyplot as plt
df1 = df[['mpg', 'weight', 'acceleration', 'displacement']]
plt.style.use('ggplot')

df1[['mpg', 'weight']].plot(kind='scatter', x='weight', y='mpg',
         figsize=(14, 10), c = df1['acceleration'], s = df1['displacement'])

plt.title('MPG & WEIGHY', size=30, color='brown', weight='bold')
plt.ylabel('mpg', size=20, color='blue')
plt.xlabel('weight', size=20, color='blue')
plt.show()




import matplotlib.pyplot as plt
plt.style.use('ggplot')

df3 = df['origin'].value_counts()

df3.plot(kind='pie', figsize=(7, 5), startangle=10,
         autopct='%.2f%%',
          colors=['blue', 'skyblue', 'green'])

plt.ylabel("")
plt.title('Pie Chart - Origin', size=15)
plt.legend(loc='upper right', fontsize=8)

plt.show()
