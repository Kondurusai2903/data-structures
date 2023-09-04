from collections import deque
# arr = [10, 12, 54, 27, 5, 6, 7]
# arr = [3, 2, 1, 4, 5]
# arr = [10, 5, 15, 4, 7, 8, 9, 13, 14]
# arr = [1, 2, 3, 4, 5, 6]
# arr = [4, 2, 5, 1, 6, 3]
# arr = [26, 10, 3, 4, 6, 3]
# arr = [12, 5, 7, 3, 1]
# arr = [1, 2, 3, 4]
arr = [5, 2, 1]
# ------------------------------------input array here----------------------------------------------


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
# ----------------------------Construct a complete binary tree from given array in level order fashion-----------------


def inorderBstfashion(arr, i, j):
    if i < j:
        mid = (i+j)//2
        root = Node(arr[mid])
        root.left = inorderBstfashion(arr, i, mid)
        root.right = inorderBstfashion(arr, mid+1, j)
        return root


def binarytreeinsert(arr, i, n):
    root = None
    if i < n:
        root = Node(arr[i])
        root.left = binarytreeinsert(arr, 2*i+1, n)
        root.right = binarytreeinsert(arr, 2*i+2, n)
    return root
# ----------------------------------binary insert function--------------------------------------------


def insert(root, key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    elif root.data > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
# ---------------------------------------binary_search function--------------------------------------------


def search(root, key):
    if root == None:
        return False
    while root != None:
        if root.data == key:
            return True
        elif root.data > key:
            root = root.left
        else:
            root = root.right
    return False
# -------------------------------------recursive inorder traversal------------------------------------------


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
# -------------------------------------recursive preorder traversal-----------------------------------------


def preorder(root):
    if root != None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
# -------------------------------------recursive postorder traversal-----------------------------------------


def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
# -----------------------------------levelorder traversal(using  extra None)------------------------------------


def levelorder(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)
    while len(q) > 1:
        curr = q.popleft()
        if curr == None:
            print()
            q.append(None)
            continue
        print(curr.data, end=" ")
        if curr.left != None:
            q.append(curr.left)
        if curr.right != None:
            q.append(curr.right)
# ----------------------------------------levelorder(method-2)--------------------------------------------------


def levelorder2(root):
    if root == None:
        return None
    q = deque()
    q.append(root)
    while len(q) > 0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            print(curr.data, end=" ")
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        print()
# ------------------------------------levelorderTraversal(reverse)----------------------------------------------


def reverselevelorder(root):
    if root is None:
        return None
    arr = []
    q = deque()
    q.append(root)
    while len(q) > 0:
        count = len(q)
        list = []
        for i in range(count):
            curr = q.popleft()
            list.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        arr.append(list)
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()
# ----------------------------------------height of binary Tree--------------------------------------------


def height(root):
    if root == None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        return lh+rh+1


# -----------------------------------diameter of a binary Tree----------------------------------------------
def diameter(root, res):
    if root == None:
        return 0
    else:
        lh = diameter(root.left, res)
        rh = diameter(root.right, res)
        res[0] = max(res[0], lh+rh+1)
        return max(lh, rh)+1
# ----------Mirror Tree(Create a mirror tree from the given binary tree)----------------------------------


def mirror(root):
    if root is None:
        return root
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
# ------------------------Inorder Traversal of a tree using Iteration---------------------


def iterativeinorder(root):
    # pass
    if root == None:
        return None
    st = []
    curr = root
    while curr != None:
        st.append(curr)
        curr = curr.left
    while len(st) > 0:
        curr = st.pop()
        print(curr.data, end=" ")
        curr = curr.right
        while curr != None:
            st.append(curr)
            curr = curr.left
# ----------------------Preorder Traversal of a tree  using Iteration-------------------------


def ownpreorder(root):
    if root == None:
        return None
    st = []
    while root != None:
        print(root.data, end=" ")
        if root.right != None:
            st.append(root.right)
        root = root.left
    while len(st) > 0:
        curr = st.pop()
        while curr != None:
            print(curr.data, end=" ")
            if curr.right != None:
                st.append(curr.right)
            curr = curr.left


def iterativepreorder(root):
    if root is None:
        return None
    st = []
    curr = root
    while curr != None or st:
        while curr != None:
            print(curr.data, end=" ")
            if curr.right != None:
                st.append(curr.right)
            curr = curr.left
        if st:
            curr = st.pop()

# --------------------------------Postorder Traversal of a tree  using Iteration---------------------------


def iterativepostorder(root):
    if root is None:
        return
    st = []
    while True:
        while root != None:
            st.append(root)
            st.append(root)
            root = root.left
        if len(st) == 0:
            return
        root = st.pop()
        if len(st) > 0 and st[-1] == root:
            root = root.right
        else:
            print(root.data, end=" ")
            root = None


# ----------------------------Print Left View of a Binary Tree--------------------------------------------
def leftview(root):
    arr = []
    if root == None:
        return arr
    q = deque()
    q.append(root)
    while len(q) > 0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            if i == 0:
                arr.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
    for i in arr:
        print(i, end=" ")
# --------------------------------------------Right View of Tree----------------------------------------------


def rightview(root):
    arr = []
    if root == None:
        return arr
    q = deque()
    q.append(root)
    while len(q) > 0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            if i == count-1:
                arr.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
    for i in arr:
        print(i, end=" ")

# --------------------------------------------Top View of a tree-----------------------------------------------


def topview(root):
    dict = {}
    if root == None:
        return None
    q = deque()
    q1 = deque()
    q.append(root)
    q1.append(0)
    while len(q) > 0:
        curr = q.popleft()
        hd = q1.popleft()
        if hd not in dict:
            dict[hd] = curr.data
        if curr.left != None:
            q.append(curr.left)
            q1.append(hd-1)
        if curr.right != None:
            q.append(curr.right)
            q1.append(hd+1)
    # arr = []
    for i in sorted(dict.keys()):
        print(dict[i], end=" ")
        # arr.append(dict[i])
    # return arr
# ----------------------------------------Bottom View of a Binary Tree----------------------------------------------------


def bottomview(root):
    dict = {}
    if root == None:
        return None
    q = deque()
    q1 = deque()
    q.append(root)
    q1.append(0)
    while len(q) > 0:
        curr = q.popleft()
        hd = q1.popleft()
        dict[hd] = curr.data
        if curr.left != None:
            q.append(curr.left)
            q1.append(hd-1)
        if curr.right != None:
            q.append(curr.right)
            q1.append(hd+1)
    for i in sorted(dict.keys()):
        print(dict[i], end=" ")
# ---------------------------------------Zig-Zag traversal of a binary tree-----------------------------------------------


def zigzagtraversal(root):
    if root == None:
        return
    st = []
    rev = False
    q = deque()
    q.append(root)
    while len(q) > 0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            if rev:
                st.append(curr)
            else:
                print(curr.data, end=" ")
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        if rev:
            while st:
                print(st.pop().data, end=" ")
        rev = bool(1-rev)
# --------------------------------Check if a tree is balanced or not(helper_function)-------------------------------------


def isbalanced(root):
    if root == None:
        return 0
    lh = isbalanced(root.left)
    if lh == -1:
        return -1
    rh = isbalanced(root.right)
    if rh == -1:
        return -1
    if abs(lh-rh) > 1:
        return -1
    return max(lh, rh)+1
# ------------------------------------------Check if a tree is balanced or not--------------------------------------------


def isbalancedmain(root):
    if isbalanced(root) == -1:
        return False
    return True
# ------------------------------Diagonal Traversal of Binary Tree------------------------------------------------------


def diagonaltraversal(root):
    if root == None:
        return
    st = deque()
    curr = root
    while st or curr != None:
        while curr != None:
            print(curr.data, end=" ")
            if curr.left != None:
                st.append(curr.left)
            curr = curr.right
        if st:
            curr = st.popleft()

# ---------------------------------------------Boundary traversal of a Binary tree-----------------------------------------


class boundary:
    def __init__(self):
        self.arr = []

    def isleaf(self, root):
        if root.left == None and root.right == None:
            return True
        return False

    def leftbouundary(self, root):
        self.arr.append(root.data)
        root = root.left
        while root != None:
            if self.isleaf(root) is not True:
                self.arr.append(root.data)
            if root.left:
                root = root.left
            else:
                root = root.right

    def rightboundary(self, root):
        root = root.right
        while root != None:
            if self.isleaf(root) is not True:
                self.arr.append(root.data)
            if root.right:
                root = root.right
            else:
                root = root.left

    def leafnodes(self, root):
        if root != None:
            self.leafnodes(root.left)
            if self.isleaf(root) == True:
                self.arr.append(root.data)
            self.leafnodes(root.right)
# ----------------------------------------Convert Binary tree into Doubly Linked List--------------------------------------


prev = None


def BinarytoDLL(root):
    if root == None:
        return root
    head = BinarytoDLL(root.left)
    global prev
    if prev == None:
        head = root
    else:
        prev.right = root
        root.left = prev
    prev = root
    BinarytoDLL(root.right)
    return head
# ---------------------------------------------Convert Binary tree into Sum tree-------------------------------------------


def sumtree(root):
    if root == None:
        return 0
    else:
        old_val = root.data
        root.data = sumtree(root.left)+sumtree(root.right)
        return root.data+old_val


# -----------------------------------construct binary tree from inorder and preorder traversals---------------------------
pre_index = 0


def binarytree(pre, io, isi, iei):
    if isi > iei:
        return None
    global pre_index
    root = Node(pre[pre_index])
    pre_index += 1
    if isi == iei:
        return root
    for i in range(isi, iei+1):
        if io[i] == root.data:
            break
    root.left = binarytree(pre, io, isi, i-1)
    root.right = binarytree(pre, io, i+1, iei)
    return root
# -----------------Minimum swap required to convert binary tree to binary search tree--------------------------------------
# ----------------------------it requires three steps :1->construct level order tree---------------------------------------
# ----------------------------step :2-> inorder traversal and store in arr ------------------------------------------------
# ------------------------------ step :3-> find the minimum swaps required  in arr-----------------------------------------


def minimunswaps(arr):
    res = [*enumerate(arr)]
    res.sort(key=lambda it: it[1])
    swaps = 0
    i = 0
    while i < len(arr):
        if res[i][0] == i:
            i += 1
            continue
        else:
            swaps += 1
            A = res[i][0]
            res[A], res[i] = res[i], res[A]
    return swaps


# -----------------------------------------Construct Binary Tree from String with BracketRepresentation--------------------
def BracketRepresentationTree(str):
    def findindex(str, si, ei):
        if si > ei:
            return -1
        st = []
        for i in range(si, ei+1):
            if str[i] == "(":
                st.append(str[i])
            elif str[i] == ")":
                if st[-1] == "(":
                    st.pop(-1)
                    if len(st) == 0:
                        return i
        return -1

    def treefromstring(str, si, ei):
        if si > ei:
            return None
        root = Node(ord(str[si])-ord("0"))
        print(root.data, end=" ")
        index = -1
        if si+1 <= ei and str[si+1] == "(":
            index = findindex(str, si+1, ei)
        if index != -1:
            root.left = treefromstring(str, si+2, index-1)
            root.right = treefromstring(str, index+2, ei-1)
        return root
    si = 0
    ei = len(str)-1
    root = treefromstring(str, si, ei)
    return root
# ------------------------------------------Check if a given Binary Tree is SumTree--------------------------------------


def sum(root):
    if root == None:
        return 0
    return sum(root.left)+root.data+sum(root.right)


def issumtree(root):
    if root == None or root.left == None and root.right == None:
        return 1
    lh = sum(root.left)
    # print(lh, end=" ")
    rh = sum(root.right)
    # print(rh, end=" ")
    if root.data == lh+rh and issumtree(root.left) and issumtree(root.right):
        return 1
    return 0
# -----------------------------------Check if all leaves are at samelevel--------------------------------------------------


def leaflevel(root):
    pass
    q = deque()
    q.append(root)
    res = []
    while len(q) > 0:
        count = len(q)
        a = []
        for i in range(count):
            curr = q.popleft()
            if curr.left == None and curr.right == None:
                a.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        if len(a) != 0:
            res.append(a)
    print(len(res))
    print(res)
    if len(res) > 1:
        return "not at same level"
    return "same level"
# -------------------------------------------maximum depth of binary Tree--------------------------------------------------


def maxdepth(root):
    if root == None:
        return 0
    lh = maxdepth(root.left)
    rh = maxdepth(root.right)
    return max(lh, rh)+1
# -------------------------------------------minimum depth of binary Tree--------------------------------------------------


def mindepth(root):
    if root == None:
        return 0
    lh = mindepth(root.left)
    rh = mindepth(root.right)
    if lh == 0 or rh == 0:
        return max(lh, rh)+1
    return min(lh, rh)+1


# --------------------------Min distance between two given nodes of a Binary Tree----------------------------------------
res = 0


def mindistance(root, a, b):
    if root == None:
        return 0
    left = mindistance(root.left, a, b)
    right = mindistance(root.right, a, b)
    global res
    if left != None and right != None:
        res = left+right
        return 0
    elif root.data == a or root.data == b:
        if left != None and right != None:
            res = max(left, right)
            return 0
        else:
            return 1
    else:
        if left != None or right != None:
            return max(left, right)+1
    return 0

# ---------------------------------------------inordersuccessor of a BST---------------------------------------------------


def inorderSuccessor(root, x):
    # Code here

    def successor(root, x, ans):
        # nonlocal ans
        if root == None:
            return None
        while root != None:
            # print(root.data, end=" ")
            if root.data <= x:
                root = root.right
            else:
                root = root.left
                ans = root

            # print(ans)
        return ans
    # print(ans)
    ans = None
    res = successor(root, x, ans)
    return res


# ---------------------------------Maximum difference between node and its ancestor----------------------------------------
res = float("-inf")
_max = float("inf")


def maxdifference(root):
    global res
    global _max
    if root == None:
        return _max, res
    if root.left == None and root.right == None:
        return root.data, res
    a, res = maxdifference(root.left)
    b, res = maxdifference(root.right)
    val = min(a, b)
    res = max(res, root.data-val)
    return min(val, root.data), res

    # m = maxdepth(root)
    # n = maxdepth(root)
    # if n == m:
    #     return "same level"
    # return "not in the same level"

    # root = None
    # res = [0]
    # for i in arr:
    #     root = insert(root, i)
root = binarytreeinsert(arr, 0, len(arr))
# root = inorderBstfashion(arr, 0, len(arr)-1)
# print()
# inorder(root)
# print()
# preorder(root)
# print()
# postorder(root)
# levelorder2(root)
# reverselevelorder(root)
# print(height(root))
# print(diameter(root, res))
# print(res[0])
# mirror(root)
# print()
# print("sai")
# iterativeinorder(root)
# iterativepreorder(root)
# print()
# ownpreorder(root)
# iterativepostorder(root)
# leftview(root)
# print()
# rightview(root)
# print()
# topview(root)
# print()
# bottomview(root)
# print()
# zigzagtraversal(root)
# print()
# print(isbalancedmain(root))
# print()
# diagonaltraversal(root)
# sai = boundary()
# sai.leftbouundary(root)
# sai.leafnodes(root)
# sai.rightboundary(root)
# print(sai.arr)
# head = BinarytoDLL(root)


# def printlist(head):
#     curr = head
#     while curr != None:
#         print(str(curr.data)+"->", end=" ")
#         curr = curr.right
# printlist(head)
# io = [20, 10, 40, 30, 50]
# pre = [10, 20, 30, 40, 50]
# root = binarytree(pre, io, 0, len(io)-1)
# iterativeinorder(root)
# print()
# print(minimunswaps(arr))

# str = "4(2(3)(1))(6(5))"
# root = BracketRepresentationTree(str)
# print()
# iterativeinorder(root)
# print(issumtree(root))
# print(leaflevel(root))
# a = 2
# b = 3
# mindistance(root, a, b)
# print(res)
# print(inorderSuccessor(root, 2))
maxdifference(root)
print(res)
