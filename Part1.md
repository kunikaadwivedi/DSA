# Part 1: Core DSA Patterns & Templates (Theory & Implementation)

This file contains the definitive Python 3 templates for the core algorithmic patterns outlined in your FAANG AI Engineering roadmap. These templates are optimized for Python standard library usage (e.g., `collections`, `heapq`, `bisect`), readability, and performance.

---

## P1: Graphs, Grids & Computational DAGs

### 1.1 Multi-Source BFS
**Theory:** Used when you need to find the shortest distance from *multiple* starting points simultaneously. Instead of running BFS from each source (which is $O(V \times (V+E))$), you initialize the queue with all sources at distance 0.
**Complexity:** Time $O(V + E)$, Space $O(V)$.
```python
from collections import deque

def multi_source_bfs(grid, sources):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    visited = set()
    
    # 1. Enqueue all starting sources
    for r, c in sources:
        q.append((r, c, 0)) # (row, col, distance)
        visited.add((r, c))
        
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # 2. Run BFS
    while q:
        r, c, dist = q.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, dist + 1))
                # Update grid or result distance here
```

### 1.2 0-1 BFS
**Theory:** Used for shortest path on graphs where edge weights are strictly `0` or `1`. It runs in linear time using a double-ended queue. `0`-weight edges are pushed to the front, `1`-weight edges to the back.
**Complexity:** Time $O(V + E)$, Space $O(V)$.
```python
from collections import deque

def zero_one_bfs(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    q = deque([start])
    
    while q:
        u = q.popleft()
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                if weight == 0:
                    q.appendleft(v)  # Prioritize 0-cost transitions
                else:
                    q.append(v)      # Standard 1-cost transitions
    return dist
```

### 1.3 Dijkstra’s Algorithm
**Theory:** Finds the shortest path in a graph with non-negative edge weights.
**Complexity:** Time $O((V + E) \log V)$, Space $O(V)$.
```python
import heapq

def dijkstra(graph, start, n):
    dist = {i: float('inf') for i in range(n)}
    dist[start] = 0
    pq = [(0, start)] # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Pruning: Skip if we already found a better path to 'u'
        if d > dist[u]:
            continue
            
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist
```

### 1.4 Topological Sort (Kahn’s Algorithm)
**Theory:** Orders a Directed Acyclic Graph (DAG) such that for every directed edge $U \to V$, $U$ comes before $V$. Crucial for resolving dependencies (e.g., neural network autograd execution order).
**Complexity:** Time $O(V + E)$, Space $O(V)$.
```python
from collections import deque

def kahn_topo_sort(n, edges):
    adj = {i: [] for i in range(n)}
    indegree = [0] * n
    
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
        
    q = deque([i for i in range(n) if indegree[i] == 0])
    topo = []
    
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
                
    # If topo doesn't contain all nodes, there is a cycle
    return topo if len(topo) == n else [] 
```

### 1.5 Disjoint Set Union (DSU / Union-Find)
**Theory:** Tracks a set of elements partitioned into a number of disjoint subsets. Extremely efficient for checking graph connectivity or Kruskal's MST. Uses **Path Compression** and **Union by Rank**.
**Complexity:** Time $O(\alpha(N))$ nearly $O(1)$ per operation, Space $O(N)$.
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]
        
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
            
        # Union by rank
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
```

---

## P2: Trees, LCA & Trie

### 2.1 Lowest Common Ancestor (LCA)
**Theory:** Finds the lowest node in a tree that has both $p$ and $q$ as descendants.
**Complexity:** Time $O(N)$, Space $O(H)$.
```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
        
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root # p and q are in different subtrees
        
    return left if left else right
```

### 2.2 Tree DP (Diameter / Path Sum)
**Theory:** A pattern where recursive calls return a single "branch" value to the parent, while updating a global maximum (e.g., diameter, maximum path sum) that considers both branches at the current node.
**Complexity:** Time $O(N)$, Space $O(H)$.
```python
def diameterOfBinaryTree(root):
    max_diameter = 0
    
    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
            
        left_path = dfs(node.left)
        right_path = dfs(node.right)
        
        # Update global maximum considering the current node as the peak
        max_diameter = max(max_diameter, left_path + right_path)
        
        # Return the longest single branch down to the parent
        return 1 + max(left_path, right_path)
        
    dfs(root)
    return max_diameter
```

### 2.4 Prefix Tree (Trie)
**Theory:** A tree data structure used to efficiently store and retrieve keys in a dataset of strings. Core underlying structure for Tokenizers (BPE) and autocomplete systems.
**Complexity:** Time $O(L)$ where $L$ is word length, Space $O(N \times L)$.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
```

---

## P3: Binary Search & Feasibility Space

### 3.1 Standard & Feasibility Binary Search
**Theory:** Binary search can be used not just for exact matches, but to find the optimal point in a monotonic boolean function `[False, False, True, True]`.
```python
def binary_search_feasibility(low, high):
    def condition(mid):
        # Return True if 'mid' satisfies the feasibility check
        pass

    left, right = low, high
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if condition(mid):
            ans = mid
            right = mid - 1 # or left = mid + 1 depending on minimize/maximize
        else:
            left = mid + 1 # or right = mid - 1
    return ans
```

### 3.2 Using `bisect` Module
**Theory:** Built-in Python library for binary search.
- `bisect_left(arr, x)`: Returns the first index where `arr[i] >= x`.
- `bisect_right(arr, x)`: Returns the first index where `arr[i] > x`.
```python
import bisect

arr = [1, 2, 4, 4, 4, 6]
left_idx = bisect.bisect_left(arr, 4)   # Returns 2
right_idx = bisect.bisect_right(arr, 4) # Returns 5
```

---

## P4: Dynamic Programming & Sequence Alignments

### 4.1 0/1 Knapsack (1D Space Optimized)
**Theory:** Iterate items, then iterate capacities *backwards* to prevent reusing the same item.
```python
def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        w, v = weights[i], values[i]
        for c in range(capacity, w - 1, -1): # Backwards!
            dp[c] = max(dp[c], dp[c - w] + v)
            
    return dp[capacity]
```

### 4.2 LIS in $O(N \log N)$
**Theory:** Uses `bisect_left` to maintain a monotonic array representing the smallest tail of all increasing subsequences of length $i+1$.
```python
import bisect

def lengthOfLIS(nums):
    sub = []
    for x in nums:
        idx = bisect.bisect_left(sub, x)
        if idx == len(sub):
            sub.append(x)
        else:
            sub[idx] = x # Overwrite to keep sequence elements small
    return len(sub)
```

### 4.3 Edit Distance (Needleman-Wunsch / Levenshtein)
**Theory:** $O(M \times N)$ alignment distance. Foundational for NLP metrics (WER).
```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Deletion
                                   dp[i][j-1],    # Insertion
                                   dp[i-1][j-1])  # Replacement
    return dp[m][n]
```

---

## P5: Monotonic Stack & Monotonic Deque

### 5.1 Next Greater Element (Monotonic Stack)
**Theory:** Maintain a decreasing stack. When a larger element arrives, pop smaller elements—their "Next Greater" is the current element. Time $O(N)$.
```python
def nextGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = [] # stores indices
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
        
    return res
```

### 5.3 Sliding Window Maximum (Monotonic Deque)
**Theory:** Maintains a strictly decreasing double-ended queue of indices. The maximum of the window is always at `deque[0]`. Time $O(N)$.
```python
from collections import deque

def maxSlidingWindow(nums, k):
    res = []
    q = deque()
    
    for i in range(len(nums)):
        # 1. Remove elements out of window bounds
        if q and q[0] < i - k + 1:
            q.popleft()
            
        # 2. Maintain monotonic strictly decreasing property
        while q and nums[q[-1]] < nums[i]:
            q.pop()
            
        q.append(i)
        
        # 3. Extract max when window is fully formed
        if i >= k - 1:
            res.append(nums[q[0]])
            
    return res
```

---

## P6: Prefix Sum, Two Pointers & Sliding Window

### 6.1 Dynamic Sliding Window
**Theory:** Expand window by advancing `right`. If a constraint is broken, shrink by advancing `left` until the constraint is satisfied.
```python
def longest_substring_k_distinct(s, k):
    left = 0
    max_len = 0
    counts = {}
    
    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

### 6.4 1D Prefix Sum + Hash Map Complement ($O(N)$)
**Theory:** Find if there exists a subarray with sum $K$. We track prefix sums. If `current_sum - K` exists in our seen prefixes, we found a subarray!
```python
def subarraySum(nums, k):
    prefix_counts = {0: 1} # base case: sum of 0 occurs 1 time
    cur_sum = 0
    res = 0
    
    for x in nums:
        cur_sum += x
        # If cur_sum - k exists, it means we can chop off a prefix to reach k
        res += prefix_counts.get(cur_sum - k, 0)
        prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1
        
    return res
```

### 6.6 Difference Array ($O(1)$ Range Updates)
**Theory:** Instead of adding $V$ to all elements in `[L, R]`, add $V$ to `diff[L]` and subtract $V$ from `diff[R+1]`. Accumulate at the end to get the actual array.
```python
def range_updates(n, updates):
    diff = [0] * (n + 1)
    for start, end, val in updates:
        diff[start] += val
        diff[end + 1] -= val
        
    res = []
    cur = 0
    for i in range(n):
        cur += diff[i]
        res.append(cur)
    return res
```

---

## P7: Intervals & Sweep Line

### 7.1 Merge Intervals
**Theory:** Sort by start time. Iteratively merge overlapping intervals. Time $O(N \log N)$.
```python
def mergeIntervals(intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end: # Overlap
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
            
    return merged
```

### 7.2 Sweep Line (Meeting Rooms II / Resource Peaks)
**Theory:** Separate starts and ends into independent events. Sort them. Increment on start, decrement on end. Track the peak. Time $O(N \log N)$.
```python
def minMeetingRooms(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # 1 signifies a room is taken
        events.append((end, -1))    # -1 signifies a room is freed
        
    # Sort by time. If times tie, process end (-1) before start (+1)
    events.sort(key=lambda x: (x[0], x[1]))
    
    max_rooms = 0
    curr_rooms = 0
    for time, delta in events:
        curr_rooms += delta
        max_rooms = max(max_rooms, curr_rooms)
        
    return max_rooms
```

---

## P8: Heaps, Top-K & QuickSelect

### 8.1 Top-K Frequent Elements (Min-Heap)
**Theory:** Keep a heap of size $K$. Pushing and popping takes $O(\log K)$, leading to $O(N \log K)$ overall.
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    heap = []
    
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap) # Pop the smallest frequency
            
    return [num for freq, num in heap]
```

### 8.3 Median from Data Stream
**Theory:** Maintain two heaps. `small` (max-heap) for the lower half of numbers, `large` (min-heap) for the upper half.
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # Max-heap (invert values)
        self.large = [] # Min-heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        # Ensure max of small <= min of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

---

## P9: Backtracking & State-Space Pruning

### 9.1 Subsets with Duplicate Pruning
**Theory:** Sorting is required. To avoid duplicate subsets, skip elements that are identical to the previous one at the *current recursive level*. Time $O(2^N)$.
```python
def subsetsWithDup(nums):
    res = []
    nums.sort()
    
    def backtrack(idx, path):
        res.append(path[:])
        
        for i in range(idx, len(nums)):
            # Prune duplicate branches at this depth
            if i > idx and nums[i] == nums[i - 1]:
                continue
                
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
    backtrack(0, [])
    return res
```

### 9.3 Grid Backtracking (Word Search)
**Theory:** DFS with in-place grid mutation to save $O(N \times M)$ space on visited sets.
```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, i):
        if i == len(word): return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
            
        temp = board[r][c]
        board[r][c] = '#' # Mark as visited
        
        res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or 
               dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
               
        board[r][c] = temp # Backtrack
        return res
        
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
    return False
```

---

## P10: Bit Manipulation & Math Foundations

### 10.1 Essential Bitwise Kernels
- **Clear lowest set bit:** `x & (x - 1)` (Extremely useful for Brian Kernighan’s algorithm to count set bits).
- **Extract lowest set bit:** `x & -x`.
- **Check if power of two:** `(x & (x - 1)) == 0 and x > 0`.

### 10.2 Single Number (XOR)
**Theory:** All elements appear twice except one. XORing identical numbers cancels them out ($A \oplus A = 0$).
```python
def singleNumber(nums):
    res = 0
    for x in nums:
        res ^= x
    return res
```

### 10.3 Bitmask DP (Subset/TSP Structure)
**Theory:** Use integers as bitmasks to represent subsets. Time $O(N \times 2^N)$.
```python
def tsp(n, dist):
    # memo[mask][u] -> min cost to visit remaining unvisited nodes starting from u
    memo = {}
    
    def dp(mask, u):
        if mask == (1 << n) - 1: # All nodes visited
            return 0
        if (mask, u) in memo:
            return memo[(mask, u)]
            
        ans = float('inf')
        for v in range(n):
            if not (mask & (1 << v)): # v is not visited
                ans = min(ans, dist[u][v] + dp(mask | (1 << v), v))
                
        memo[(mask, u)] = ans
        return ans
        
    return dp(1, 0) # start from node 0 (mask = 1)
```
