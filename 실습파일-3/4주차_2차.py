import numpy as np

a = np.arange(0,6).reshape(3,2)
a
a.sum() # 행렬의 모든 원소의 합
a.sum(axis = 0) # 0축 방향(행 방향) 원소의 합
a.sum(axis = 1) # 1축 방향(열 방향) 원소의 합

a.min(axis = 0) # 0축 방향 원소의 최솟값
a.min(axis = 1) # 1축 방향 원소의 최솟값
a.max(axis = 0) # 0축 방향 원소의 최댓값
a.max(axis = 1) # 1축 방향 원소의 최댓값

a = np.array([1,3,4])
np.insert(a,1,2)
a = np.array([[1,1], [2,2], [3,3]])
np.insert(a, 1, 4, axis = 0)
np.insert(a, 1, 4, axis = 1)

a = np.array([1,2,3])
print(a[0], a[1], a[2])
print(a[-1], a[-2], a[-3])

a = np.array([1,2,3,4,5])
print(a[np.array([0,1])])
print(a[np.array([0,1,2])])
print(a[np.array([0,1,3])])
print(a[np.array([1,1,1,1])])

a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
a[1:5] # 슬라이싱 구간 [시작:끝] 인덱스, 새로운 ndarray 객체 생성이 아닌 기존 ndarray 객체를 참조 
a[1:]

a = np.arange(0,6).reshape(3,2)
a
print(a[0,0])
print(a[0,1])
print(a[0,2])

a = np.arange(0,24).reshape(4, 3, 2)
a
print(a[1, 2, 1])

a = np.arange(0,24).reshape(4, 3, 2)
a[0]
a[0,0]
a[0,1]
a[0,2]
np.concatenate((a[0,0], a[0,2]), axis = 0)

a = np.arange(0,9).reshape(3,3)
print(a[0]) # 첫 번째 행 불러오기1
print(a[0, :]) # 첫 번째 행 불러오기2
print(a[:, 0]) # 첫 번째 열 불러오기

print(a[0, 0:2])
print(a[0, :2])

print(a[0:2, 0:2])
print(a[:2, :2])

a[1, 1:].shape
a[1:2, 1:].shape

a = np.array([[2,3], [1,-2]])
b = np.array([1,4])
x = np.linalg.solve(a,b)
print(x)

a = np.array([[1,2], [3,4]])
np.linalg.det(a)
b = np.array([[1,2], [3,-6]])
np.linalg.det(b)
b = np.array([[1,2], [1,2]])
np.linalg.det(b)






















