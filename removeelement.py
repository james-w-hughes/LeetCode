class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            if(nums[n] == val):
                nums.append(nums.pop(n))
            else:
                n = n + 1
        return n 
