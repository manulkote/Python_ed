x = [1, 5, 2, 4, 3, 6, 8, 7, 9]
y = x.copy()
y.pop(0)
new_list = [j for i, j in zip(x, y) if i < j]
print(new_list)
