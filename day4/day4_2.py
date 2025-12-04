def remove_rolls(grid_padded):
    accessible = 0
    next_grid = ['.' * (len(grid_padded[0]))]
    
    for i in range(1, len(grid_padded) - 1):
        next_grid_line = '.'
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
                next_grid_line += '.'
            else:
                next_grid_line += grid_padded[i][j]
        
        next_grid_line += '.'
        next_grid.append(next_grid_line)
        
    next_grid.append('.' * (len(grid_padded[0])))        
    return next_grid, accessible


grid = open('input.txt', 'r').readlines()
grid = [g.replace('\n', '') for g in grid]

grid_padded = ['.' * (len(grid[0]) + 2)]
for g in grid:
    grid_padded.append('.' + g + '.')
grid_padded.append('.' * (len(grid[0]) + 2))

next_grid, removed = remove_rolls(grid_padded)
accessible = removed
previous_accessible = 0

while accessible != previous_accessible:
    next_grid, removed = remove_rolls(next_grid)
    previous_accessible = accessible
    accessible += removed
    
print(accessible)
