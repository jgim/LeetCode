class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		if not n:
			return []
		left, right, answer = n, n, []
		self.dfs(left, right, answer, "")
		return answer

	def dfs(self, left, right, answer, string):
		if right < left:
			return
		if not left and not right:
			answer.append(string)
			return
		if left:
			self.dfs(left - 1, right, answer, string+"(")
		if right:
			self.dfs(left, right - 1, answer, string+")")