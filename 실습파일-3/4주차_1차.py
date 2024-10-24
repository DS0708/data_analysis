import numpy as np
a= np.array([1,2,3])
a
a.shape
a.ndim
a.dtype
a.itemsize #the number of bytes used per values
a.size

a = np.array([1,2,3] , dtype = 'int32')
b = np.array([1,2,3] , dtype = 'int64')
a.dtype
b.dtype
c = a + b
c.dtype

a = np.array([1,2,3,4])
a

a = np.array([1,2,3,4], dtype=np.int32)

a = np.array([1,2,3,4], dtype='int32')

a = np.array([1,2,3]) # 1차원 ndarray 배열 생성
a.max() # 가장 큰 값을 반환
a.min() # 가장 작은 값을 반환
a.mean() # 평균 값을 반환

a = np.array([[1,1], [2,2], [3,3]])
a
a.flatten()

a = np.array([1,2,3])
b = np.array([[4,5,6], [7,8,9]])
np.append(a,b)
np.append([a], b, axis = 0) #[a]를 통해 2차원 배열로 만들어야 함

np.random.rand(3, 3)

np.random.randint(0,10, size = 10) # 0에서 10사이의 10개의 난수생성

a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
c

a = np.array([1,2])
b = np.array([4,5,6])
c = a + b

a = np.array([[1,2],[3,4]])
b = np.array([[10,20], [30,40]])
a + b # 덧셈
a - b # 뺄셈
a * b # 곱셈
a / b # 나눗셈

np.matmul(a,b)
a @ b
a[0,0]*b[0,0] + a[0,1]*b[1,0]
a[0,0]*b[0,1] + a[0,1]*b[1,1]
a[1,0]*b[0,0] + a[1,1]*b[1,0]
a[1,0]*b[0,1] + a[1,1]*b[1,1]

a = np.array([[1,2], [3,4]])
a + 1 # 행렬의 각 성분에 대한 덧셈
a - 1 # 행렬의 각 성분에 대한 뺄셈
a * 100 # 행렬의 각 성분에 대한 곱셈
a / 100 # 행렬의 각 성분에 대한 나눗셈
a **2 # 행렬의 각 성분에 대한 제곱

np.zeros((2,3))
np.ones((2,3))
np.full((2,3), 100)
np.eye(3)
np.random.random((2,3))

np.arange(0, 10)
np.arange(0, 10, 2)
np.arange(0, 10, 3)
np.arange(0.0, 1.0, 0.2)

np.linspace(0, 10, 5)   #linspace = combination of the words 'linear' and 'space'
np.linspace(0, 10, 4)

np.arange(0,10).reshape(2,5) #arange = array + range()
np.arange(0,10).reshape(5,2)
np.arange(0,10).reshape(3,3)

np.arange(0, 24).reshape(4, 3, 2)

a = np.arange(6).reshape(3,2)
a
np.transpose(a)













