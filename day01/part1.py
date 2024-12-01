def main(lines):
	col1, col2 = zip(*(map(int, line.split()) for line in lines))

	sorted_col1 = sorted(col1)
	sorted_col2 = sorted(col2)

	diffs = [abs(a - b) for a, b in zip(sorted_col1, sorted_col2)]

	print(sum(diffs))




if __name__ == "__main__":
	with open('input.txt', 'r') as file:
		lines = file.readlines()

	main(lines)