# Approach-1
# Generate all subarray and calculate the sum of each subarray and find the maximum one
# T.C = O(n ^3) S.C. = O(1)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                sub_sum=0
                for k in range(i,j+1):
                    sub_sum= sub_sum+ nums[k]
                if sub_sum> maxsum:
                    maxsum = sub_sum
        return maxsum

# Approach-2
# Generate all subarray and calculate the sum of each subarray and find the maximum one
# T.C = O(n ^2) S.C. = O(1)

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        n=len(nums)
        for i in range(n):
            sub_sum=0
            for j in range(i,n):
                sub_sum= sub_sum+ nums[j]
                if sub_sum> maxsum:
                    maxsum = sub_sum
        return maxsum

# Approach-3
# Divide and conquer approach
# divide the subarray in two parts and calculate the leftmax and rightmax  then perform crossing 
# T.C.= O(nlogn) S.C= O(log n)  # recursive stack

class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxsub(nums,0,len(nums)-1)

    def maxsub(self,nums,left,right):
        if left==right:
            return nums[left]
        mid=(left+right) //2
        leftmax= self.maxsub(nums,left,mid)
        rightmax=self.maxsub(nums,mid+1,right)
        leftsum= float('-inf')
        total=0
        for i in range(mid,left-1,-1):
            total+=nums[i]
            leftsum=max(leftsum,total)
        rightsum= float('-inf')
        total=0
        for i in range(mid+1,right+1):
            total+=nums[i]
            rightsum=max(rightsum,total)
        crossmax=leftsum + rightsum
        return max(crossmax,leftmax, rightmax)
# Approach-4
# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        currentsum=0
        for num in nums:
            currentsum=max(num,currentsum+num)
            maxsum=max(maxsum,currentsum)
        return maxsum