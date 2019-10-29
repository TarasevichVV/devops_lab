w, h = map(int, input().split())
n = int(input())
S = 0
a = [[0 for x in range(w)] for y in range(h)]


def rectangle_area(x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            a[y][x] = 1


for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangle_area(x1, y1, x2, y2)
for y in range(w):
    for x in range(h):
        S += 1 - a[x][y]
print(S)
