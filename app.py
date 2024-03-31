import numpy as np
#writing array:

# a=np.array([1,2,3,4,5,6,7,8,9])
# print(a)

# 1-D array:

# l=[10,20,30,40,50]
# a=np.array(l)
# # print(a)
# print(type(a))

#2-D array:shape,reshape

# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.shape)
# print(a.reshape(3,2))
# print(a.reshape(1,6))
# print(a.reshape(6,1))

# data type:
# a=np.array([4,5,6,7,8])
# print(a.dtype)

#arange:
# a=np.arange(1,7)
# print(a)

# a=np.arange(1,10,2)
# print(a)

# a=np.arange(1,10)
# print(a.reshape(3,3))

# a=np.array(list(range(1,10)))
# print(a)

#linspace:

# a=np.linspace(1,40,20)
# print(a)

# ones function:

# a=np.ones(6)
# print(a)

# a=np.ones((6,6))
# print(a)

#zeros function:

# a=np.zeros(6)
# print(a)

# a=np.zeros((2,3))
# print(a)

#eye function:

# a=np.eye(6)
# print(a)

#random function:

# a=np.random.rand(1,10)
# print(a)

#randn function:

# a=np.random.randn(10)
# print(a)

#randfloat function:

# a=np.random.randint(1,10)
# print(a)

# a=np.random.randint(5,20,10)
# print(a)

# a=np.random.randint(5,20,(3,3))
# print(a)

#universal arithmetic functions:

# a1=np.random.randint(1,100,(3,3))
# a2=np.random.randint(1,100,(3,3))

# print(a1*a2)
# print(a1+a2)
# print(a1-a2)
# print(a1/a2)


#inbuilt funnctions:

# a1=np.random.randint(1,100,(3,3))
# a2=np.random.randint(1,100,(3,3))
# a=np.sqrt(a1)
# print(a)

# a=np.square(a1)
# print(a)

# a=np.exp(a1)
# print(a)

# a=np.log10(a1)
# print(a)

#slicing:

# a=np.arange(1,11)
# print(a)

# print(a[5])
# print(a[2:7])
# print(a[1:9:2])
# print(a[-1])
# print(a[-1::-1])

# a=np.arange(1,37).reshape(6,6)
# print(a)
# print(a[1:4,2:5])
# print(a[4:,3:5])
# print(a[2:4,:3])



# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]
#  [13 14 15 16 17 18]
#  [19 20 21 22 23 24]
#  [25 26 27 28 29 30]
#  [31 32 33 34 35 36]]