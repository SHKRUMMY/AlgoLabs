import sys
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.is_left_heavy = False
        self.is_right_heavy = False

class AVLTree:

    def getHeight(self, root):
        if not root:
            return 0
        return root.height


    def getBalanceFactor(self, node):
        if not node:
            return 0
        if self.getHeight(node.left)- self.getHeight(node.right) > 1:
            node.is_left_heavy = True
        elif self.getHeight(node.left) - self.getHeight(node.right) < -1:
            node.is_right_heavy = True
        return self.getHeight(root.left) - self.getHeight(root.right)


    def leftRotate(self, element):
        beta = element.right
        alpha = beta.left
        beta.left = element
        element.left = alpha

        element.height = 1 + max(self.getHeight(element.left), self.getHeight(element.right))
        beta.height = 1 + max(self.getHeight(beta.left), self.getHeight(beta.right))

        return  beta

    def rightRotate(self, element):
        beta = element.left
        alpha = element.right
        beta.right = element
        element.left = alpha

        element.height = 1 + max(self.getHeight(element.left), self.getHeight(element.right))
        beta.height = 1 + max(self.getHeight(beta.left), self.getHeight(beta.right))

        return beta



    # def insertRoot(self, key):
    #     if not root:
    #         return Node(key)
    #     else:
    #         print("Root is already set")

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else :
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        bf = self.getBalanceFactor(root)
        if root.is_left_heavy:
                if key < root.left.key:
                    return self.rightRotate(root)
                else:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)

        if root.is_right_heavy:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # def printHelper(self, currPtr, indent, last):
    #     if currPtr != None:
    #         sys.stdout.write(indent)
    #         if last:
    #             sys.stdout.write("R----")
    #             indent += "     "
    #         else:
    #             sys.stdout.write("L----")
    #             indent += "|    "
    #         print(currPtr.key)
    #         self.printHelper(currPtr.left, indent, False)
    #         self.printHelper(currPtr.right, indent, True)


    def makeList(self, root):
        key_list = []
        start_root = root
        while root.left != None:
            key_list.append(root.left.key)
            root = root.left

        while start_root.right != None:
            key_list.append(start_root.right.key)
            start_root = start_root.right

        print(key_list)


myTree = AVLTree()
root = None
nums = [33, 13, 52, 91, 21, 61, 8, 11]

for num in nums:
    root = myTree.insert(root, num)

print(root.left.left.key)

myTree.makeList(root)
# myTree.printHelper(root, "", True)

