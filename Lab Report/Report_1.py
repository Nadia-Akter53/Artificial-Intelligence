from collections import deque


class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.level = z




class IDDFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]


        self.found = False
        self.goal_level = 0
        self.path = []




    def is_valid(self, x, y, graph, visited):
        return (
            0 <= x < len(graph) and
            0 <= y < len(graph[0]) and
            graph[x][y] == 0 and
            not visited[x][y]
        )


    def dfs_limited(self, x, y, tx, ty, depth, graph, visited):
        if depth < 0:
            return False


        visited[x][y] = True
        self.path.append((x, y))


   
        if x == tx and y == ty:
            return True


       
        for j in range(self.directions):
            nx = x + self.x_move[j]
            ny = y + self.y_move[j]


            if self.is_valid(nx, ny, graph, visited):
                if self.dfs_limited(nx, ny, tx, ty, depth - 1, graph, visited):
                    return True


       
        self.path.pop()
        visited[x][y] = False
        return False


 
    def run_iddfs(self, graph, sx, sy, tx, ty):
        max_depth = len(graph) + len(graph[0])  


        for depth in range(max_depth + 1):
            visited = [[False] * len(graph[0]) for _ in range(len(graph))]
            self.path = []


            if self.dfs_limited(sx, sy, tx, ty, depth, graph, visited):
                self.found = True
                self.goal_level = depth
                return True


        return False






if __name__ == "__main__":


   
    graph1 = [
        [0,0,1,0],
        [1,0,1,0],
        [0,0,0,0],
        [1,1,0,1]
    ]


    algo = IDDFS()
    ok = algo.run_iddfs(graph1, 0, 0, 2, 3)


    print("CASE 1:")
    if ok:
        print("Path found at depth", algo.goal_level)
        print("Traversal Order:", algo.path)
    else:
        print("Path not found")


   
    graph2 = [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ]


    algo2 = IDDFS()
    ok = algo2.run_iddfs(graph2, 0, 0, 2, 2)


    print("\nCASE 2:")
    if ok:
        print("Path found at depth", algo2.goal_level)
        print("Traversal Order:", algo2.path)
    else:
        print("Path not found at max depth", len(graph2) + len(graph2[0]))
