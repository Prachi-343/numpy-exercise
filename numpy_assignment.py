# 1. Create a vector with values ranging from 10 to 49.

# import numpy as np
# a=np.arange(10,49)
# print(a)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.

# a=np.arange(0,9).reshape(3,3)
# print(a)

# 3. Create a 10x10 array with random values and find the minimum and maximum values.

# a=np.random.randint(1,100,(10,10))
# print(a)
# print(np.min(a))
# print(np.max(a))

# 4. Create a random vector of size 30 and find the mean value.

# a=np.random.randint(1,100,30)
# print(a)
# print(np.mean(a))

# 5. Perform addition, subtraction, multiplication, and division of two given NumPy arrays.

# a1=np.arange(1,10)
# a2=np.arange(11,20)
# print(a1+a2)
# print(a1-a2)
# print(a1*a2)
# print(a1/a2)

# 6. Calculate the element-wise square root of a given NumPy array.

# a=np.arange(1,10)
# print(np.sqrt(a))

# 7. Stack two given arrays vertically and horizontally.

# a1=np.array([1,2,3])
# a2=np.array([4,5,6])
# print(np.vstack((a1,a2)))
# print(np.hstack((a1,a2)))


# 8. Reshape a given 1D array into a 2D array with 3 rows and 4 columns.

# a=np.arange(1,13).reshape(3,4)
# print(a)

# 9. Transpose a given 2D array and then flatten it into a 1D array.

# a=np.arange(1,13).reshape(3,4)
# b=np.transpose(a)
# print(b.reshape(12))
# print(b.flatten())

# 10. Create a random of array and implement different slicing methods on it 

# a=np.random.randint(1,100,(6,6))
# print(a)
# print(a[1:3,:2])





