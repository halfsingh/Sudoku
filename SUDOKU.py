""" PYTHON CODE FOR SOLVING AND PLAYING SUDOKU"""

bo=[

[0,0,0,6,0,5,0,3,2],
[0,2,0,7,0,0,5,9,0],
[0,0,3,2,0,0,7,6,0],
[0,0,0,3,0,2,0,0,0],
[0,0,1,5,6,0,0,2,0],
[2,4,5,1,9,0,6,0,0],
[3,5,4,0,0,6,8,0,1],
[8,0,9,0,7,0,0,0,0],
[7,0,2,8,5,0,3,0,0]

]

def valid_or_not(board, num, pos):

	#Check the row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	#Check the column
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	#Check tiny squares
	square_x = pos[1] //3
	square_y = pos[0] //3

	for i in range(square_x*3,square_x*3+3):
		for j in range(square_y*3,square_y*3+3):
			if board[j][i] == num and (j,i)!= pos:
				return False
	return True


def print_board(board):

	for i in range(len(board)):
		if i%3==0 and i!=0:
			print("- - - - - - - - - - - - ")


		for j in range(len(board[0])):
			if j%3 == 0 and j!= 0:
				print(" | ", end = "")


			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + " ",end="")

#print_board(bo)


def find_empty_box(board):

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return(i,j) #row, col

	return None


def solve(board):

	find = find_empty_box(board)
	if not find:
		return True

	else:
		row, col = find

	for i in range(1,10):
		if valid_or_not(board, i, (row,col)):
			board[row][col] = i

			if solve(board):
				return True

			board[row][col] = 0

	return False

print_board(bo)
print(".........................................")
print(".........................................")
solve(bo)
print(".........................................")
print(".........................................")
print_board(bo)