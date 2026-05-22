def make_tree(tree):
    mid, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[mid] = [left, right]
    return mid

# 딕셔너리 선위 순회
def preorder(node):
    if node == None: return
    print(node, end = '')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 딕셔너리 중위 순회
def inorder(node):
    if node == None: return
    inorder(tree[node][0])
    print(node, end = '')
    inorder(tree[node][1])

# 딕셔너리 후위 순회
def postorder(node):
    if node == None: return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = '')


count = int(input())
tree = {}
for i in range (count):
    if i != 0:
        make_tree(tree)
    else:
        root = make_tree(tree)


print("전위 순회한 결과 : ", end = '')
preorder(root)
print()
print("중위 순회한 결과 : ", end = '')
inorder(root)
print()
print("후위 순회한 결과 : ", end = '')
postorder(root)