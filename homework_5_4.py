from sys import getsizeof
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
start = perf_counter()
[result.append(src[i]) for i in range(1, len(src)) if src[i] > src[i - 1]]

print(result)
print(type(result), getsizeof(result))
print(perf_counter() - start)
# -----------------------------------------------------------
start = perf_counter()
result = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
print('-' * 20)
print(*result)
print(type(result), getsizeof(result))
print(perf_counter() - start)
