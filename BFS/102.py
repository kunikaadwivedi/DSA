from collections import deque

def bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            curr = queue.popleft()
            current_level.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
                
        result.append(current_level)
    
    return result