# QUESTION :
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(arr):
    # Creating Hashmap.
    duplicateHashMap = {}
    # Looping every element of array
    for i, n in enumerate(arr):
        # If element exists in duplicateHashMap return true if not exists append the element to duplicateHashMap
        if n in duplicateHashMap:
            return True
        else:
            duplicateHashMap[n] = i
    # If didn't return true after loop return false
    return False


print(containsDuplicate([1, 2, 3,])
      )
