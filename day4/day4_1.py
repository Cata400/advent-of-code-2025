grid = open('input.txt', 'r').readlines()
grid = [g.replace('\n', '') for g in grid]

grid_padded = ['.' * (len(grid[0]) + 2)]
for g in grid:
    grid_padded.append('.' + g + '.')
grid_padded.append('.' * (len(grid[0]) + 2))

accessible = 0

for i in range(1, len(grid_padded) - 1):
    for j in range(1, len(grid_padded[0]) - 1):
        v8 = [
            grid_padded[i - 1][j - 1],
            grid_padded[i - 1][j],
            grid_padded[i - 1][j + 1],
            grid_padded[i][j - 1],
            grid_padded[i][j + 1],
            grid_padded[i + 1][j - 1],
            grid_padded[i + 1][j],
            grid_padded[i + 1][j + 1],
        ]
        
        surrounding_papers = v8.count('@')
        
        if grid_padded[i][j] == '@' and surrounding_papers < 4: 
            accessible += 1
        
print(accessible)
