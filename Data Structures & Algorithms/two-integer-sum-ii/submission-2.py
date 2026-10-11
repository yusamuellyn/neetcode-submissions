class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        arr = []
        while left < right:
            currsum = numbers[left] + numbers[right]

            if currsum < target:
                left = left + 1 
            
            if currsum > target:
                right = right - 1

            if currsum == target:
                arr.append(left + 1)
                arr.append(right + 1)
                break

        return arr 
        