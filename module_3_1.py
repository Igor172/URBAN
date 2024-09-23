calls = 0

def count_calls(count):
    global calls
    calls += 1

def string_info(string):
    length = len(string)
    up = string.upper()
    dwn = string.lower()
    count_calls(calls)
    return length, up, dwn

def is_contains(word: str, spisok: list):
    count_calls(calls)
    word = word.lower()
    spisok = [el.lower() for el in spisok]
    if word in spisok:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)