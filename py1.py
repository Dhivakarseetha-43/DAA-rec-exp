def interpolationsearch(arr, target):
    low=0
    high=len(arr)-1
    while low<=high and arr[low]<=target and arr[high]>=target:
        if low==high:
            if arr[low]==target:
                return low
            else:
                return -1
        mid=low+((target-arr[low])*(high-low)//(arr[high]-arr[low]))
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
'''
def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+high//2
        if arr[mid]==target:
           return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1'''
        

arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 60
idx1 = interpolationsearch(arr, target)
#idx2 = binarysearch(arr, target)

print(f"Index of {target}: {idx1}")
#print(f"Index of {target}: {idx2}")
