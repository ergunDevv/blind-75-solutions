

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
