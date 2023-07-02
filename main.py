def symbolCounter(s: str):
    for sym in s:
        # counter = 0
        # for sub_sym in s:
        #     counter += 1
        print(sym, s.count(sym))

# Решение задачи за O(N*M), N - кол-во всех символов строке, а М - кол-во уникальных символов
def symbolCounterBetter(s: str):
    for sym in set(s):
        print(sym, s.count(sym))

# Решение задачи за O(N)
def symbolCounterTheBest(s: str):
    symbols = {}
    for char in s:
        symbols[char] = symbols.get(char, 0) + 1
    for char, counter in symbols.items():
        print(char, counter)


symbolCounter('aaaabbbcccdddddd')
print('\n')
symbolCounterBetter('aaaabbbcccdddddd')
print('\n')
symbolCounterTheBest('aaaabbbcccdddddd')
print('\n')
