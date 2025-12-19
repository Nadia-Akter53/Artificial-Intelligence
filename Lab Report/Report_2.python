import heapq




def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)




def a_star_search(grid, sx, sy, tx, ty):
    rows = len(grid)
    cols = len(grid[0])
   
    visited = [[False] * cols for _ in range(rows)]
    pq = []  
   
   
    heapq.heappush(pq, (0, 0, sx, sy, [(sx, sy)]))
   
    while pq:
        f, g, x, y, path = heapq.heappop(pq)
       
        if visited[x][y]:
            continue
        visited[x][y] = True
       
       
        if x == tx and y == ty:
            return True, g, path
       
       
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
           
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if not visited[nx][ny]:
                    new_g = g + 1
                    h = manhattan(nx, ny, tx, ty)
                    f_cost = new_g + h
                    heapq.heappush(pq, (f_cost, new_g, nx, ny, path + [(nx, ny)]))
   
    return False, -1, []




def read_input():
    with open("/input.txt", "r") as file:
        R, C = map(int, file.readline().split())
       
        grid = []
        for _ in range(R):
            row = list(map(int, file.readline().split()))
            grid.append(row)
       
        sx, sy = map(int, file.readline().split())
        tx, ty = map(int, file.readline().split())
   
    return grid, sx, sy, tx, ty




if __name__ == "__main__":
    grid, sx, sy, tx, ty = read_input()
    found, cost, path = a_star_search(grid, sx, sy, tx, ty)
   
    if found:
        print(f"Path found with cost {cost} using A*")
        print("Shortest Path:", path)
    else:
        print("Path not found using A*")
