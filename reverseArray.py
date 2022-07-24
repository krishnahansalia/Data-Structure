def reverseArray(nums):
    left=0
    right=len(nums)-1

    while left<=right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

    return nums

def reversenum(num):
    r=0

    while num:
        r= r*10 + num%10
        num//=10
    
    return r

print(reverseArray([1,2,3,4,5]))

print(reversenum(12345))