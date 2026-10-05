# Count how many elements are common between two lists.

lst1 = [1,34,8,22,88,63]
lst2 = [15,3,8,22,18]

commonCnt = len(set(lst1) & set(lst2))

print(f"Count of common elements: {commonCnt}")