import sys

N = int(sys.stdin.readline())

house = []
for i in range(0, N):
    house.append(list(map(int, sys.stdin.readline().split())))

for j in range(1, N):
    house[j][0] = min(house[j][0] + house[j - 1][1], house[j][0] + house[j - 1][2])
    house[j][1] = min(house[j][1] + house[j - 1][0], house[j][1] + house[j - 1][2])
    house[j][2] = min(house[j][2] + house[j - 1][0], house[j][2] + house[j - 1][1])

print(min(house[N-1]))
