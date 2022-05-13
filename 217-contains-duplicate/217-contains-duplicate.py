class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		lens = len(nums)
		dictionary = {}
		for num in nums:
			if num not in dictionary:
				dictionary[num] = num
			else:
				return True
		return False