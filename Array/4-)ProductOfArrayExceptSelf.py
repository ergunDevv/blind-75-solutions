# QUESTION : Product Of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and without using the division operation.

# APPROUCH
# Our approuch to this question is defining result array with 1's length of the array's length.
# Beacuse of question ask us return an array result[i] is equal to the product of all the elements of nums except arr[i] that's why we will define prefix and postfix integers than multiply the result[i] with prefix and postfix.Than multiply prefix and postfix's values with nums[i]


def ProductOfArrayExceptSelf(arr):
    # Defining result array with 1's length of an array.
    result = [1] * (len(arr))
    # Defining prefix,postfix
    prefix = 1
    postfix = 1
    for i in range(len(arr)):
        # Multiplying the result with prefix
        result[i] *= prefix
        # Multiplying the prefix with arr[i]
        prefix *= arr[i]
        # Multiplying the result with postfix
        result[len(arr)-1-i] *= postfix
        # Multiplying the postfix with arr[i]
        postfix *= arr[len(arr)-1-i]

    return result


print(ProductOfArrayExceptSelf([1, 2, 3, 4]))
# returns = [24, 12, 8, 6]
