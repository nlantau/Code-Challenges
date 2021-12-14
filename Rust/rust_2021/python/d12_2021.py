# nlantau, 2021-12-14

class Cave:
    def __init__(self, name):
        self._name = name
        self._is_start = self.is_start()
        self._is_end   = self.is_end()
        self._connected_to = None
        self._is_small_cave = self.is_small()
        self._visited = False

    def set_visited(self):
        self._visited = True

    def is_small(self):
        if self._is_start or self._is_end: return False
        return self._name.lower() == self._name

    def connected_to(self, other):
        self._connected_to = other._name

    def is_start(self):
        return 'start' in self._name

    def is_end(self):
        return 'end' in self._name

    def __repr__(self):
        a = f"Cave: {self._name}"; b = f"Start: {self._is_start}"
        c = f"End: {self._is_end}"; d = f"Connected to: {self._connected_to}"
        e = f"Small Cave: {self._is_small_cave}"; return f'\n{a}\n{b}\n{c}\n{d}\n{e}\n'

class Graph:
    def __init__(self):
        self._nodes = []



def get_input():
    """ Parse input to list of tuples """
    data = "../assets/d12_2021_test_1.txt"
    return [tuple(a.split('-')) for a in open(data).read().split()]

def create_caves(lot):
    caves = list()
    for c1, c2 in lot:
        c1 = Cave(c1); c2 = Cave(c2)
        c1.connected_to(c2); c2.connected_to(c1)
        caves.append(c1); caves.append(c2)
    return caves


def main():
    pinp = get_input()
    print(pinp)
    caves = create_caves(pinp)
    print(caves)

if __name__ == "__main__":
    main()
