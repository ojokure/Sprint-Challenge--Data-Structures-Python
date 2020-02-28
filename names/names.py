import time


def binary_search(names, dup):
    if len(names) == 0:
        return -1
    if names[0] > dup:
        return -1
    if names[len(names) - 1] < dup:
        return -1
    low = 0
    high = len(names)-1
    middle = int((high-low)/2 + low)
    while high > low:
        middle = int((high + low)/2)
        if dup == names[middle]:
            return middle
        elif dup < names[middle]:
            high = middle
        else:
            low = middle + 1
    return -1


start_time = time.process_time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


names_1.sort()
for names_2 in names_2:
    if binary_search(names_1, names_2):
        duplicates.append(names_2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# a = 0
# while a < len(names_1):
#     # for name_2 in names_2:
#     if names_1[a] in names_2:
#         duplicates.append(names_1[a])
#     a += 1


end_time = time.process_time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
