class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
    def __str__(self, level=0, prefix="Root: "):
        ret = f"\t" * level + prefix + str(self.val) + f"\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def max_value(node):
    current = node
    while current.right:
        current = current.right
    return current

def min_value(node):
    current = node
    while current.left:
        current = current.left
    return current

def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)


root = Node(5)
values = [15, 10, 20, 8, 12, 17, 25]
for value in values:
    root = insert(root, value)
    
print(root)

print("Найбільше значення в дереві:", max_value(root).val)
print("Найменше значення в дереві:", min_value(root).val)
print("Сума всіх значень у дереві:", sum_tree(root))

