from collections import defaultdict


def preorder(tree, root):
    global preorder_result
    preorder_result.append(root)

    if tree[root][0] != '.':
        preorder(tree, tree[root][0])

    if tree[root][1] != '.':
        preorder(tree, tree[root][1])

    return

def inorder(tree, root):
    global inorder_result
    if tree[root][0] != '.':
        inorder(tree, tree[root][0])

    inorder_result.append(root)

    if tree[root][1] != '.':
        inorder(tree, tree[root][1])

    return

def postorder(tree, root):
    global postorder_result
    if tree[root][0] != '.':
        postorder(tree, tree[root][0])

    if tree[root][1] != '.':
        postorder(tree, tree[root][1])

    postorder_result.append(root)

    return

tree = defaultdict(list)
n = int(input())
for _ in range(n):
    parent, left, right = input().split(" ")
    tree[parent] = [left, right]

preorder_result = []
inorder_result = []
postorder_result = []

preorder(tree, 'A')
inorder(tree, 'A')
postorder(tree, 'A')

print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))
