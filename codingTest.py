n = int(input())
f = [0, 1]
for i in range(2, n + 1):
    f.append(f[i - 1] + f[i - 2])
new_list = []
for i in range(len(f)):
    if f[i] % 2 != 0:
        new_list.append(f[i])
answer = sum(new_list) / len(new_list)
print(answer)




