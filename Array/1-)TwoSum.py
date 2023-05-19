def twoSum(arr,target) :
    prevHashMap={} # storing data as value: index pairs

    for i, n in enumerate(arr):
        diff=target-n
        if diff in prevHashMap: #Searching difference between target and number if difference exists in the prevHashMap. Returning the indexes of values.
        # If not exists in the prevHashMap loop continues
            return[prevHashMap[diff],i]

        print('i'+str(i))
        # print('prevHashMap'+str(prevHashMap[n]))
        prevHashMap[n]=i
    return


print(twoSum([2,7,11,15],9)) 