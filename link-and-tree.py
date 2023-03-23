class BinaryTree:
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

def preorder(t):
    yield t.label
    if t.left:
        yield from preorder(t.left)
    if t.right:
        yield from preorder(t.right)

def postorder(t):
    if t.left:
        yield from postorder(t.left)
    if t.right:
        yield from postorder(t.right)
    yield t.label

t = BinaryTree(13, BinaryTree(5, BinaryTree(2, BinaryTree(1), BinaryTree(3)), BinaryTree(8)), BinaryTree(21))
print(list(postorder(t)))  # [13, 5, 2, 1, 3, 8, 21]

