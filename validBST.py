""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# node = node, p = parent-node, lb = lowerBound, ub = upperBound, childT = left or right chile
import sys
def f(node, p, lb, ub, childT):
    flag = None
    # termination case for recursion
    if node == None:
        return True
    # For a left child , lowerbound is same as parent's lower bound lb, upper bound = parent's value. 
    # For example, a node 5 with parent 10 will have an upperbound 10 so that no child of 5 can 
    # have a value greater than 10
    if childT == "l":
        lb = lb
        ub = p.data
        # lchild condition plus bounds check to make the node valid
        if node.data < p.data and node.data > lb and node.data < ub:
            flag = True
        else:
            flag = False        
    if childT == "r":
        lb = p.data
        ub = ub
        if node.data > p.data and node.data > lb and node.data < ub:
            flag = True
        else:
            flag = False  
    # return flag set for validity of current node and find the validity of the left and right subtree
    return flag and f(node.left,node,lb,ub,"l") and f(node.right,node,lb,ub,"r")

def checkBST(root):
    lTree = f(root.left,root,-sys.maxsize, root.data,"l" )
    rTree = f(root.right,root,root.data,sys.maxsize,"r" )
    return lTree and rTree