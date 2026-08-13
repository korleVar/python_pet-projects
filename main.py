symbols = {0: ' ', 1: '.', 4: 'd', 5: 'w'}

def base_map():
    matrix =[]
    for i in range(8):
        row = []
        for j in range(8):
            if i in range(0, 3) and (i + j) % 2 == 1:
                row.append(4)
            elif i in range(5, 8) and (i + j) % 2 == 1:
                row.append(5)
            else:
                row.append((i + j) % 2)
        matrix.append(row)
    for row in matrix:
        print(' '.join(map(symbols.get, row)))
    return matrix


def map_checker(start,finish):

    start_a = int(start[0])
    start_b = int(start[1])
    finish_a = int(finish[0])
    finish_b = int(finish[1])

    return start_a, start_b, finish_a, finish_b


def change_map(matrix, start_a, start_b, finish_a, finish_b, current_player):
    
    if start_a == finish_a and start_b == finish_b:
        return False

    move_direction = 1 if finish_a - start_a > 0 else -1

    if current_player["direction"] != move_direction:
        return False
    
    if  matrix[start_a][start_b] != current_player["color"]:
        return False
    if  matrix[finish_a][finish_b] == 4 or  matrix[finish_a][finish_b] == 5 :
        return False    
    row_diff = abs(finish_a - start_a)
    col_diff = abs(finish_b - start_b)
    mid_a = start_a + (finish_a - start_a) // 2
    mid_b = start_b + (finish_b - start_b) // 2

    if row_diff == 1 and col_diff == 1:
        matrix[finish_a][finish_b] = current_player["color"]
        matrix[start_a][start_b] = 1
    elif row_diff == 2 and col_diff == 2:
        opponent_color = 9 - current_player["color"]  # если твой цвет 4 -> чужой 5, и наоборот
        if matrix[mid_a][mid_b] != opponent_color:
            return False
        matrix[mid_a][mid_b] = 1          # клетка посередине освобождается (была тёмной, тёмной и остаётся)
        matrix[finish_a][finish_b] = current_player["color"]
        matrix[start_a][start_b] = 1
        current_player["score"] += 1
    else:
        return False
    return True    

def main():
    f_player = {"name": input('Введите имя игрока за белых: '), "color": 5}
    s_player = {"name": input('Введите имя игрока за черных: '), "color": 4}
    f_player["direction"] = -1
    s_player["direction"] = 1
    f_player["score"] = 0
    s_player["score"] = 0
    current_player = f_player

    matrix = base_map()

    while True:
        print (f"счет:{f_player['score']}:{s_player['score']}")
        print()
        print(f"Ход {current_player['name']}")
        start = input("start: ")
        finish = input("finish: ")

        start_a, start_b, finish_a, finish_b = map_checker(start, finish)
        result = change_map(matrix, start_a, start_b, finish_a, finish_b, current_player)

        if result:
            for row in matrix:
                print(' '.join(map(symbols.get, row)))
            current_player = s_player if current_player == f_player else f_player
        else:
            print("Недопустимый ход, попробуйте снова")
main()
