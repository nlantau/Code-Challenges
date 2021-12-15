# nlantau, 2021-12-15

sample = r'../assets/d15_2021_test.txt'
data   = r'../assets/d15_2021.txt'


with open(sample, 'r') as r:
    data = r.read().split()

data = [[int(i) for i in row] for row in data]

print(*data, sep='\n')

# Implement Djikstra's or A* 
