def sum_of_two(nums,target):
    
    seen={}
    for i,num in enumerate(nums):
        if target-num in seen:
            return [seen[target-num],i]
        else:
            seen[num]=i
    return "No nums sum up to the Target number..."

#print(sum_of_two([1,2,3,4,5],3))

a=[1,2,3,4]
print(a)