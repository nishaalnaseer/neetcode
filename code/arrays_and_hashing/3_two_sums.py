from typing import List


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for index in range(length-1):
            for index2 in range(index+1, length):
                num1 = nums[index]
                num2 = nums[index2]

                if num1 + num2 == target:
                    return [index, index2]

        return []


if __name__ == '__main__':
    numses = [
        [2, 7, 11, 15],
        [3, 2, 4],
        [3, 3],
        [3, 2, 3]
    ]

    targets = [
        9, 6, 6, 6
    ]

    outputs = [
        [0, 1], [1, 2], [0, 1], [0,2]
    ]

    for x in range(len(numses)):
        nums = numses[x]
        target = targets[x]
        output = outputs[x]

        actual = Solution().twoSum(nums, target)

        assert actual == output
