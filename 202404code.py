D = open("202404input.txt").read().split('\n')

grid = [[char for char in line] for line in D]

rows_grid = len(grid)
cols_grid = len(grid[0])

# print(grid)

p1 = p2 = 0

dir = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]

for r in range(rows_grid):
    for c in range(cols_grid):
        if grid[r][c] == 'X': 
            for r_a, c_a in dir:
                end_r = r + 3*r_a
                end_c = c + 3*c_a
                if 0 <= end_r < rows_grid and 0 <= end_c < cols_grid:
                    if grid[r+r_a][c+c_a] + grid[r+2*r_a][c+2*c_a] + grid[r+3*r_a][c+3*c_a] == 'MAS':
                        p1 += 1
print(p1)

# for part 2 start searching from 'A'
# for each 'A' the diagonals should be MS and/or SM

for r in range(1, rows_grid-1):
    for c in range(1, cols_grid-1):
        if grid[r][c] == 'A': 
            if {(grid[r-1][c-1] + grid[r+1][c+1]),(grid[r-1][c+1] + grid[r+1][c-1])} <= {'MS', 'SM'}:
                p2+=1
print(p2)

"""             if ((grid[r-1][c-1] == grid[r-1][c+1] == 'M' and grid[r+1][c-1] == grid[r+1][c+1] == 'S')  
                or (grid[r-1][c-1] == grid[r-1][c+1] == 'S' and grid[r+1][c-1] == grid[r+1][c+1] == 'M') 
                or (grid[r-1][c-1] == grid[r+1][c-1] == 'M' and grid[r-1][c+1] == grid[r+1][c+1] == 'S')
                or (grid[r-1][c-1] == grid[r+1][c-1] == 'S' and grid[r-1][c+1] == grid[r+1][c+1] == 'M')):
                    p2 += 1 """