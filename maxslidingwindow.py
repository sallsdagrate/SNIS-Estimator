
nums = [1,3,-1,-3,5,3,6,7]
k = 3

for i in range(k - 1):
    for j in range(len(nums)-i - 1):
        nums[j] = max(nums[j], nums[j+1])
    print(nums)

print(nums[:len(nums) - k + 1])
