from collections import deque

def bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        curr = queue.popleft()
        result.append(curr.val)
        
        if curr.left:
            queue.append(curr.left)
        
        if curr.right:
            queue.append(curr.right)
            
    return result