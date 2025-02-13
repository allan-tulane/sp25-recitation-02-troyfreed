from main import *


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

	assert simple_work_calc(16, 4, 2) == 496
	assert simple_work_calc(40, 5, 2) == 5390
	assert simple_work_calc(48, 6, 2) == 13584


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n * n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300

	assert work_calc(10, 2, 2, lambda n: n ^ 2) == 30
	assert work_calc(20, 1, 2, lambda n: n * 2) == 75
	assert work_calc(30, 3, 2, lambda n: n + n) == 519


def test_compare_work():
	# Set recurrence parameters
	a = 2
	b = 2

	# Create work_fn1 for where c < log_b(a)
	work_fn1 = lambda n: work_calc(n, a, b, lambda n: n**0.5)

	# Create work_fn2 for  where c > log_b(a)
	work_fn2 = lambda n: work_calc(n, a, b, lambda n: n**1.5)

	res = compare_work(work_fn1, work_fn2)

	print(res)


def test_compare_span():
	a = 2
	b = 2

	span_fn1 = lambda n: span_calc(n, a, b, lambda n: n**0.5)
	span_fn2 = lambda n: span_calc(n, a, b, lambda n: n**1.5)

	res = compare_span(span_fn1, span_fn2)

	print(res)
