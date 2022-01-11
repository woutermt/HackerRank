import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):

        data_vals = str(root.data)
        nodes = [root]

        for i in range(T):
            if nodes[i].left != None:
                nodes.append(nodes[i].left)
                data_vals += (' ' + str(nodes[i].left.data))

            if nodes[i].right != None:
                nodes.append(nodes[i].right)
                data_vals += (' ' + str(nodes[i].right.data))

        print(str(data_vals))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
