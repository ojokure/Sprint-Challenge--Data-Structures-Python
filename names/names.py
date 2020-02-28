import time
from collections import defaultdict
from binary_search_tree import BinarySearchTree


start_time = time.process_time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Runtime Complexity = O(n^2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# apparently the most efficient. with time complexity of O(1)
# dict = defaultdict(bool)
# for name_1 in names_1:
#     dict[name_1] = True

# for name_2 in names_2:
#     if dict[name_2]:
#         duplicates.append(name_2)

# set1 = set(names_1)
# set2 = set(names_2)

# set_intersect = list(set1.intersection(set2))

# duplicates = [x for x in set_intersect]


bst = BinarySearchTree(names_1[0])
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


end_time = time.process_time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
