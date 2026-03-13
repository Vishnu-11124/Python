
def mergeSortedArrays(firstArray, secondArray):
    n, m = len(firstArray), len(secondArray)

    i = j = 0
    
    newArray = []

    def addValue(value):
        if len(newArray) == 0 or value != newArray[-1]:
            newArray.append(value)

    while i<n and j<m:
        if firstArray[i] <= secondArray[j]:
            addValue(firstArray[i])
            i+=1
        else:
            addValue(secondArray[j])
            j+=1     

    while i<n:
        addValue(firstArray[i])
        i+=1

    while j<m:
        addValue(secondArray[j])
        j+=1

    return newArray   

 
# -------------------------------------------------

print("Output: ", mergeSortedArrays([1, 2, 3], [2, 3, 4]))  # Output: [1, 2, 3, 4]

# -------------------------------------------------

print("Output: ", mergeSortedArrays([5, 10, 15], [10, 20, 30]))  # Output: [5, 10, 15, 20, 30]

# -------------------------------------------------

nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [ 1, 2, 3, 6, 7, 8, 9, 10]
print("Output: ", mergeSortedArrays(nums1, nums2))  # Output: [1, 2, 3, 4, 6, 7, 8, 9, 10]

# -------------------------------------------------