# nlantau, 2022-01-01

from collections import deque

def breadth_depth_print(graph, source):
    queue = deque([source])

    while queue:
        curr = queue.popleft()
        print(curr)

        for neighbor in graph[curr]:
            queue.append(neighbor)


g = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}


if __name__ == "__main__":
    breadth_depth_print(g, 'a')
