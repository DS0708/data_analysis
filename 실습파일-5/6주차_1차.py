import pandas as pd
df = pd.read_csv('mpg.csv')


import matplotlib.pyplot as plt
plt.style.use('ggplot') 

plt.figure(figsize=(14, 5))

plt.xticks(size=10, rotation='vertical')

plt.plot(df.index, df['mpg'], marker='o', markersize=8)

plt.title('auto-mpg', size=30) 
plt.xlabel('mpg', size=20)
plt.ylabel('index', size=20)
plt.legend(labels=['mpg'], loc='best', fontsize=10)

plt.show()



import matplotlib.pyplot as plt
plt.style.use('ggplot') 

fig = plt.figure(figsize=(14, 10))   
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(df.index, df['mpg'], marker='o', markersize=8, label = 'mpg')
ax2.plot(df.index, df['weight'], marker='o', markerfacecolor='green', markersize=8, 
         color='olive', linewidth=2, label='weight')
ax1.legend(loc='best')
ax2.legend(loc='best')

ax1.set_ylim(0, 50)
ax2.set_ylim(1000, 6000)

ax1.set_xticklabels(df.index, rotation=90)
ax2.set_xticklabels(df.index, rotation=90)

plt.show()




import matplotlib.pyplot as plt
fig = plt.figure(figsize=(14, 5))   
ax = fig.add_subplot(1, 1, 1)

ax.plot(df.index, df['mpg'], marker='o', markerfacecolor='green', 
        markersize=10, color='olive', linewidth=2, label='mpg')
ax.plot(df.index, df['acceleration'], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='acceleration')

ax.legend(loc='best')
ax.set_title('MPG & ACCELERATION', size=20)
ax.set_xlabel('index', size=12) 
ax.set_xticklabels(df.index, rotation=0)
ax.tick_params(axis="x", labelsize=12)
ax.tick_params(axis="y", labelsize=12)
plt.show()





import matplotlib.pyplot as plt
df1 = df[['mpg', 'acceleration']]
plt.style.use('ggplot')

df1.plot(kind='area', stacked=False, alpha=0.2, figsize=(14, 5))

plt.title('MPG & ACCELERATION', size=30)
plt.xlabel('Index', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()





import matplotlib.pyplot as plt
df1 = df[['mpg', 'acceleration']]
plt.style.use('ggplot')

ax = df1.plot(kind='area', stacked=False, alpha=0.2, figsize=(20, 10))

ax.set_title('MPG & ACCELERATION', size=30, color='brown', weight='bold')
ax.set_xlabel('Index', size=20, color='blue')
ax.legend(loc='best', fontsize=15)

plt.show()


import matplotlib.pyplot as plt
df1 = df[['mpg', 'acceleration']]
plt.style.use('ggplot')

ax = df1.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))

ax.set_title('MPG & ACCELERATION', size=30, color='brown', weight='bold')
ax.set_xlabel('Index', size=20, color='blue')
ax.legend(loc='best', fontsize=15)

plt.show()
