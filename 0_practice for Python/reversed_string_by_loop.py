def reverse_string (input):
	reversed_str = ""
	for i in input:
		reversed_str = i + reversed_str
	return reversed_str

input_str = "Hello World"
reversed_str = reverse_string(input_str)
print("Reverserd String: ", reversed_str)