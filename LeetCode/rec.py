# nlantau, 2021-12-28

class BTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __repr__(self):
        return f'{self.val}'

a = BTree('a')
b = BTree('b')
c = BTree('c')
d = BTree('d')
e = BTree('e')
f = BTree('f')

a.set_left(b)
a.set_right(c)
b.set_left(d)
b.set_right(e)
c.set_right(f)


def depth_first_val(root):
    if root == None: return []
    left = depth_first_val(root.left)
    right = depth_first_val(root.right)
    print(root)
    print("-----------------")
    print(left)
    print("-----------------")
    print(right)
    print("-----------------")
    return f'{root}, {left}, {right}'

print(depth_first_val(a))








