import random
from itertools import chain

arr1 = random.sample(range(100), 10)
arr2 = random.sample(range(100), 10)
resultado = chain.from_iterable(zip(arr1, arr2))

print(arr1)
print(arr2)
print(*resultado)