import math


def slow_is_prime(n):
	"""
	Time complexity: 0(n)
	>>> slow_is_prime(199)
	True
	"""
	for i in range(2, int(n/2)):
		if (n % i) == 0:
			return False
	return True


def is_prime(n):
	"""
	Time complexity: √n
	>>> is_prime(199)
	True
	"""
	for i in range(2, int(math.sqrt(n))+1):
		if (n % i) == 0:
			return False
	return True


if __name__ == "__main__":
	import doctest
	doctest.testmod()
