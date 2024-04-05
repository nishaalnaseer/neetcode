from collections import Counter
from typing import List


class Solution:
    def __init__(self):
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _anagrams = []

        for string in strs:
            _update = True

            for listing in _anagrams:
                if self.isAnagram(listing[0], string):
                    _update = False
                    listing.append(string)
                    break

            if _update:
                _anagrams.append([string])

        return _anagrams


if __name__ == '__main__':
    class Test:
        def __init__(self, input_, output_):
            self.input_ = input_
            self.output_ = output_


    tests = [
        Test(["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        Test([""], [[""]], ),
        Test(["a"], [["a"]])
    ]

    for test in tests:
        actual_output = Solution().groupAnagrams(test.input_)

        # assert actual_output == test.output_
