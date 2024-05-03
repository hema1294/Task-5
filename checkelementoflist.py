#Python program using lambda function to check every element of a list is an integer or string

# Example list
given_list = [1, 2, "hello", 4, "world"]

# Lambda function to check if an element is an integer or a string
check_element = lambda x : isinstance(x, int) or isinstance(x, str)

# Use map() to apply the lambda function to each element of the list
result = all(map(check_element, given_list))

if result:
    print("Every element of the list is an integer or a string.")
else:
    print("Some elements of the list are not integers or strings.")