class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        n = len(nums)
        right = [1] * n
        left = [1] * n
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        
        for j in range(n-2 , -1, -1):
            right[j] = nums[j+1] * right[j + 1]
        
        for g in range(n):
            arr[g] = right[g] * left[g]

        return arr
            

        