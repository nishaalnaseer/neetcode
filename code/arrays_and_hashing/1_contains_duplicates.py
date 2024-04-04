from typing import List


class Solution:

    def __init__(self):
        pass

    def containsDuplicate(self, nums: List[int]) -> bool:
        original = len(nums)
        new = len(set(nums))

        if original != new:
            return True
        else:
            return False
