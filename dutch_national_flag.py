def sortColors(nums):
    mid=1
    i=0
    j=0
    k=len(nums)-1

    while j<=k:
        if nums[j]<mid:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        elif nums[j]>mid:
            nums[j],nums[k]=nums[k],nums[j]
            k-=1
        else:
            j+=1

    return nums

print(sortColors([2,0,2,1,1,0,2]))
print(sortColors([0,0,0,0]))
print(sortColors([2,2,2,2]))
print(sortColors([1,1,1]))
print(sortColors([1,2,0,0]))