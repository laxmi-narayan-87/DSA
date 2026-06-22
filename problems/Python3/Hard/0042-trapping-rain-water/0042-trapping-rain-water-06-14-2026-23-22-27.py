class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,lm,rm,res=0,len(height)-1,0,0,0
        while l<r:
            if height[l]<height[r]:
                lm=max(lm,height[l]);res+=lm-height[l];l+=1
            else:
                rm=max(rm,height[r]);res+=rm-height[r];r-=1
        return res
