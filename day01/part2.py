def calculate_similarity_score(left_list, right_list):

    score = 0
    
    for num in left_list:
        appearances = right_list.count(num)
        score += num * appearances
        
    return score


def main(lines):
	col1, col2 = zip(*(map(int, line.split()) for line in lines))

	sorted_col1 = sorted(col1)
	sorted_col2 = sorted(col2)

	score = calculate_similarity_score(sorted_col1, sorted_col2)

	print(score)


if __name__ == "__main__":
	with open('input.txt', 'r') as file:
		lines = file.readlines()

	main(lines)
