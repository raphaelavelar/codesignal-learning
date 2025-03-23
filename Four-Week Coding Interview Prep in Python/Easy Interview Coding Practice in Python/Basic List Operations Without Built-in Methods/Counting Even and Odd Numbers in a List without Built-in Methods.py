def solution(nums):
    even = 0

    for number in nums:
        if number % 2 == 0:
            even += 1

    return (even, len(nums) - even)
