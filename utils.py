import math
import itertools

def is_prime(number: int) -> bool:
	# Cover all prime numbers that could be factors.
	maybe_factors = itertools.chain(
		iter([2]),
		range(3, math.ceil(math.sqrt(number)), 2),
	)
	# Identifies factors.
	factors = filter(lambda v: (number % v == 0), maybe_factors)
	try:
		next(factors)
	except StopIteration:
		return True
	else:
		return False

def is_palindrome(string: str) -> bool:
	n = len(string)
	for i in range(0, n // 2) :
		if string[i] != string[n-1-i]:
			return False
	return True