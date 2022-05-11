class MinStack:
	def __init__(self):
		self.stack = []

	def push(self, val: int) -> None:
		min_value = self.getMin()
		if min_value == None or val < min_value:
			min_value = val
		self.stack.append((val, min_value))

	def pop(self) -> None:
		self.stack.pop()

	def top(self) -> int:
		if not self.stack:
			return None
		return self.stack[-1][0]

	def getMin(self) -> int:
		if not self.stack:
			return None
		return self.stack[-1][1]