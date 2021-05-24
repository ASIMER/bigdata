data = [1, 2, 3, 4]
new_data = []
for i, day in enumerate(data):
    if i > 0:
        new_data.append((data[i-1] + data[i]) / 2)
    new_data.append(data[i])
print(new_data)