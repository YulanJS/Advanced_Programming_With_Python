import numpy as np
'''
import numpy as np
first = np.array([1, 2, 3, 4])
type(first)
<class 'numpy.ndarray'>
print(first)
[1 2 3 4]
second = np.array([1, 2.6, 3.5])
print(second)
[1.  2.6 3.5]
type(second)
<class 'numpy.ndarray'>
print(first.size)
4
print(first.dtype)
int32
second = np.array((1.99, 2.1, 3.3, 4.8), 'int')
print(second)
[1 2 3 4]
type(second.dtype)
<class 'numpy.dtype'>
second.dtype
dtype('int32')
first = np.arange(10)
print(first)
[0 1 2 3 4 5 6 7 8 9]
first.dtype
dtype('int32')
second = np.arange(4, 20, 2)
print(second)
[ 4  6  8 10 12 14 16 18]
second.dtype
dtype('int32')
first = np.linspace(1, 10)
print(first.size)
50
print(first)
[ 1.          1.18367347  1.36734694  1.55102041  1.73469388  1.91836735
  2.10204082  2.28571429  2.46938776  2.65306122  2.83673469  3.02040816
  3.20408163  3.3877551   3.57142857  3.75510204  3.93877551  4.12244898
  4.30612245  4.48979592  4.67346939  4.85714286  5.04081633  5.2244898
  5.40816327  5.59183673  5.7755102   5.95918367  6.14285714  6.32653061
  6.51020408  6.69387755  6.87755102  7.06122449  7.24489796  7.42857143
  7.6122449   7.79591837  7.97959184  8.16326531  8.34693878  8.53061224
  8.71428571  8.89795918  9.08163265  9.26530612  9.44897959  9.63265306
  9.81632653 10.        ]
second = np.linspace(100, 200, 11)
print(second)
[100. 110. 120. 130. 140. 150. 160. 170. 180. 190. 200.]
first = np.array((1, 2, 3), (4, 5, 6))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: data type not understood
first = np.array(((1, 2, 3),(4, 5, 6)))
print(first)
[[1 2 3]
 [4 5 6]]
print(first.size)
6
print(first.shape)
(2, 3)
first.ndim
2
first = np.zeros(5, 2)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: data type not understood
first = np.zeros((5, 2))
print(first)
[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]
second = np.ones((2, 6), 'int')
print(second)
[[1 1 1 1 1 1]
 [1 1 1 1 1 1]]
first = np.arange(10)
print(first.shape)
(10,)
print(first.ndim)
1
first.shape = (2, 5)
print(shape)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'shape' is not defined
print(first)
[[0 1 2 3 4]
 [5 6 7 8 9]]
second = first.reshape(5, 2)
print(second)
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
print(first)
[[0 1 2 3 4]
 [5 6 7 8 9]]
first = np.arange(5, 101, 5).reshape(4, 5)
print(first)
[[  5  10  15  20  25]
 [ 30  35  40  45  50]
 [ 55  60  65  70  75]
 [ 80  85  90  95 100]]
second = np.arange(20).reshape(4, 5)
print(second)
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
result = first + second
print(result)
[[  5  11  17  23  29]
 [ 35  41  47  53  59]
 [ 65  71  77  83  89]
 [ 95 101 107 113 119]]
result = first ** 2 + second * 5
print(result)
[[   25   105   235   415   645]
 [  925  1255  1635  2065  2545]
 [ 3075  3655  4285  4965  5695]
 [ 6475  7305  8185  9115 10095]]
result = second >= 10
print(result)
[[False False False False False]
 [False False False False False]
 [ True  True  True  True  True]
 [ True  True  True  True  True]]
result = first % 10 == 0
print(result)
[[False  True False  True False]
 [ True False  True False  True]
 [False  True False  True False]
 [ True False  True False  True]]
print(result.astype('int'))
[[0 1 0 1 0]
 [1 0 1 0 1]
 [0 1 0 1 0]
 [1 0 1 0 1]]
first = np.arange(1, 25, 2).reshape(3, 4)
print(first)
[[ 1  3  5  7]
 [ 9 11 13 15]
 [17 19 21 23]]
print(first[1])
[ 9 11 13 15]
print(first[1: ])
[[ 9 11 13 15]
 [17 19 21 23]]
result = first[0: 2]
result.size
8
print(first)
[[ 1  3  5  7]
 [ 9 11 13 15]
 [17 19 21 23]]
print(first[0: 2])
[[ 1  3  5  7]
 [ 9 11 13 15]]
result = first[2]
result.size
4
print(first[1:, 2])
[13 21]
print(first[1:, 2:])
[[13 15]
 [21 23]]
print(first[2:, 1:])
[[19 21 23]]
first[2:, 1:].size
3
second = first.view()
print(second)
[[ 1  3  5  7]
 [ 9 11 13 15]
 [17 19 21 23]]
second[1, 2:] = 0
print(second)
[[ 1  3  5  7]
 [ 9 11  0  0]
 [17 19 21 23]]
print(first)
[[ 1  3  5  7]
 [ 9 11  0  0]
 [17 19 21 23]]
'''