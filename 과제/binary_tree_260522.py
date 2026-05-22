def make_tree(tree):
    mid, left, right = input().split()
    tree[mid] = [left, right]

# 딕셔너리 선위 순회
def preorder(node):
    if node == '.': return
    print(node, end = '')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 딕셔너리 중위 순회
def inorder(node):
    if node == '.': return
    inorder(tree[node][0])
    print(node, end = '')
    inorder(tree[node][1])

# 딕셔너리 후위 순회
def postorder(node):
    if node == '.': return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = '')


count = int(input())
tree = {}
for i in range (count):
    make_tree(tree)
    
root = list(tree.keys())[0]

print("전위 순회한 결과 : ", end = '')
preorder(root)
print()

print("중위 순회한 결과 : ", end = '')
inorder(root)
print()

print("후위 순회한 결과 : ", end = '')
postorder(root)