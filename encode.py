import sys

usage = """
        Uso:\tencode.py <input> [output]
        Si no se introduce un archivo de output, se creará uno del estilo 'input-solution.txt'.
        """

def convert_file(input_file, output_file):
    if input_file.endswith(".txt"):
        grid = []
        with open(input_file, 'r') as f:
            for line in f:
                if line.strip():
                    row = list(map(int, line.split()))
                    grid.append(row)

        size = len(grid)
        with open(output_file, 'w+') as f:
            f.write("size({}).\n".format(size))
            for i in range(size):
                for j in range(size):
                    if grid[i][j] != 0:
                        f.write("number(({},{}),{}).\n".format(i, j, grid[i][j]))
    else:
        print("Tipo de archivo no soportado.")


if len(sys.argv) == 1:
    print(usage)
elif len(sys.argv) == 2:
    convert_file(sys.argv[1], sys.argv[1].replace(".txt", "-solution.txt"))
else:
    convert_file(sys.argv[1], sys.argv[2])
