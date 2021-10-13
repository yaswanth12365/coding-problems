class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i,j=0,n-1
        nums.sort()
        min_sum = float("inf")
                
        while(i<j):#outer two pointer-->[..i,k....j] 
            k=i+1
            while(k<j):#innner two pointer.--->[..k...j]
                curr_sum = nums[i]+nums[k]+nums[j]
                
                if curr_sum == target:
                    return curr_sum
                
                elif abs(target - curr_sum)<abs(min_sum-target):
                    min_sum = curr_sum
                
                if curr_sum<target:
                    #value is lesser, so increase it how?
                    #k is moved forwards
                    k+=1
                else:
                    j-=1
            i+=1
            j=n-1
            #reset the value of j to last pointer.
        return min_sum

