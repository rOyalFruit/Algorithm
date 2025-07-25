def traverse(root, order):
    # Base Case: 리프 노드의 자식('.')에 도달하면 빈 리스트를 반환
    if root == '.':
        return []

    left_child, right_child = tree[root]

    # 재귀적으로 왼쪽과 오른쪽 서브트리의 결과를 미리 계산
    left_result = traverse(left_child, order)
    right_result = traverse(right_child, order)

    # 순서에 따라 루트와 자식들의 결과를 조합하여 반환
    if order == 'pre':
        return [root] + left_result + right_result
    elif order == 'in':
        return left_result + [root] + right_result
    else:  # 'post'
        return left_result + right_result + [root]


tree = {}
n = int(input())
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]

print("".join(traverse('A', 'pre')))
print("".join(traverse('A', 'in')))
print("".join(traverse('A', 'post')))
