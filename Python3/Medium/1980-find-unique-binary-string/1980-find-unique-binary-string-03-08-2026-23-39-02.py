class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        st=set(nums)
        n=len(nums)
        for i in range(2**n):
            s=format(i,'0{}b'.format(n))
            if s not in st:
                return s