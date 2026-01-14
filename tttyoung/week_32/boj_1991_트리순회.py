tree = {}
n = int(input())
for i in range(n):
    par, left, right = map(str, input().split())
    tree[par] = [left, right]

result1 = []
result2 = []
result3 = []

def preorder(a): #먼저 루트노드 방문
    if a == '.':
        return 
    result1.append(a) #전위순회
    if tree[a][0] != '.':
        preorder(tree[a][0])
    if tree[a][1] != '.':
        preorder(tree[a][1])

def inorder(a): #왼쪽 자식노드 방문
    if a == '.':
        return 
    if tree[a][0] != '.':
        inorder(tree[a][0])
    result2.append(a) #중위순회
    if tree[a][1] != '.':
        inorder(tree[a][1])

def postorder(a): #오른쪽 자식노드 방문
    if a == '.':
        return 
    if tree[a][0] != '.':
        postorder(tree[a][0])
    if tree[a][1] != '.':
        postorder(tree[a][1])
    result3.append(a) #후위순회

preorder('A')
inorder('A')
postorder('A')
print("".join(result1))
print("".join(result2))
print("".join(result3))