class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        generate_permutations_recursive(nums, 0, [], result)
        return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation[:])
        return
    # create a new permutation by adding the current number at every position
    for i in range(len(currentPermutation)+1):
        newPermutation = list(currentPermutation)
        newPermutation.insert(i, nums[index])
        generate_permutations_recursive(nums, index + 1, newPermutation, result)
            
