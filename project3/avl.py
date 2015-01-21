# AVL Trees, by Elizabeth Feicke

# Was unable to complete this file.

from BST import BSTNode, BinarySearchTree

class AVLNode(BSTNode):
    def __init__(self, key, left=None, right=None, parent=None):
        BSTNode.__init__(self, key, left, right, parent)
        self.height = self.node_height()

    def node_height(self):
        if self.left and self.right:
            self.left.height = self.left.node_height()
            self.right.height = self.right.node_height()
            return max(self.left.height, self.right.height) + 1
        elif self.left:
            self.left.height = self.left.node_height()
            return self.left.height + 1
        elif self.right:
            self.right.height = self.right.node_height()
            return self.right.height + 1
        else:
            return 0
        
def less_than(x,y):
    return x < y

class AVLTree(BinarySearchTree):
    def __init__(self, root=None, less=less_than):
        super(AVLTree, self).__init__(root, less)
        #self.height = self.tree_height()
 
    def left_rotate(self, n):
        new_root = n.right
        n.right = new_root.left
        if n.right:
            n.right.parent = n
        new_root.left = n
        new_root.parent = n.parent
        n.parent = new_root

        #y = n.right
        #n.right = y.left
        #if y.left:
        #    y.left.parent = n
        #y.parent = n.parent
        #n.parent = y
        #y.left = n   

    def right_rotate(self, n):
        new_root = n.left
        n.left = new_root.right
        if n.left:
            n.left.parent = n
        new_root.right = n
        new_root.parent = n.parent
        n.parent = new_root

        #x = n.left
        #n.left = x.right
        #if x.right:
        #    n.left.parent = n
        #x.parent = n.parent
        #n.parent = x
        #x.right = n

    #def tree_height(self):
    #    if not self.root:
    #        return -1

    #    if self.root.left and self.root.right:
    #        left = AVLTree(self.root.left)
    #        right = AVLTree(self.root.right)
    #        return 1 + max(left.height, right.height) 
    #    elif self.root.left:
    #        left = AVLTree(self.root.left)
    #        return 1 + left.height
    #    elif self.root.right:
    #        right = AVLTree(self.root.right)
    #        return 1 + right.height
    #    else:
    #        return 0

    # takes a node that may have unbalanced the tree.
    def balance(self, n):
        if n.parent is None:
            return

        if n.left:
            left_height = n.left.height
        else:
            left_height = -1
        if n.right:
            right_height = n.right.height
        else:
            right_height = -1

        if abs(left_height - right_height) > 1:
            if left_height - right_height == 1:
                self.left_rotate(n)
                n.node_height()
            if left_height - right_height == 2:
                self.left_rotate(n.left)
                if n.left:
                    n.left.node_height()
                self.right_rotate(n)
                n.node_height()
            elif right_height - left_height == 1:
                self.right_rotate(n)
                n.node_height()
            elif right_height - left_height == 2:
                self.right_rotate(n.right)
                if n.right:
                    n.right.node_height()
                self.left_rotate(n)
                n.node_height()

        self.balance(n.parent)
        
        #left = AVLTree(n.left)
        #
        #right = AVLTree(n.right)

        #if left.root and right.root and abs(left.height - right.height) > 1:
        #    left_left = AVLTree(left.root.left)
        #    left_right = AVLTree(left.root.right)
        #    right_left = AVLTree(right.root.left)
        #    right_right = AVLTree(right.root.right)
        #    if left.height < right.height:
        #        if left_left.root and left_right.root:
        #            if left_left.height > left_right.height:
        #                self.right_rotate(left.root)
        #                self.left_rotate(n)
        #            elif left_left.height < left_right.height:
        #                self.left_rotate(n)
        #            else:
        #                self.right_rotate(n)
        #    else:
        #        if right_left.root and right_right.root:
        #            if right_left.height > right_right.height:
        #                self.right_rotate(right.root)
        #                self.left_rotate(n)
        #            elif right_left.height < right_right.height:
        #                self.left_rotate(n)
        #            else:
        #                self.right_rotate(n)

        #    self.height = self.tree_height()
        #    self.balance(n.parent)

    def insert(self, k):
        if not self.root:
            self.root = AVLNode(k, parent=None)
        if self.less(k, self.root.key):
            if self.root.left:
                left = AVLTree(self.root.left)
                return left.insert(k)
            else:
                new_node = AVLNode(k, parent=self.root)
                self.root.left = new_node
                self.balance(new_node)
                return new_node
        else:
            if self.root.right:
                right = AVLTree(self.root.right)
                return right.insert(k)
            else:
                new_node = AVLNode(k, parent=self.root)
                self.root.right = new_node
                self.balance(new_node)
                return new_node

    def delete_node(self, n):
        if n.left and n.right: # y has two children
            y = self.successor(n)
        elif n.left: # y has a left child
            y = self.predecessor(n)
        elif n.right: # n has a right child
            y = self.successor(n)
        
        # inform y's parents of its departure
        if y.parent.left is y:
            y.parent.left = None
        else:
            y.parent.right = None
        
        # y takes over n's children
        y.left = n.left
        y.right = n.right

        # tell y's new children who their parent is
        if y.left:
            y.left.parent = y
        if y.right:
            y.right.parent = y

        # y has the same parent as n
        y.parent = n.parent

        # tell y's parent its child is
        if not n.parent: # n is the root
            y.right.parent = y
        elif n.parent.left is n: # n is the left child of its parent
            n.parent.left = y
        elif n.parent.right is n: # n is the right child of its parent
            n.parent.right = y
        self.balance(n.parent)
        return y


    # takes value, returns node with key value
    #def insert(self, k):
    #    new_node = BinarySearchTree.insert(self, k)
    #    avl_node = AVLNode(new_node.key, new_node.left, new_node.right, new_node.parent)
    #    self.balance(avl_node)
    #    return avl_node

    # takes node, returns node
    #def delete_node(self, n):
    #    deleted_node = BinarySearchTree.delete(self, n)
    #    avl_node = AVLNode(deleted_node.key, deleted_node.left, deleted_node.right, deleted_node.parent)
    #    self.balance(avl_node.parent)
    #    return avl_node
#########
# Tests #
#########

# Based off the AVL tree at this URL:
# http://upload.wikimedia.org/wikipedia/commons/thumb/0/06/AVLtreef.svg/251px-AVLtreef.svg.png

if __name__ == '__main__':
#     test_avl = AVLTree((AVLNode(50, AVLNode(17), AVLNode(72))))
#     test_avl.root.left.left = AVLNode(12, parent=test_avl.root.left)
#     test_avl.root.left.left.left =\
#             AVLNode(9, parent=test_avl.root.left.left)
#     test_avl.root.left.left.right = AVLNode(14, parent=test_avl.root.left.left)
#     test_avl.root.left.right = AVLNode(23, parent=test_avl.root.left)
#     test_avl.root.left.right.left = AVLNode(19, parent=test_avl.root.left.right)
#     test_avl.root.right.left = AVLNode(54, parent=test_avl.root.right)
#     test_avl.root.right.left.right =\
#             AVLNode(67, parent=test_avl.root.right.left)
#     test_avl.root.right.right = AVLNode(76, parent=test_avl.root.right)

    test_avl = AVLTree(
            AVLNode(50,
                AVLNode(17,
                    AVLNode(12,
                        AVLNode(9),
                        AVLNode(14)),
                    AVLNode(23,
                        AVLNode(19))),
                AVLNode(72,
                    AVLNode(54,
                        right=AVLNode(67)),
                    AVLNode(76))))
                    

    ## tree_height ##
    assert test_avl.root.height == 3
    assert test_avl.root.left.height == 2
    assert test_avl.root.right.height == 2
    assert test_avl.root.right.left.height == 1
    assert test_avl.root.right.right.height == 0

    ## predecessor ##
    assert test_avl.predecessor(test_avl.root) is test_avl.root.left.right
    assert test_avl.predecessor(test_avl.root.left) is test_avl.root.left.left.right
    assert test_avl.predecessor(test_avl.root.right)\
            is test_avl.root.right.left.right
    assert test_avl.predecessor(test_avl.root.right.right) is test_avl.root.right

    ## successor ##
    assert test_avl.successor(test_avl.root) is test_avl.root.right.left
    assert test_avl.successor(test_avl.root.left.left)\
            is test_avl.root.left.left.right
    assert test_avl.successor(test_avl.root.left) is test_avl.root.left.right.left
    assert test_avl.successor(test_avl.root.left.right) is test_avl.root

    ## insert ##
    test_avl.insert(74)
    assert test_avl.root.right.right.left.key == 74
    test_avl.insert(18)
    assert test_avl.root.left.key == 19 or test_avl.root.left.right.key == 19
    assert test_avl.root.left.right.left.key == 18
    assert test_avl.root.left.right.right.key == 23
