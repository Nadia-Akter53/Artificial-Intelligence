#Solve Graph Coloring Problem using Backtracking Algorithm in Python

def read_graph_data(filename):
   
    with open(filename, 'r') as f:
       
        n, m, k = map(int, f.readline().split())
       
       
        adj_list = [[] for _ in range(n)]
       
       
        for _ in range(m):
            u, v = map(int, f.readline().split())
            adj_list[u].append(v)
            adj_list[v].append(u)
       
        return n, m, k, adj_list


def can_use_color(vertex, color, coloring, graph):
 
    for neighbor in graph[vertex]:
        if coloring[neighbor] == color:
            return False
    return True


def try_coloring(current_vertex, num_vertices, num_colors, coloring, graph):
   
   
    if current_vertex == num_vertices:
        return True
   
   
    for color in range(1, num_colors + 1):
        if can_use_color(current_vertex, color, coloring, graph):
           
            coloring[current_vertex] = color
           
           
            if try_coloring(current_vertex + 1, num_vertices, num_colors, coloring, graph):
                return True
           
           
            coloring[current_vertex] = 0
   
    return False


def solve_graph_coloring():
   
    filename = "input_case1.txt"
   
   
    vertices, edges, colors, graph = read_graph_data(filename)
   
   
    color_assignment = [0] * vertices
   
   
    if try_coloring(0, vertices, colors, color_assignment, graph):
        print(f"Coloring Possible with {colors} Colors")
       
        result = [color_assignment[i] for i in range(vertices)]
        print(f"Color Assignment: {result}")
        return True
    else:
        print(f"Coloring Not Possible with {colors} Colors")
        return False




if __name__ == "__main__":
    solve_graph_coloring()
