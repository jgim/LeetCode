class Solution:
	def isValid(self, s: str) -> bool:
		stack, dictionary = [],{'{':'}', '[':']', '(':')'}
		for i in s:
			if i in dictionary:
				stack.append(i)
			elif len(stack) == 0 or i != dictionary[stack.pop()]:
				return False
		if len(stack) != 0:
			return False
		return True