class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j,z=1,0
        for i in nums:
            if i:
                j*=i
            else:
                z+=1
        if z>1: return[0]*len(nums)
        res=[0]*len(nums)
        for i,c in enumerate(nums):
            if z:
                res[i]=0 if c else j
            else:
                res[i]= j//c
        return res
        