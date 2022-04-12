class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    result = {}
    if root is None:
        return result
    result = {"val": root.val, "left": serialize(root.left), "right": serialize(root.right)}
    return result

def deserialize(data):
    if data == {}:
        return None
    root = Node(data["val"], deserialize(data["left"]), deserialize(data["right"]))
    return root

node = Node("root", Node("left", Node("left.left")), Node("right", Node("right.left"), Node("right.right")))
print(deserialize(serialize(node)).right.left.val)