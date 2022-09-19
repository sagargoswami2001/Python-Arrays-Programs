# Write a Python Program to find the First Duplicate Element in a Given Array of Integers.
''' Return -1 if there are no such elements.'''

def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

print(find_first_duplicate([1,2,3,4,4,5]))
print(find_first_duplicate([1,2,3,4]))
print(find_first_duplicate([1,1,2,3,3,2,2]))
