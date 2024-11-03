calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    count_calls()
    return (length, upper_case, lower_case)


def is_contains(string, list_to_search):
    count_calls()
    lower_case = string.lower()
    lowercase_list = []
    for item in list_to_search:
        lowercase_list.append(item.lower())
    if lower_case in lowercase_list:
        a = True
    else:
        a = False
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
