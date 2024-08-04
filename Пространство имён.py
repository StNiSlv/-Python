calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(n):
    inf0 = ((len(n)), (n.upper()), (n.lower()))
    print(inf0)
    count_calls()
def is_contains(x, z):
    lowercase_str = x.lower()
    lowercase_list = [s.lower() for s in z]
    print(lowercase_str in lowercase_list)
    count_calls()
string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
