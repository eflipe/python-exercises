arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
    ]



# print(arr[0][0], arr[0][1], arr[0][2],
#                arr[1][1],
#       arr[2][0], arr[2][1], arr[2][2])

maximo = []
for i in range(4):
    for j in range(4):
        suma = []
        estructura = [arr[i][j], arr[i][j+1], arr[i][j+2],
                   arr[i+1][j+1],
          arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
        for estruc in estructura:

            suma.append(estruc)
        maximo.append(sum(suma))
print(max(maximo))


# otra
res = []
for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print(max(res))
# otra
m = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        try:
            m.append(sum([arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]))
        except IndexError as e:
            continue
print(max(m))
