
elements = [1, 2, 2, 3, 4, 5,6]

count = {}

for item in elements:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print(count)