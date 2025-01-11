def thirdMax(nums: list[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)
    print(nums)
    
    if len(nums) > 3 :
        return nums[2]
    else :
        return max(nums)
    



    


print(thirdMax([0,2,2,3,1]))



