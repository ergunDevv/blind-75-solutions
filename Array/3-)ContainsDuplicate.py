def containsDuplicate(arr):
    duplicateHashMap = {}

    for i, n in enumerate(arr):
        if n in duplicateHashMap:
            return True
        else:
            duplicateHashMap[n] = i
    return False


print(containsDuplicate([1, 2, 3,])
      )
