from collections import deque 

def bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            curr = queue.popleft()
            
            if i == level_size - 1:
                result.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
                
    
    return result