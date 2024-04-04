from typing import Dict, List


class Letter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __repr__(self):
        return str(self.count)


class Solution:

    def __init__(self):
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t):
            return False

        _countsS: List[Letter] = [Letter() for _ in range(255)]
        _countsT: List[Letter] = [Letter() for _ in range(255)]

        for x in range(0, length):
            charS = s[x]
            charT = t[x]

            letterS = _countsS[ord(charS)]
            letterT = _countsT[ord(charT)]

            letterS.increment()
            letterT.increment()

        for x in range(0, length):
            charS = s[x]
            charT = s[x]

            letterS = _countsS[ord(charS)]
            letterT = _countsT[ord(charT)]

            if letterS.count != letterT.count:
                return False

        return True
