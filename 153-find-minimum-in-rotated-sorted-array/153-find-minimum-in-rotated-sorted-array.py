class Solution:
	def findMin(self, nums: List[int]) -> int:
		lens = len(nums) - 1
		low, high = 0, lens
		if nums[0] < nums[high] or lens == 0:
			return nums[0]
		while low <= high:
			mid = (low + high) // 2
			if nums[low] == nums[high]:
				return nums[low]
			if nums[low] < nums[high]:
				return nums[low]
			if nums[mid] < nums[mid - 1]:
				return nums[mid]
			if nums[low] > nums[mid]:
				high = mid - 1
			elif nums[mid] > nums[high]:
				low = mid + 1