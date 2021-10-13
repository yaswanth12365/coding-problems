from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [i for i, j in Counter(nums).items() if j == 2]
