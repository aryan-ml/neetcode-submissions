class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Map = set()

        # for i in nums:
        #     if i in Map:
        #         return True
        #     Map.add(i)
        # return False

        Unq = set(nums)

        if len(nums) != len(Unq):
            return True
        return False