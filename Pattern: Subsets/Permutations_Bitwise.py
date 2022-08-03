class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        helper(0, [],result,nums)
        return result

def helper(index, currentPermutation,result,nums):
    #if same length then thats a result
    if len(nums) == len(currentPermutation):
        result.append(currentPermutation[:])
        
    
    for i in range(len(nums)):
        print("and1=",1<<index & index)
        if 1 << i & index == 0:
            print("and2=",1<<i & index)
            print("or=",index | 1 << i)
            helper(index | 1 << i , currentPermutation + [nums[i]],result,nums)
