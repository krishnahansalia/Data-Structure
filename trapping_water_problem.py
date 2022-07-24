def trapping_water_problem(nums): 
    if len(nums)<3:
        return 0

    left_max=[0 for i in range(len(nums))]
    right_max=[0 for i in range(len(nums))]

    for i in range(1,len(nums)):
        left_max[i]=max(left_max[i-1],nums[i-1])

    for i in range(len(nums)-2,-1,-1):
        right_max[i]=max(right_max[i+1],nums[i+1])

    count=0

    for i in range(1,len(nums)-1):
        
        if min(left_max[i],right_max[i])>nums[i]:
            count+=min(left_max[i],right_max[i])-nums[i]
        
    return count


print(trapping_water_problem([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapping_water_problem([4,2,0,3,2,5]))