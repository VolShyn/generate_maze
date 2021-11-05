import random

def generate_maze(max_rows, max_cols, max_mines):
	
	#let's create a minefield
	minefield = []
	current_position = 0
	for row in range(max_rows):
		minefield.append([])
		for column in range(max_cols):
			minefield[current_position].append(0)
		current_position += 1
	
	#let's generate coordinates for mines
	mine_coordinates = []
	coordinate = []
	for mine in range(max_mines):
		
		coordinate.append([random.randint(0, max_rows-1), random.randint(0, max_cols-1)])
		while coordinate[0] in mine_coordinates:
			coordinate = []
			coordinate.append([random.randint(0, max_rows-1), random.randint(0, max_cols-1)])

		mine_coordinates.append(coordinate[0]) 

	#let's put the mines into the minefield
	mine = 0
	s = 0
	i = 0 #rows' number on the minefield
	j = 0 #columns' number on the minefield
	for mine in mine_coordinates:
		i = mine[0]
		j = mine[1]
		minefield[i][j] = -1 
	#let's fill the minefield with numbers
	row = 0
	i = 0 #rows' number on the minefield
	j = 0 #columns' number on the minefield
	for row in minefield:

		for cell in row:
			if cell == -1:
				j += 1
			else:
				check_radius = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]

				#let's review that our check_radius don't go out the minefield
				for check in check_radius:
					if check[0] < 0:
						check_radius[check_radius.index(check)][0] = 0
					elif check[0] > (max_rows-1):
						check_radius[check_radius.index(check)][0] = (max_rows-1)

					if check[1] < 0:
						check_radius[check_radius.index(check)][1] = 0
					elif check[1] > (max_cols-1):
						check_radius[check_radius.index(check)][1] = (max_cols-1)


				#let's be sure that all items in "check_radius" are unique

				unique_checker = []
				p = 1
				for check in check_radius:
					if check in check_radius[p:]:
						unique_checker.append(1)
					else:
						unique_checker.append(0)
					p += 1

				p = 0
				for value in unique_checker:
					if value == 1:
						check_radius.pop(p)
					else:
						p += 1

				#let's count how many mines around [i,j] point on the minefield
				check = 0
				mines_around = 0
				for check in check_radius:
					if minefield[check[0]][check[1]] == -1:
						 mines_around += 1

				minefield[i][j] = mines_around
				mines_around = 0
				j += 1

		i += 1
		j = 0
		s = 0
	#we're ready to send the minefield to the user
	return minefield


x = generate_maze(10,10,10)

#Here i simply try to show you the minefield with mines and numbers 
coco = 0
for c in range(10):
	print(x[coco])
	coco += 1
