nums = [1,1,7,14]
k = 4
if sum(nums)<=k:
    print(0)
count=0
h=k
for i in range(len(nums)):
    if nums[i]<=h:
        h-=nums[i]
    else:
        while nums[i]>h:
            h+=k
            count+=count+1
        h-=nums[i]
print(count)
