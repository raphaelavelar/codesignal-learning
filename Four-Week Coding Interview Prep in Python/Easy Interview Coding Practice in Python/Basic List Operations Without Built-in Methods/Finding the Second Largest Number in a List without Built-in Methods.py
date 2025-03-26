from typing import List, Optional


def second_max(nums: List[int]) -> Optional[int]:
    if len(nums) < 2:
        return None

    largest = None
    second_largest = None

    for number in nums:
        if largest is None:
            largest = number
        elif number == largest:
            continue
        elif number > largest:
            second_largest = largest
            largest = number
        elif second_largest is None:
            second_largest = number
        elif number > second_largest:
            second_largest = number

    return second_largest
