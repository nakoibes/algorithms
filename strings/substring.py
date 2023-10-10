string1 = "clues"
string2 = "blue"

table = [[0 for _ in range(len(string1))] for _ in range(len(string2))]

for i in range(len(string1)):
    if string2[0] == string1[i]:
        table[0][i] += 1

for i in range(1, len(string2)):
    letter = string2[i]
    for j in range(len(string1)):
        if letter == string1[j]:
            table[i][j] = table[i - 1][j - 1] + 1


max_num = 0
row = 0
for i in range(len(string2)):
    current_max = max(table[i])
    if current_max > max_num:
        row = i
        max_num = current_max

res = string2[row-max_num + 1:row+1]
print(res)
