import sys, re

cnt = 1
patron_seg = r"seg\(\((\d+),(\d+)\),\((\d+),(\d+)\)\)"
patron_size = r"size\((\d+)\)"

segs = []
size = 0

# Escribe la primera línea en un fichero
for line in sys.stdin:
    if cnt == 5:
        for coincidencia in re.findall(patron_seg, line):
            x1, y1, x2, y2 = map(int, coincidencia)
            segs.append(((x1, y1), (x2, y2)))

        size = int(re.search(patron_size, line).group(1))

        for i in range(size):
            for j in range(size):
                print("+", end = "")
                if j < (size - 1):
                    if ((i, j),(i, j + 1)) in segs:
                        print("--", end = "")
                    else:
                        print("  ", end = "")
            print("")
            if i < (size - 1):
                for j in range(size):
                    if ((i, j),(i + 1, j)) in segs:
                        print("|  ", end = "")
                    else:
                        print("   ", end = "")
                print("")
        
        break
    cnt += 1