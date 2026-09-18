def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	ans = [0 for i in range(len(a))]
	if len(a)==len(b):
		for j in range(len(a)): 
			for i in range(len(a[0])):
				ans[j]=ans[j]+a[j][i]*b[i]
		return ans
	else:
		return -1
