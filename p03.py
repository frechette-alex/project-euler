# https://projecteuler.net/problem=3
# Solution: 6857

import math

import utils

def get_greatest_prime_factor(n: int) -> int:
	for v in range(math.floor(math.sqrt(n)), 2, -1):
		if n % v == 0 and utils.is_prime(v):
			return v
	# `n` has no prime factor greater than 1, so `n` is prime.
	return n

print(get_greatest_prime_factor(600851475143))

