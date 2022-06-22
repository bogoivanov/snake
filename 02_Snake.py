def is_outside(next_row, next_col, size):
    return next_row < 0 or next_col < 0 or next_row >= size or next_col >= size


def get_next_position(snake_row, snake_col, direction, matrix):
    if direction == "up":
        return snake_row - 1, snake_col
    if direction == "down":
        return snake_row + 1, snake_col
    if direction == "left":
        return snake_row, snake_col - 1
    if direction == "right":
        return snake_row, snake_col + 1


size = int(input())

matrix = []
snake_row = 0
snake_col = 0
bur_one_row = 0
bur_one_col = 0
bur_two_row = 0
bur_two_col = 0
count = 1
for row in range(size):
    row_element = list(input())
    matrix.append(row_element)
    for col in range(size):
        if row_element[col] == "S":
            snake_row = row
            snake_col = col
        if row_element[col] == "B" and count == 1:
            bur_one_row = row
            bur_one_col = col
            matrix[bur_one_row][bur_one_col] = f"B{count}"
            count += 1
        elif row_element[col] == "B" and count == 2:
            bur_two_row = row
            bur_two_col = col
            matrix[bur_two_row][bur_two_col] = f"B{count}"

food_quantity = 0

game_over = False
game_win = False
while True:
    matrix[snake_row][snake_col] = "."
    direction = input()
    next_row, next_col = get_next_position(snake_row, snake_col, direction, matrix)
    if is_outside(next_row, next_col, size):
        game_over = True
        break
    if matrix[next_row][next_col] == "B1":
        matrix[next_row][next_col] = "."
        next_row, next_col = bur_two_row, bur_two_col
    elif matrix[next_row][next_col] == "B2":
        matrix[next_row][next_col] = "."
        next_row, next_col = bur_one_row, bur_one_col
    elif matrix[next_row][next_col] == "*":
        food_quantity += 1
    snake_row, snake_col = next_row, next_col
    matrix[snake_row][snake_col] = "S"
    if food_quantity >= 10:
        game_win = True
        break
if game_over:
    print("Game over!")
if game_win:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "B1":
            matrix[row][col] = "B"
        if matrix[row][col] == "B2":
            matrix[row][col] = "B"

for row in matrix:
    print(*row, sep="")
