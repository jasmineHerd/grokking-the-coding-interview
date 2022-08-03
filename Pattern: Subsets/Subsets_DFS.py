class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        reVal = []
        helper(nums,0,[],reVal)
        return reVal
        
def helper(nums,index,curr,reVal):
    if index == len(nums):
        reVal.append(curr[:]) 
        return
    curr.append(nums[index])
    helper(nums,index+1,curr,reVal)
    curr.pop()
    helper(nums,index+1,curr,reVal)

       
        
        
        
