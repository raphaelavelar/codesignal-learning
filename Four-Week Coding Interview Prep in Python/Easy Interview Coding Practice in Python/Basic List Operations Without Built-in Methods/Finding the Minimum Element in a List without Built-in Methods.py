def find_min(nums):
    if not nums:
        return None

    minimum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < minimum:
            minimum = nums[i]

    return minimum
