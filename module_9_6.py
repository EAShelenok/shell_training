def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j : j + i + 1]

a = all_variants('abc')

b = all_variants('abcd')

for i in a:
    print(i)
    
for i in b:
    print(i)