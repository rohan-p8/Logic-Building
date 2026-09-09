# Rotate an array by one position to the left.

lst = [18, 14, 8, 13, 27, 88, 45]
print("Given list: ", lst)

# Left Shift <<<<<<<<<<<<<<

lst[:] = lst[1:] + lst[:1]
# lst[:] = lst[2:] + lst[:2]

# lst[:] = lst[3:] + lst[:3]

# lst[:] = lst[4:] + lst[:4]

# Right shift >>>>>>>>>>>>>>

# lst[:] = lst[-1:] + lst[:-1]

# lst[:] = lst[-2:] + lst[:-2]

# lst[:] = lst[-3:] + lst[:-3]

print(lst)

