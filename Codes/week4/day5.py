# 145. Binary Tree Postorder Traversal 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.ans = []
    
    def postorder(self, root):
        # base case 
        if root is None:
            return
        
        # recursive case 
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)


    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        self.ans= []
        self.postorder(root)
        return self.ans




# 94. Binary Tree Inorder Traversal 


class Solution:
    def __init__(self):
        self.ans = []
    
    def inorder(self, root):
        # base case 
        if root is None:
            return
        
        # recursive case 
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)


    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        self.ans= []
        self.inorder(root)
        return self.ans



# 144. Binary Tree Preorder Traversal

class Solution:
    def __init__(self):
        self.ans = []
    
    def preorder(self, root):
        # base case 
        if root is None:
            return
        
        # recursive case 
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)


    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        self.ans= []
        self.preorder(root)
        return self.ans

# 100 same tree 



class Solution:
    def __init__(self):
        self.ans = []
        self.ans1 = []

    def preorder(self, root, arr):

        # Base case
        if root is None:
            arr.append(None)
            return

        # Recursive case
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    def isSameTree(self, p, q):

        self.ans = []
        self.ans1 = []

        self.preorder(p, self.ans)
        self.preorder(q, self.ans1)

        return self.ans == self.ans1
