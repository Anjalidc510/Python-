def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char
    return result

test_string = "programming"
print(remove_duplicates(test_string))