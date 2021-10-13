class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_reach, curr_reach = 0, 0
        jumps = 0
        for i in range(len(nums)-1):
            if i+nums[i] > max_reach:
                max_reach = i+nums[i]
                
            if i == curr_reach:
                jumps += 1
                curr_reach = max_reach
                
        return jumps
