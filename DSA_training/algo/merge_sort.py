def merge_sort(arr):
    if len(arr) > 1 :        
        right_arr = arr[:len(arr)//2]
        left_arr = arr[len(arr)//2:]

        print(right_arr)
        print(left_arr)

        merge_sort(right_arr)
        merge_sort(left_arr)

        i,j = 0,0

        while i < len(right_arr) :
            print(right_arr)
            break









ls = [4,5,7,3,2,1,8,9,6,10]
merge_sort(ls)