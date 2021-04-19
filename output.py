def output(field):
    for row in field:
        line = ''

        for column in row:
            line += column

        print(line)

