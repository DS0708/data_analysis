import pandas as pd
df = pd.read_excel("titanic.xlsx")

nan_deck = df['deck'].value_counts(dropna=False) 
print(nan_deck)

print(df.head().isnull())

print(df.head().notnull())

print(df.head().isnull().sum(axis=0))


import pandas as pd
df = pd.read_excel("titanic.xlsx")

print(df['age'].head(10))
mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)
print(df['age'].head(10))

df = pd.read_excel("titanic.xlsx")
print(df['embark_town'][825:830])
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()   
print(most_freq)
df['embark_town'].fillna(most_freq, inplace=True)
print(df['embark_town'][825:830])

df = pd.read_excel("titanic.xlsx")
print(df['embark_town'][825:830])
df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#데이터 불러오기
df = pd.read_csv("heart_2020_cleaned.csv")
df
df.info()

#BMI 칼럼의 박스플롯 시각화를 통한 이상치 확인
plt.figure(figsize=(8, 6))
sns.boxplot(y = 'BMI', data = df)
plt.show()

#BMI 칼럼의 이상치 제거
Q1 = df['BMI'].quantile(0.25)
Q3 = df['BMI'].quantile(0.75)
IQR = Q3 - Q1
rev_range = 1.5
filter = (df['BMI'] >= Q1 - rev_range*IQR) & (df['BMI'] <= Q3 + rev_range*IQR)
df_rmv = df.loc[filter]

#BMI 칼럼의 박스플롯 시각화를 통한 이상치 확인
plt.figure(figsize=(8, 6))
sns.boxplot(y = 'BMI', data = df_rmv)
plt.show()



import pandas as pd
import numpy as np

df = pd.read_csv("mpg.csv")
df.dropna(subset=['horsepower'], axis=0, inplace=True)

bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'], bins=[0, 100, 200, 1000],
                            labels=bin_names, include_lowest=True)

print(df[['horsepower', 'hp_bin']].head(15))


import pandas as pd

df = pd.read_csv('mpg.csv', header=None)
df.dropna(subset=['horsepower'], axis=0, inplace=True)

bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'], bins=[0, 100, 200, 1000],
                            labels=bin_names, include_lowest=True)

horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))

df1 = pd.get_dummies(df, columns=['hp_bin'])
print(df1)


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("wine-clustering.csv")
df.head()

#표준화
StandardScaler = StandardScaler()
df_stand = StandardScaler.fit_transform(df)
df_stand = pd.DataFrame(data = df_stand, columns=df.columns)
df_stand.head()

#정규화
MinMaxScaler = MinMaxScaler()
df_minmax = MinMaxScaler.fit_transform(df)
df_minmax = pd.DataFrame(data = df_minmax, columns=df.columns)
df_minmax.head()



import pandas as pd

df = pd.read_excel("titanic.xlsx")
df
X = df.drop('survived', axis=1)
y = df['survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, randomstate=0,
                                                    stratify=y, shuffle=True)


import pandas as pd
df = pd.read_excel("iris.xlsx")

from sklearn.model_selection import KFold
kfold = KFold(n_splits=10, shuffle=True, random_state=0)
list(kfold.split(df))


