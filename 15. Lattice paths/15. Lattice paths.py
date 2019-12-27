maze=[]
row1=[]
for i in range(21):
    row1.append(1)
maze.append(row1)
for i in range(20):
    maze.append([1])

for j in range(20):
    for i in range(20):
        maze[j+1].append(maze[j+1][i]+maze[j][i+1])
print(maze[-1][-1])
        
