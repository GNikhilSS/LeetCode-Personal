class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while j > i:
            if numbers[i] + numbers[j] == target:
                return [i+1] + [j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
