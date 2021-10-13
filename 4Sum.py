class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        n = len(A)
        A.sort()

        numCounters = {}
        for a in A:
            numCounters[a] = 1 if a not in numCounters else numCounters[a]+1
        
        # binary search
        def search(start, end, target) -> int:
            if target <= A[start]:
                return start
            
            if A[end] < target:
                return -1
            
            leng = end-start+1
            while leng > 0:
                while start+leng <= e and A[start+leng] < target: # find the biggest number and less than target
                    start += leng
                leng = leng // 2

            return start+1 # smallest number and greater or equal to target
        
        def findKSum(k, start, target) -> List[List[int]]:
            if k == 1:
                if target in numCounters and numCounters[target] > 0:
                    return [[target]]
                return []
            
            targeti = search(start, n-k, target-sum(A[n-k+1:]))
            if targeti == -1:
                return []
            
            result = []
            for i in range(targeti, n-k+1):
                if i > targeti and A[i] == A[i-1]: # prevent duplicate results
                    continue
                if sum(A[i:i+k]) > target: # sum of smallest numbers are still bigger than target
                    return result
                
                numCounters[A[i]] -= 1 # consume A[i]
                
                for l in findKSum(k-1, i+1, target-A[i]):
                    result.append([A[i]] + l)
                    
                numCounters[A[i]] += 1 # release A[i]
                             
            return result
                         
        return findKSum(4, 0, target)
