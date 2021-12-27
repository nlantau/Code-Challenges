# nlantau, 2021-12-15

from queue import PriorityQueue


sample = r'../assets/d15_2021_test.txt'
data   = r'../assets/d15_2021.txt'


with open(sample, 'r') as r:
    data = [[int(i) for i in row] for row in r.read().split()]
    #data = r.read().split()


print(*data, sep='\n')

pq = PriorityQueue()





# Implement Djikstra's or A* 
