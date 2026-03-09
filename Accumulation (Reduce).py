## Accumulation (Reduce)

from functools import reduce

words = ["apple", "banana", "cherry", "dragonfruit"]
remove = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(remove)