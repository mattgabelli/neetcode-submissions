class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = []
        for i in range(0, len(nums)):
            if nums[i] in nums_seen:
                return True
            nums_seen.append(nums[i])
        return False