def jump(nums):
    if len(nums) < 2:
        return 0
    start = 0
    end = 0
    step = 0
    while end < len(nums) - 1:
        step += 1
        max_end = end + 1
        for i in range(start, end + 1):
            if nums[i] + i >= max_end:
                max_end = nums[i] + i
        start = end + 1
        end = max_end
    return step

print(jump([2,3,1,1,4]))
