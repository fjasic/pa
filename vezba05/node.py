
class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self,  d = None, l = None, r = None):
        """
        Node constructor 
        @param A node data object
        """
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2