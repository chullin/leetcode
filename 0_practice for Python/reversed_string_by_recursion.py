def reversed_sting(input):
    if len(input) == 0:
        return input
    else:
        return reversed_sting(input[1:]) + input[0]
    
input_str = "Hello World"
reversed_str = reversed_sting(input_str)
print("Reverserd String: ", reversed_str)
