class Solution:
	def isValid(self, s: str) -> bool:
		def curlyBrackets(i, result):
			lens = len(s)
			while i < lens:
				if s[i] == '}':
					return True, i + 1
				elif s[i] == '{':
					result, i = curlyBrackets(i + 1, result)
				elif s[i] == '(':
					result, i = roundBrackets(i + 1, result)
				elif s[i] == '[':
					result, i = squareBrackets(i + 1, result)
				elif s[i] == ' ':
					i += 1
				else:
					return False, i
				if result == False:
					return False, i
			return False, i

		def squareBrackets(i, result):
			lens = len(s)
			while i < lens:
				if s[i] == ']':
					return True, i + 1
				elif s[i] == '{':
					result, i = curlyBrackets(i + 1, result)
				elif s[i] == '(':
					result, i = roundBrackets(i + 1, result)
				elif s[i] == '[':
					result, i = squareBrackets(i + 1, result)
				elif s[i] == ' ':
					i += 1
				else:
					return False, i
				if result == False:
					return False, i
			return False, i

		def roundBrackets(i, result):
			lens = len(s)
			while i < lens:
				if s[i] == ')':
					return True, i + 1
				elif s[i] == '{':
					result, i = curlyBrackets(i + 1, result)
				elif s[i] == '(':
					result, i = roundBrackets(i + 1, result)
				elif s[i] == '[':
					result, i = squareBrackets(i + 1, result)
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
			print (i)
			if s[i] == '{':
				result, i = curlyBrackets(i + 1, result)
			elif s[i] == '[':
				result, i = squareBrackets(i + 1, result)
			elif s[i] == '(':
				result, i = roundBrackets(i + 1, result)
			elif s[i] == ' ':
				i += 1
			else:
				return False
			if result == False:
				return False
		return True