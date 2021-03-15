### still not sure if it's easier to write code in here rather than in the online editor...

# if __name__ == '__main__':
list = []
N = int(raw_input())
for num in range(N):
    line = raw_input().split()
    if len(line) > 2:
        list.insert(line[2,1])
    cmd, first, second = line[0], line[1], line[2]
print(list)