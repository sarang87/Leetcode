# [3,5,1,6,2,0,8,null,null,7,4]
# 4
# 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

# finds the path from a node all the way to the root. Paths returned in a reverse order from node to root
def helper(self, node, val, path):
    if node == None:
        return []
    if node.val == val:
        path.append(node)
        return path
    p1 = self.helper(node.left, val, path)       
    p2 = self.helper(node.right, val, path)
    if len(p1) > 0:
        p1.append(node)
        return p1
    elif len(p2) > 0:
        p2.append(node)
        return p2
    else:
        return []
      

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    pp = self.helper(root, p.val, [])
    qq = self.helper(root, q.val, [])
    od = collections.OrderedDict()
    # add all node val as key and node as value to an ordered dict
    for i in pp:
        od[i.val] = i 
    # loop over the other paths and look in the hash map. If a match occus it is the common ancestor      
    for j in qq:
        if j.val in od:
            return od[j.val]
