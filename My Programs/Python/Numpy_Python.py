# !D array
import numpy as np

cricket= np.array(["Bat", "Ball", "Gloves"])
print(cricket[1:])

price= np.array(["2000", "200", "20"])
print(price[-2])

a=np.arange(1, 16, 3)
print(a)

'''Write 5 numbers between
 1to100 which are all equal
  distance to each other'''
b=np.linspace(1, 100, num=5) 
print(b)

#data type
c=np.ones(20, dtype=np.float64)
print(c)

zeroValue=np.zeros(9)
print(zeroValue)

np.identity(3)

#add 2D array values
a= np.array([1,2,3,4,5])
b= np.array([5,4,3,2,1])

c= np.concatenate((a,b))
print(c)


# 2D array
a=np.array([[1,2,3,4,5], [5,4,3,2,1]])
b=np.array([[5,4,3,2,1], [1,2,3,4,5]])

c=np.concatenate((a,b), axis=1)
print(c.ndim)

#np.size
#np.reshape(a, newshape(1,9), order="c")

#1D to 2D
a=np.array([1,2,3,4,5,6])
b=a[np.newaxis, :]  # change position of ratio

# .sum
# .mean

# 1D Array
numpy_1D = np.array([1,2,3])
numpy_1D.ndim

# 2D Array
numpy_2D = np.array([[1,2,3,4],[5,6,7,8]])
numpy_2D.ndim

# 3D Array
numpy_3D = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
numpy_3D.ndim