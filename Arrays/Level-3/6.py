# Reverse the list (without using built-in reverse).
# Use two pointer concept

lst = [18, 14, 8, 13, 27, 88, 45]
print("Given list: ", lst)

# print(lst[::-1])

left = 0
right = len(lst) - 1

while left < right:

	lst[left], lst[right] = lst[right], lst[left]

	left += 1
	right -= 1

print("\nReversed list: ", lst)

