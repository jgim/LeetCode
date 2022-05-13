class Solution:
	def generateParenthesis(self, n):
		result = []
		string = [("(", n - 1, n)]
		while string:
			brakets, left, right = string.pop()
			if left - right > 0 or left < 0 or right < 0:
				continue
			if left == 0 and right == 0:
				result.append(brakets)
			string.append((brakets + "(", left - 1, right))
			string.append((brakets + ")", left, right - 1))
		return result