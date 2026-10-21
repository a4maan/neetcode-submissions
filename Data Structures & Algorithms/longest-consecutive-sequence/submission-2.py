class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) == 0: return 0
        longest = 0
        l = 0
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]-1:
                l += 1
                if l > longest:
                    longest = l
            else:
                l = 0
        return longest+1

        