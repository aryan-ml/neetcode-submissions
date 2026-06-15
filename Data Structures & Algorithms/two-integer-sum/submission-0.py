class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in Map:
                return [Map[diff], i]
            else:
                Map[v] = i
        return 