def add_two_numbers() -> int:
    user_input = input()
    output = user_input.split(",")
    sum = 0
    for i in output:
        sum+=int(i)
    return sum




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
