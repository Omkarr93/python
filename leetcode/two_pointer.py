ls = [2, 5, 7, 9, 11, 15]
Target =  16







def two_sum_sorted(nums, target):
    left,right = 0 , len(ls) - 1 
    while left < right:
            current_sum = ls[left] + ls[right]
            if current_sum == Target:
                return [ls[left], ls[right]]
            
            elif current_sum < Target :
                left += 1
            else :
                right -= 1 
    return []


print(two_sum_sorted(ls,Target))

