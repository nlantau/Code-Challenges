# nlantau, 2022-01-01

def depth_first_print(graph, source):
    stack = [source]

    while stack:
        curr = stack.pop()
        print(curr)

        for neighbor in graph[curr]:
            stack.append(neighbor)

def depth_first_print_rec(graph, source):
    print(source)
    visited = [source]
    for neighbor in graph[source]:
        visited += depth_first_print_rec(graph, neighbor)
    return visited



g = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

if __name__ == "__main__":
    depth_first_print(g, 'a')
    print(f'{"":-^30}')
    print(depth_first_print_rec(g, 'a'))