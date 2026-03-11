

def mergeTwoLists(list1, list2):
    i = j = 0
    new_array = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_array.append(list1[i])
            i += 1
        else:
            new_array.append(list2[j])   
            j += 1 

    new_array.extend(list1[i:])    
    new_array.extend(list2[j:])  

    return new_array 

# ------------------------------------------------------

list1 = [1,2,4] 
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))
# Output: [1, 1, 2, 3, 4, 4]

# ------------------------------------------------------

list1 = []
list2 = []
print(mergeTwoLists(list1, list2))
# Output: []

# ------------------------------------------------------

list1 = [2]
list2 = [0,4,6]
print(mergeTwoLists(list1, list2))
# Output: [0, 2, 4, 6]

# ------------------------------------------------------