class Solution:
	def findMin(self, nums: List[int]) -> int:
		lens = len(nums) - 1
		low, high = 0, lens
		while low < high:
			mid = (low + high) // 2
			if nums[low] < nums[high]:
				return nums[low]
			if nums[low] > nums[mid]:
				high = mid
			elif nums[mid] > nums[high]:
				low = mid + 1
		return nums[low]