# Binary search implementation in python
def binary_search(arr,n):
   
    total_array_length = len(arr)
    left = 0
    right = total_array_length - 1
    
    while(left <= right):
        mid = (left + right) // 2
        if(arr[mid] ==  n):
            return mid
        if(arr[mid] < n ):
            left = mid + 1
        else:
            right = mid - 1
    return -1

num = [10,20,30,40,50,60,70,80,90]
result = binary_search(num, 20)
print(result)
