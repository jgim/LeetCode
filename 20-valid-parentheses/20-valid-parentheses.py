class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		for i in s:
			print (i)
			if i in ['{', '[', '(']:
				stack.append(i)
			elif len(stack) <= 0:
				return False
			elif i == '}' and stack.pop() != '{':
				return False
			elif i == ']' and stack.pop() != '[':
				return False
			elif i == ')' and stack.pop() != '(':
				return False
		return len(stack) == 0

