a = np.array([1,2,34,4,5,6])
np.where(a > 15, a, 10*a)
array([10, 20, 34, 40, 50, 60])
