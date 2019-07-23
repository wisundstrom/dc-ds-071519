"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
	temperature_c = (temperature_f - 32) * (5/9)
	return temperature_c


def convert_c_to_f(temperature_c):
	f=temperature_c*(9/5)+32
	return f

def convert_k_to_c(temperature_k):
	c=temperature_k-270
	return c

def convert_c_to_k(temperature_c):
	k=temperature_c+270
	return k

def convert_k_to_f(temperature_k):
	c=convert_k_to_c(temperature_k)
	f=convert_c_to_f(c)
	return f

def convert_f_to_k(temperature_f):
	c=convert_f_to_c(temperature_f)
	k=convert_c_to_k(c)
	return k



