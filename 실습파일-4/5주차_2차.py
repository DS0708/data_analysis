# 데이터 미리보기

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head()) 
print(df.tail())

print(df.shape)

print(df.info())

print(df.dtypes)

print(df.mpg.dtypes)

print(df.describe())
print(df.describe(include='all'))

# 데이터 개수 확인

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.count())

print(type(df.count()))

unique_values = df['origin'].value_counts() 
print(unique_values)

print(type(unique_values))

# 통계함수 적용

import pandas as pd
df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df.info()
#df.drop(['origin', 'name', 'horsepower'], axis = 1, inplace = True)

print(df.mean())
print(df['mpg'].mean())
print(df.mpg.mean())
print(df[['mpg','weight']].mean())

print(df.median()); print(df['mpg'].median())

print(df.max()); print(df['mpg'].max())

print(df.min()); print(df['mpg'].min())

print(df.std()); print(df['mpg'].std())

print(df.corr()); print(df[['mpg','weight']].corr())

# 선 / 막대그래프, 히스토그램 그리기

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0, 5], 3:] 
df_ns.index = ['South','North']
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())

df_ns.plot()

tdf_ns = df_ns.T
print(tdf_ns.head())
tdf_ns.plot()

tdf_ns.plot(kind='bar')



# 산점도 / 박스플롯 그리기
import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df.plot(x='weight',y='mpg', kind='scatter')

df[['mpg','cylinders']].plot(kind='box')