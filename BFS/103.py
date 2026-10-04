from collections import deque
def bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        nodes_for_level =deque()
        
        for i in range(level_size):
            curr = queue.popleft()
            
            if left_to_right:
                nodes_for_level.append(curr.val)
            else:
                nodes_for_level.appendleft(curr.val)
                
            if curr.left:
                queue.append(curr.left) 
            if curr.right:
                queue.append(curr.right)
                
        result.append(list(nodes_for_level))
        left_to_right = not left_to_right
    
    return result
    