class Solution:
	def search(self, nums: List[int], target: int) -> int:
		lens = len(nums) - 1
		if not nums:
			return -1
		if nums[0] < nums[lens]:
			if nums[0] > target or nums[lens] < target:
				return -1
		low, high = 0, lens
		while low <= high:
			mid = (low + high) // 2
			if nums[mid] == target:
				return mid
			if nums[low] <= nums[mid]:
				if nums[low] <= target < nums[mid]:
					high = mid - 1
				else:
					low = mid + 1
			elif nums[mid] <= nums[high]:
				if nums[mid] < target <= nums[high]:
					low = mid + 1
				else:
					high = mid - 1
		return -1