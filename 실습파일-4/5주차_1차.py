# 행 인덱스 / 열 이름 설정
import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
print(df)

# 행 인덱스 / 열 이름 변경
import pandas as pd
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)
df.rename(index={'학생1':'준서', '학생2':'예은' }, inplace=True)

print(df)

# 행 삭제
import pandas as pd
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)
print(df3)

# 열 삭제
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)

# 행 / 열 / 원소 선택
import pandas as pd
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])

#행 선택
df.loc['서준'] ;df.iloc[0] 
df.loc[['서준', '우현']]; df.iloc[[0, 1]]
df.loc['서준':'우현']; df.iloc[0:1]

#열 선택
df['수학']; df.영어
df[['음악', '체육']]; df[['수학']]

#원소 선택
df.loc['서준', '음악']; df.iloc[0, 2]
df.loc['서준', ['음악', '체육']]; df.iloc[0, [2, 3]]
df.loc['서준', '음악':'체육']; df.iloc[0, 2:]
df.loc[['서준', '우현'], ['음악', '체육']]; df.iloc[[0, 1], [2, 3]]
df.loc['서준':'우현', '음악':'체육']; df.iloc[0:2, 2:]

# 행 / 열 추가
import pandas as pd
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

# 행(row)을 추가
df.loc[3] = 0
df.loc[4] = ['동규', 90, 80, 70, 60]
df.loc['행5'] = df.loc[3]

# 열(column)을 추가
df['국어'] = 80

# 행,열 바꾸기 / 원소 추가
import pandas as pd
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

#행,열 바꾸기
df.transpose()

#원소 추가
df.set_index('이름', inplace=True)

df.iloc[0][3] = 80
df.loc['서준']['체육'] = 90
df.loc['서준', '체육'] = 100
df.loc['서준', ['음악', '체육']] = 50
df.loc['서준', ['음악', '체육']] = 100, 50

# Index 설정 및 배열
import pandas as pd
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
#특정 열을 행 인덱스로 설정
df.set_index(['이름'])

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']

#행 인덱스 재배열
df.reindex(new_index, fill_value=0)
#행 인덱스 초기화
df.reset_index()
#행 인덱스 기준 정렬
df.sort_index(ascending=False)
#특정 열 데이터값 기준 정렬
df.sort_values(by='c1', ascending=False)



# Quiz
import pandas as pd

data = {
	'year' : [2016,2017,2018],
	'GDP_rate' : [2.8,3.1,3.9],
	'GDP' : ['1.23M','1.98M','1.77M']
	}

df = pd.DataFrame(data)

# Q2. 

df.drop ('GDP', axis = 1, inplace=True)
df

# Q3.

df['GDP'] = [1.23,1.98,1.77]
df