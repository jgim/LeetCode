class Solution:
	def findMin(self, nums: List[int]) -> int:
		def searchMin(low, high):
			mid = (low + high) // 2
			if high - low <= 0:
				return nums[low]
			if nums[mid] > nums[high]:
				return searchMin(mid + 1, high)
			else:
				return searchMin(low, mid)
		return searchMin(0, len(nums) - 1)