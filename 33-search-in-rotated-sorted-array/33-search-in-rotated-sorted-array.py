class Solution:
	def search(self, nums: List[int], target: int) -> int:
		def	binary_search(low, high):
			mid = (low + high) // 2
			if nums[mid] == target:
				return mid
			elif nums[low] == target:
				return low
			elif nums[high] == target:
				return high
			if high - low <= 0:
				return -1
			if nums[low] < nums[mid]:
				if nums[low] < target < nums[mid]:
					return binary_search(low, mid - 1)
				else:
					return binary_search(mid + 1, high)
			elif nums[mid] < nums[high]:
				if nums[mid] < target < nums[high]:
					return binary_search(mid + 1, high)
				else:
					return binary_search(low, mid - 1)
			return -1

		lens = len(nums)
		if not nums:
			return -1
		if nums[0] < nums[lens - 1]:
			if nums[0] > target or nums[lens - 1] < target:
				return -1
		return binary_search(0, lens - 1)