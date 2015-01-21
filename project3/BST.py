from stack import ArrayStack

class BSTNode(object):
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

def less_than(x,y):
    return x < y

class BinarySearchTree(object):
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.parents = True
        self.less = less

    # takes value, returns node with key value
    def insert(self, k):
        if not self.root:
            self.root = BSTNode(k, parent=None)
        if self.less(k, self.root.key):
            if self.root.left:
                left = BinarySearchTree(self.root.left)
                return left.insert(k)
            else:
                new_node = BSTNode(k, parent=self.root)
                self.root.left = new_node
                return new_node
        else:
            if self.root.right:
                right = BinarySearchTree(self.root.right)
                return right.insert(k)
            else:
                new_node = BSTNode(k, parent=self.root)
                self.root.right = new_node
                return new_node

    def tree_min(self):
        if self.root.left:
            left = BinarySearchTree(self.root.left)
            return left.tree_min()
        else:
            return self.root

    def tree_max(self):
        if self.root.right:
            right = BinarySearchTree(self.root.right)
            return right.tree_max()
        else:
            return self.root

    def greater_ancestor(self, n):
        p = n.parent

        if p and n is p.right:
            return self.greater_ancestor(p)
        else:
            return p

    def lesser_ancestor(self, n):
        p = n.parent

        if p and n is p.left:
            return self.lesser_ancestor(p)
        else:
            return p

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        if n.right:
            right = BinarySearchTree(n.right)
            return right.tree_min()
        else:
            return self.greater_ancestor(n)

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        if n.left:
            left = BinarySearchTree(n.left)
            return left.tree_max()
        else:
            return self.lesser_ancestor(n)

    # takes key returns node
    # can return None
    def search(self, k):
        if self.root.key == k:
            return self.root
            
        if self.less(k, self.root.key): # key is on the left
            if self.root.left:
                left = BinarySearchTree(self.root.left)
                return left.search(k)
            else:
                return None
        else: # right
            if self.root.right:
                right = BinarySearchTree(self.root.right)
                return right.search(k)
            else:
                return None

    # takes node, returns node
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

        return y

    def inorder_walk(self, walk_list=[]):
        if self.root.left:
            left = BinarySearchTree(self.root.left)
            left.inorder_walk()
        print(self.root.key)
        if self.root.right:
            right = BinarySearchTree(self.root.right)
            right.inorder_walk()
        


#########
# Tests #
#########

# Based off the tree at this URL:
# http://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/200px-Binary_search_tree.svg.png

if __name__ == '__main__':
    print(u'Doing some tests...')
    print(u'Making a tree...')
    print(u'See http://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/200px-Binary_search_tree.svg.png')
    
    test_bst = BinarySearchTree(
            BSTNode(8,
                BSTNode(3,
                    BSTNode(1),
                    BSTNode(6,
                        BSTNode(4),
                        BSTNode(7))),
                BSTNode(10,
                    right=BSTNode(14,
                        BSTNode(13)))))

    print(u'Testing tree_min...')
    ## tree_min ##
    assert test_bst.tree_min() is test_bst.root.left.left

    print(u'Testing tree_max.')
    ## tree_max ##
    assert test_bst.tree_max() is test_bst.root.right.right

    print(u'Testing successor...')
    ## successor ##
    assert test_bst.successor(test_bst.root) is test_bst.root.right
    assert test_bst.successor(test_bst.root.right)\
            is test_bst.root.right.right.left
    assert test_bst.successor(test_bst.root.left)\
            is test_bst.root.left.right.left
    assert test_bst.successor(test_bst.root.left.left)\
            is test_bst.root.left
    assert test_bst.successor(test_bst.root.left.right.right)\
            is test_bst.root

    print(u'Testing predecessor...')
    ## predecessor ##
    assert test_bst.predecessor(test_bst.root.left.right)\
            is test_bst.root.left.right.left
    assert test_bst.predecessor(test_bst.root.left.right)\
            is test_bst.root.left.right.left
    assert test_bst.predecessor(test_bst.root.right)\
            is test_bst.root
    assert test_bst.predecessor(test_bst.root.left)\
            is test_bst.root.left.left
    assert test_bst.predecessor(test_bst.root.left.right.left)\
            is test_bst.root.left

    print(u'Testing search...')
    ## search ##
    assert test_bst.search(8) is test_bst.root
    assert test_bst.search(3) is test_bst.root.left
    assert test_bst.search(13) is test_bst.root.right.right.left

    print('Testing delete...')
    ## delete ##
    ### the tree with root.left removed ###
    test_bst.delete_node(test_bst.root.left)
    assert test_bst.root.left.key == 4 # where 3 used to be
    assert test_bst.root.left.left.key == 1
    assert test_bst.root.left.right.key == 6
    assert test_bst.root.left.right.left is None # where 4 used to be
    assert test_bst.root.left.right.right.key == 7

    ### the tree with root.right.right removed in addition to root.left ###
    test_bst.delete_node(test_bst.root.right.right)
    assert test_bst.root.right.right.key == 13 # where 14 was
    assert test_bst.root.right.right.left is None # where 13 was

    print(u'Testing insert...')
    ## insert ##
    ### let's put the nodes back that we took out ###
    test_bst.insert(3)
    test_bst.insert(14)
    assert test_bst.root.left.left.right.key == 3
    assert test_bst.root.right.right.right.key == 14

    print(u'Passed all tests.')
