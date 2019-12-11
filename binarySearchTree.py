
#example of a binary search tree
def search(root,key):
    
    if root is None or root.val == key: #start at root. if root is the same as search key or tree is empty, return root
        return root
    
    if root.val < key: #move right
        
        return search(root.right,key)
    
    return search(root.left,key) #move left

