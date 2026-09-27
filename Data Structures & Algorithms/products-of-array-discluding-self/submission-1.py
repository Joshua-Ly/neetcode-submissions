class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # final = []
        # for i in range(len(nums)):
        #     left = 1
        #     right = 1
        #     for j in range(i):
        #         left *= nums[j]
        #     for j in range(i + 1, len(nums)):
        #         right *= nums[j]
        #     result = left * right
        #     final.append(result)
        # return final
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        