# QUESTION :
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.

def twoSum(arr, target):
    prevHashMap = {}  # storing data as value: index pairs

    for i, n in enumerate(arr):
        diff = target-n
        # Searching difference between target and number if difference exists in the prevHashMap. Returning the indexes of values.
        if diff in prevHashMap:
            # If not exists in the prevHashMap loop continues
            return [prevHashMap[diff], i]

        print('i'+str(i))
        # print('prevHashMap'+str(prevHashMap[n]))
        prevHashMap[n] = i
    return


print(twoSum([2, 7, 11, 15], 9))
