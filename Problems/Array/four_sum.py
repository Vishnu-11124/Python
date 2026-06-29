
def fourSum(nums, target):
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1
            while k <l:
                result = nums[i]+nums[j]+nums[k]+nums[l]
                if result<target:
                    k+=1
                elif result>target:
                    l-=1
                else:
                    temp = [nums[i],nums[j],nums[k],nums[l]]
                    ans.append(temp)    
                    k+=1
                    l-=1

                    while k < l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
    return ans                            
                
# ------------------------------------------------------------

# def fourSum(nums, target):
#     n = len(nums)
#     result = set()
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                     if nums[i]+nums[j]+nums[k]+nums[l] == target:
#                         temp = [nums[i],nums[j],nums[k],nums[l]]
#                         temp.sort()
#                         result.add(tuple(temp))
#     return [list(ans) for ans in result] 
                   
# ------------------------------------------------------------

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))

# ------------------------------------------------------------

nums = [2,2,2,2,2]
target = 8
print(fourSum(nums, target))

# ------------------------------------------------------------