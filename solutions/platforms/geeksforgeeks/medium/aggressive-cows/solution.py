class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        def isplace(dis):
            c=1
            last=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-last>=dis:
                    c+=1
                    last=arr[i]
                    if c==k:
                        return True
            return False
        low=1
        high=arr[-1]-arr[0]
        ans=0
        while low<=high:
            mid=(low+high)//2
            if isplace(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans