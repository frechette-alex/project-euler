# https://projecteuler.net/problem=1
# Solution: 233168.

sum_of_multiples = 0
for number in range(1000):
	if number % 3 == 0 or number % 5 ==0:
		sum_of_multiples += number
print(sum_of_multiples)

test