def check_field(field):
    for i in range(3):
        if all(field[i][0] == j for j in (field[i][1], field[i][2])):
            if field[i][0] != ' ':
                return True

        if all(field[0][i] == j for j in (field[1][i], field[2][i])):
            if field[0][i] != ' ':
                return True

    if all(field[0][0] == j for j in (field[1][1], field[2][2])):
        if field[0][0] != ' ':
            return True

    if all(field[2][0] == j for j in (field[1][1], field[0][2])):
        if field[2][0] != ' ':
            return True

    return False

