# https://projecteuler.net/problem=2
# Solution: 4613732

import functools
import itertools

@functools.lru_cache
def fib(n: int) -> int:
	if n == 0:
		return 1
	if n == 1:
		return 2
	else:
		return fib(n-1) + fib(n-2)

sum_number = 0
for number in itertools.takewhile(lambda v: v <= 4_000_000, map(fib, itertools.count())):
	if number %2 == 0:
		sum_number += number
print(sum_number)


