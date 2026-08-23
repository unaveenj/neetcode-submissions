class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set(nums)
        if len(nums)==len(output):
            return False
        else:
            return True
