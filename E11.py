#Write a program to sort a dictionary in ascending and descending order of values
data = {'a': 5, 'b': 1, 'c': 9, 'd': 3}

ascending_order = dict(sorted(data.items(), key=lambda item: item[1]))
descending_order = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print("Original dictionary:", data)
print("Ascending order by values:", ascending_order)
print("Descending order by values:", descending_order)
