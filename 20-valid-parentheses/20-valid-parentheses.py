class Solution:
	def isValid(self, s: str) -> bool:
		def brackets(i, result, target):
			lens = len(s)
			while i < lens:
				if s[i] == target:
					return True, i + 1
				elif s[i] == '{':
					result, i = brackets(i + 1, result, '}')
				elif s[i] == '(':
					result, i = brackets(i + 1, result, ')')
				elif s[i] == '[':
					result, i = brackets(i + 1, result, ']')
				elif s[i] == ' ':
					i += 1
				else:
					return False, i
				if result == False:
					return False, i
			return False, i

		i = 0
		lens = len(s)
		if lens <= 1:
			return False
		result = True
		while i < lens:
			if s[i] == '{':
				result, i = brackets(i + 1, result, '}')
			elif s[i] == '[':
				result, i = brackets(i + 1, result, ']')
			elif s[i] == '(':
				result, i = brackets(i + 1, result, ')')
			elif s[i] == ' ':
				i += 1
			else:
				return False
			if result == False:
				return False
		return True