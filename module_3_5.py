def get_multiplied_digits(number):
    if number == 0:
        return 0
    while number % 10 == 0:
        number //= 10
    str_number = str(number)
    first = int(str_number[0])
    if len(str(number)) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str(number)) == 1:
        return first

result = get_multiplied_digits(402030)
print(result)
