# CodeVita Forest Fire problem.

forest = []
time = []

M, N = map(int, input("Enter the length of forest in rows and columns: ").split())

X, Y = map(int, input("Enter the location of first tree that catches the fire: ").split())

for i in range(0, M):
    temp = []
    for j in range(0, N):
        temp.append(input())
    forest.append(temp)
    
# print(forest)

for i in range(0, M):
    temp1 = []
    for j in range(0, N):
        temp1.append(0)
    time.append(temp1)
    

# print(time)



def total_time(row, col, cur_time):
    
    if row < 0 or row > (M-1) or col < 0 or col > (N-1):
        return
    
    if forest[row][col] == 'W':
        return
    
    if time[row][col] != 0 and cur_time >= time[row][col]:
        return
    
    
    time[row][col] = cur_time 
    
    total_time(row+1, col+1, cur_time+1)
    total_time(row-1, col-1, cur_time+1)
    total_time(row+1, col-1, cur_time+1)
    total_time(row-1, col+1, cur_time+1)
    total_time(row+1, col, cur_time+1)
    total_time(row-1, col, cur_time+1)
    total_time(row, col+1, cur_time+1)
    total_time(row, col-1, cur_time+1)
    
    

total_time((X-1),(Y-1), 1)

# print(time)

maxi = time[0][0]

for i in range(0, len(time)):
    for j in range(0, len(time[i])):
        if maxi < time[i][j]:
            maxi = time[i][j]
            
print(maxi)
