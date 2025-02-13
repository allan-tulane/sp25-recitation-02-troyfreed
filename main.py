"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###


def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1
	else:
		return a * simple_work_calc(n // b, a, b) + n

	pass


def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
					 the work done at each node 

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1
	else:
		return a * work_calc(n // b, a, b, f) + f(n)
	pass


for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
	w1 = work_calc(n, 2, 2, lambda x: 1)
	w2 = work_calc(n, 2, 2, lambda x: math.log2(x))
	w3 = work_calc(n, 2, 2, lambda x: x)
	print(n, "     ", "Lambda x:1 ", w1, " lambda x: log2(x) ", w2,
	      " lambda x: x ", w3)


def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
					 the work done at each node 

	Returns: the value of W(n).
	"""
	if n == 1:
		return f(1)
	else:
		return span_calc(n // b, a, b, f) + f(n)
	pass


def compare_work(work_fn1,
                 work_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)

	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n, work_fn1(n), work_fn2(n)))
	return result


def print_results(results):
	""" done """
	print(
	    tabulate.tabulate(results,
	                      headers=['n', 'W_1', 'W_2'],
	                      floatfmt=".3f",
	                      tablefmt="github"))


def compare_span(span_fn1,
                 span_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)

	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n, span_fn1, span_fn2))
	return result
