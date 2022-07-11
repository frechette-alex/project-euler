# https://projecteuler.net/problem=4
# Solution: 906609

import utils

products = (m*n for m in range(1000) for n in range(1000))
palindromes = filter(lambda v: utils.is_palindrome(str(v)), products)
print(max(palindromes))