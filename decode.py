import re, sys, linecache

usage = """
        Uso:\tdecode.py <input> [output]
        Si no se introduce un archivo de output, se creará uno del estilo 'input-decode.txt'.
        """


def decode(input_string, output_file):
    patron_seg = r"seg\(\((\d+),(\d+)\),\((\d+),(\d+)\)\)"
    patron_size = r"size\((\d+)\)"
    
    segs = []
    size = 0

    for coincidencia in re.findall(patron_seg, input_string):
        x1, y1, x2, y2 = map(int, coincidencia)
        segs.append(((x1, y1), (x2, y2)))

    size = int(re.search(patron_size, input_string).group(1))

    with open(output_file, 'w+') as f:
        for i in range(size):
            for j in range(size):
                print("+", end = "", file = f)
                if j < (size - 1):
                    if ((i, j),(i, j + 1)) in segs:
                        print("--", end = "", file = f)
                    else:
                        print("  ", end = "", file = f)
            print("", file = f)
            if i < (size - 1):
                for j in range(size):
                    if ((i, j),(i + 1, j)) in segs:
                        print("|  ", end = "", file = f)
                    else:
                        print("   ", end = "", file = f)
                print("", file = f)


if len(sys.argv) == 1:
    print(usage)
elif len(sys.argv) == 2:
    decode(linecache.getline(sys.argv[1], 5), sys.argv[1].replace(".txt", "-decode.txt"))
else:
    decode(linecache.getline(sys.argv[1], 5), sys.argv[2])
