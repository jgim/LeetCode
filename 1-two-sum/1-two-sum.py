class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		dictionary = {}
		for i, num in enumerate(nums):
			value = target - num
			if value not in dictionary:
				dictionary[num] = i
			else:
				return [dictionary[value], i]