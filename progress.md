# 🎯 FAANG AI Engineering & DSA Master Roadmap & Progress Tracker

> **Candidate Profile:** AI Engineer / Applied AI Engineer / Generative AI SWE / ML Systems Engineer  
> **Target Companies:** Meta (E4/E5 AI), Google (L4/L5 SWE-AI/ML), Apple (ICT4/ICT5 AIML), Amazon (L5/L6 Applied AI / SDE), Microsoft (L61–L63 AI), OpenAI / Anthropic (MTS)  
> **Primary Language:** Python 3 (Vectorized NumPy, PyTorch, Standard Library)  
> **Tracker Version:** 2026 FAANG Hiring Bar Benchmark  

---

## 📊 FAANG AI Engineering Interview Loop Matrix

| Round Type | Format & Duration | Focus Areas | Weight in Loop |
| :--- | :--- | :--- | :--- |
| **Round 1: Python DSA & Algorithms** | 45–60 min live coding | Graph/DAG traversals, Trees/LCA, Monotonic Structures, Heaps, Sliding Windows, Intervals, DP | 25% |
| **Round 2: AI/ML Coding From Scratch** | 45–60 min live coding | Pure Python/NumPy/PyTorch implementation of Attention, KV-Cache, BPE, Sampling, Autograd, Normalization | 25% |
| **Round 3: GenAI, RAG & LLM Systems** | 45–60 min technical deep dive | Advanced RAG, Hybrid Retrieval, HNSW, ReAct Agents, Serving, KV memory math, LoRA, Quantization | 20% |
| **Round 4: Large-Scale AI / ML System Design (MLSD)** | 45–60 min architecture | End-to-end Copilot, Enterprise RAG, 1B-vector search, Multi-tenant LLM gateway, RecSys | 20% |
| **Round 5: Behavioral & Engineering Leadership** | 45 min behavioral | Conflict resolution, technical tradeoffs, production failures, AI safety/ethics (Google Googlyness / Amazon LP) | 10% |

---

## Part 1: Core DSA Patterns & Templates (Python-Optimized)

### P1: Graphs, Grids & Computational DAGs
- [ ] **1.1 Multi-Source BFS (Grids / Unweighted Graphs)** `MUST DO (Google/Meta Core)`
  - *Context:* Matrix diffusion, distance transforms, wave propagation.
  - *Template:* Initialize `deque` with all initial sources at step 0; track visited set or in-place marker.
- [ ] **1.2 0-1 BFS with Deque** `MUST DO`
  - *Context:* Graphs with binary edge weights $w \in \{0, 1\}$.
  - *Template:* `deque.appendleft()` for 0-weight transition, `deque.append()` for 1-weight transition. Runs in $O(V + E)$ vs Dijkstra $O(E \log V)$.
- [ ] **1.3 Dijkstra’s Algorithm (Weighted Shortest Path)** `MUST DO`
  - *Context:* Non-negative weights, routing latency, shortest token paths.
  - *Template:* `heapq` with `(dist, node)`, eager distance pruning (`if d > dist[u]: continue`).
- [ ] **1.4 Topological Sort & Cycle Detection (Kahn’s Algorithm vs DFS)** `CRITICAL (ML Computational Graphs)`
  - *Context:* PyTorch Autograd computation graph execution order, task dependency resolution.
  - *Template:* Indegree array + queue (Kahn's), or 3-state DFS coloring (0: unvisited, 1: visiting, 2: visited).
- [ ] **1.5 Disjoint Set Union (DSU / Union-Find with Path Compression & Rank)** `MUST DO`
  - *Context:* Graph connectivity, Kruskal's MST, clustering entities.
  - *Complexity:* $\alpha(N)$ inverse Ackermann per query.
- [ ] **1.6 Bipartite Graph Verification (2-Coloring)**
  - *Context:* Graph bipartite matching, two-tower user-item graph validation.

---

### P2: Trees, LCA & Hierarchical Structures
- [ ] **2.1 Lowest Common Ancestor (LCA) in Binary Tree & BST** `MUST DO (Meta Favorite)`
  - *Context:* Hierarchical syntax trees, AST code embeddings, ontology traversal.
  - *Template:* Post-order traversal bubbling up found nodes; binary lifting for $O(\log N)$ online queries.
- [ ] **2.2 Tree DP: Path Sum & Diameter Pattern** `MUST DO`
  - *Context:* Maximum path between any two nodes, tree diameter.
  - *Template:* Return single-branch max to parent while updating global diameter at current root.
- [ ] **2.3 Binary Tree Serialization & Deserialization** `MUST DO`
  - *Context:* Model AST checkpoints, graph serialization format.
  - *Template:* Pre-order traversal with `#` null delimiters or BFS level-order token stream.
- [ ] **2.4 Prefix Tree (Trie) & Compressed Trie (Radix)** `CRITICAL (Tokenizers & Autocomplete)`
  - *Context:* BPE token lookup, dictionary matching, prefix decoding.
  - *Template:* Dict of dicts: `trie[char]`, with terminal boolean marker `is_end`.

---

### P3: Binary Search & Feasibility Space
- [ ] **3.1 The Universal Binary Search Templates (Exact Match vs Condition Minimization)**
  - *Template:* `left, right = low, high; while left < right: mid = (left + right) // 2; if condition(mid): right = mid else: left = mid + 1`
- [ ] **3.2 Lower Bound & Upper Bound (`bisect_left` vs `bisect_right`)**
  - *Context:* Exact index slicing, threshold searches in embedding index thresholds.
- [ ] **3.3 Search in Rotated Sorted Array** `MUST DO (Amazon/Google Core)`
  - *Context:* Boundary identification, pivot handling.
- [ ] **3.4 Binary Search on Monotonic Feasibility Space (Minimize Max / Maximize Min)** `HIGH FREQUENCY`
  - *Context:* Capacity allocation, throughput throttling, token budget distribution.

---

### P4: Dynamic Programming & Sequence Alignments
- [ ] **4.1 0/1 Knapsack & Unbounded Knapsack Patterns**
  - *Context:* Memory budget optimization, GPU VRAM token allocation.
  - *Template:* 1D reversed loop for 0/1; forward loop for unbounded.
- [ ] **4.2 Longest Increasing Subsequence (LIS) in $O(N \log N)$** `MUST DO`
  - *Context:* Patience sorting with `bisect_left`.
- [ ] **4.3 Edit Distance & Sequence Alignment (Needleman-Wunsch / Levenshtein)** `CRITICAL (LLM Text Evaluation)`
  - *Context:* Token edit distance, Word Error Rate (WER), diff generation in code agents.
- [ ] **4.4 State Machine DP (Stock Trading with Cooldown / Transaction Fees)**
  - *Context:* Multi-state transitions, autoregressive finite state token constraints.

---

### P5: Monotonic Stack & Monotonic Deque
- [ ] **5.1 Next Greater / Smaller Element (Universal Monotonic Stack)** `MUST DO`
  - *Context:* Temperature lookahead, attention span horizon checks.
  - *Template:* Decreasing stack of indices; resolve elements upon violation.
- [ ] **5.2 Largest Rectangle in Histogram & Maximal Rectangle** `MUST DO (Google Core)`
  - *Context:* $O(N)$ area calculation with dummy sentinels.
- [ ] **5.3 Monotonic Sliding Window Maximum/Minimum (Sliding Deque)** `CRITICAL (Streaming & Buffers)`
  - *Context:* Real-time token streaming rate-limiting, local context pooling.
  - *Template:* `deque` maintaining monotonically decreasing order of values.

---

### P6: Prefix Sum, Two Pointers & Sliding Window
- [ ] **6.1 Dynamic Sliding Window (Expand Right, Shrink Left)** `MUST DO`
  - *Context:* Substring matching, token windowing with capacity limits.
- [ ] **6.2 The "Exact $K$" Subarray Trick (`atMost(K) - atMost(K - 1)`)** `HIGH YIELD`
- [ ] **6.3 3-Sum & $K$-Sum with Duplicate Pruning** `MUST DO (FAANG Standard)`
  - *Context:* Sorting + 2-pointer convergence + `while left < right and nums[left] == nums[left+1]` skip.
- [ ] **6.4 1D Prefix Sum + Hash Map Complement ($O(N)$ Subarray Sum Equals $K$)** `MUST DO`
  - *Context:* `count += prefix_counts[current_sum - k]`.
- [ ] **6.5 2D Prefix Sum Formula (Integral Image / Matrix Range Query in $O(1)$)**
  - *Context:* 2D feature map pooling, image patch sum extraction.
- [ ] **6.6 Difference Array (1D & 2D Range Updates in $O(1)$)** `MUST DO (Google Core)`
  - *Context:* Flight bookings, continuous intervals load tracking, offline timestamp delta accumulation.

---

### P7: Intervals & Sweep Line
- [ ] **7.1 Merge Intervals & Insert Interval** `MUST DO (FAANG Baseline)`
  - *Context:* Slicing audio/video segments, token span merging in RAG chunks.
- [ ] **7.2 Meeting Rooms II / Sweep Line Algorithm** `MUST DO (Google/Meta Priority)`
  - *Context:* Peak GPU server concurrent usage, scheduled training job overlap.
  - *Template:* Coordinate compression / event sorting with `(time, +1)` start and `(time, -1)` end.

---

### P8: Heaps, Top-K & QuickSelect
- [ ] **8.1 Top-K Frequent Elements & K-Way Merge** `CRITICAL (FAANG Live Coding)`
  - *Context:* Top-k logits selection, beam search candidate pruning, multi-node log merging.
  - *Template:* Min-heap of size $K$ for top-k elements ($O(N \log K)$).
- [ ] **8.2 QuickSelect ($O(N)$ Average, $O(1)$ Extra Space)** `MUST DO`
  - *Context:* In-place median finding, threshold partitioning without full sorting.
- [ ] **8.3 Median from Data Stream (Two Heaps: Max-Heap + Min-Heap)** `MUST DO`
  - *Context:* Streaming percentile monitoring in model inference servers.

---

### P9: Backtracking & State-Space Pruning
- [ ] **9.1 Subsets & Combinations with Duplicate Pruning**
  - *Template:* Sort first; skip `if i > start and nums[i] == nums[i-1]: continue`.
- [ ] **9.2 Permutations with Frequency Maps / Visited Masks**
- [ ] **9.3 In-Place Grid Backtracking & Word Search with Trie** `HIGH YIELD`
  - *Context:* Substring generation, vocabulary validation, game state trees.

---

### P10: Bit Manipulation & Numerical Foundations
- [ ] **10.1 Bitwise Kernels ($x \& (x - 1)$ to clear LSB, $x \& (-x)$ to extract LSB)**
- [ ] **10.2 Single Number I, II, III (Bit Counter modulo $K$)**
- [ ] **10.3 Bitmask Dynamic Programming**
  - *Context:* Traveling Salesperson, subset assignment, TSP-like token routing.

---

## Part 2: LeetCode DSA Question Bank (FAANG High-Yield in Python)

### 1. Arrays & Hashing
- [ ] `Q1.1` [LC 1] Two Sum — `EASY` `MUST DO`
- [ ] `Q1.2` [LC 49] Group Anagrams — `MEDIUM` `MUST DO`
- [ ] `Q1.3` [LC 347] Top K Frequent Elements — `MEDIUM` `MUST DO`
- [ ] `Q1.4` [LC 238] Product of Array Except Self — `MEDIUM` `MUST DO (FAANG Core)`
- [ ] `Q1.5` [LC 36] Valid Sudoku — `MEDIUM`
- [ ] `Q1.6` [LC 128] Longest Consecutive Sequence — `MEDIUM` `MUST DO`
- [ ] `Q1.7` [LC 271] Encode and Decode Strings — `MEDIUM` `MUST DO (Data Serialization)`

### 2. Two Pointers
- [ ] `Q2.1` [LC 167] Two Sum II - Input Array Is Sorted — `MEDIUM`
- [ ] `Q2.2` [LC 15] 3Sum — `MEDIUM` `MUST DO (Meta Core)`
- [ ] `Q2.3` [LC 11] Container With Most Water — `MEDIUM` `MUST DO`
- [ ] `Q2.4` [LC 42] Trapping Rain Water — `HARD` `MUST DO (Google Favorite)`

### 3. Prefix Sum & Difference Arrays
- [ ] `Q3.1` [LC 560] Subarray Sum Equals K — `MEDIUM` `MUST DO (Meta/Google Top)`
- [ ] `Q3.2` [LC 525] Contiguous Array (Equal 0s and 1s) — `MEDIUM`
- [ ] `Q3.3` [LC 523] Continuous Subarray Sum (Modulo Math) — `MEDIUM`
- [ ] `Q3.4` [LC 974] Subarray Sums Divisible by K — `MEDIUM`
- [ ] `Q3.5` [LC 304] Range Sum Query 2D - Immutable — `MEDIUM`
- [ ] `Q3.6` [LC 1109 / LC 370] Corporate Flight Bookings / Range Addition — `MEDIUM` `MUST DO`
- [ ] `Q3.7` [LC 862] Shortest Subarray with Sum at Least K — `HARD` `TRENDING IN FAANG`

### 4. Sliding Window
- [ ] `Q4.1` [LC 121] Best Time to Buy and Sell Stock — `EASY`
- [ ] `Q4.2` [LC 3] Longest Substring Without Repeating Characters — `MEDIUM` `MUST DO`
- [ ] `Q4.3` [LC 424] Longest Repeating Character Replacement — `MEDIUM`
- [ ] `Q4.4` [LC 567] Permutation in String — `MEDIUM`
- [ ] `Q4.5` [LC 76] Minimum Window Substring — `HARD` `MUST DO (Meta/Google Top)`
- [ ] `Q4.6` [LC 992] Subarrays with K Different Integers — `HARD`

### 5. Stack & Monotonic Stack
- [ ] `Q5.1` [LC 155] Min Stack — `MEDIUM` `MUST DO`
- [ ] `Q5.2` [LC 150] Evaluate Reverse Polish Notation — `MEDIUM`
- [ ] `Q5.3` [LC 22] Generate Parentheses — `MEDIUM`
- [ ] `Q5.4` [LC 739] Daily Temperatures — `MEDIUM` `MUST DO`
- [ ] `Q5.5` [LC 853] Car Fleet — `MEDIUM`
- [ ] `Q5.6` [LC 84] Largest Rectangle in Histogram — `HARD` `MUST DO (Google Core)`

### 6. Binary Search
- [ ] `Q6.1` [LC 74] Search a 2D Matrix — `MEDIUM`
- [ ] `Q6.2` [LC 153] Find Minimum in Rotated Sorted Array — `MEDIUM` `MUST DO`
- [ ] `Q6.3` [LC 33] Search in Rotated Sorted Array — `MEDIUM` `MUST DO`
- [ ] `Q6.4` [LC 981] Time Based Key-Value Store — `MEDIUM` `MUST DO (Systems & AI Caching)`
- [ ] `Q6.5` [LC 875] Koko Eating Bananas — `MEDIUM` `MUST DO`
- [ ] `Q6.6` [LC 4] Median of Two Sorted Arrays — `HARD` `GOOGLE TOP`

### 7. Linked Lists & Memory Buffers
- [ ] `Q7.1` [LC 143] Reorder List — `MEDIUM`
- [ ] `Q7.2` [LC 19] Remove Nth Node From End of List — `MEDIUM`
- [ ] `Q7.3` [LC 138] Copy List with Random Pointer — `MEDIUM` `MUST DO (Deep Copy / Graph Clone)`
- [ ] `Q7.4` [LC 2] Add Two Numbers — `MEDIUM`
- [ ] `Q7.5` [LC 287] Find the Duplicate Number (Floyd's Tortoise and Hare) — `MEDIUM`
- [ ] `Q7.6` [LC 146] LRU Cache — `MEDIUM` `MUST DO (FAANG #1 Most Asked)`
- [ ] `Q7.7` [LC 460] LFU Cache — `HARD` `AI KV-CACHE FAVORITE`
- [ ] `Q7.8` [LC 23] Merge k Sorted Lists — `HARD` `MUST DO`

### 8. Trees & Binary Search Trees
- [ ] `Q8.1` [LC 543] Diameter of Binary Tree — `EASY`
- [ ] `Q8.2` [LC 235] Lowest Common Ancestor of a BST — `MEDIUM`
- [ ] `Q8.3` [LC 236] Lowest Common Ancestor of a Binary Tree — `MEDIUM` `MUST DO (Meta Core)`
- [ ] `Q8.4` [LC 102] Binary Tree Level Order Traversal — `MEDIUM`
- [ ] `Q8.5` [LC 199] Binary Tree Right Side View — `MEDIUM`
- [ ] `Q8.6` [LC 1448] Count Good Nodes in Binary Tree — `MEDIUM`
- [ ] `Q8.7` [LC 98] Validate Binary Search Tree — `MEDIUM` `MUST DO`
- [ ] `Q8.8` [LC 230] Kth Smallest Element in a BST — `MEDIUM`
- [ ] `Q8.9` [LC 105] Construct Binary Tree from Preorder and Inorder Traversal — `MEDIUM`
- [ ] `Q8.10` [LC 124] Binary Tree Maximum Path Sum — `HARD` `MUST DO`
- [ ] `Q8.11` [LC 2096] Step-by-Step Directions From a Binary Tree Node to Another — `MEDIUM` `TRENDING IN POOL`

### 9. Tries
- [ ] `Q9.1` [LC 208] Implement Trie (Prefix Tree) — `MEDIUM` `MUST DO (Tokenizer Foundational)`
- [ ] `Q9.2` [LC 211] Design Add and Search Words Data Structure — `MEDIUM`
- [ ] `Q9.3` [LC 212] Word Search II (Trie + 2D Backtracking) — `HARD` `MUST DO`
- [ ] `Q9.4` [LC 642] Design Search Autocomplete System — `HARD` `AI/SEARCH CORE`

### 10. Graphs
- [ ] `Q10.1` [LC 200] Number of Islands — `MEDIUM` `MUST DO`
- [ ] `Q10.2` [LC 695] Max Area of Island — `MEDIUM`
- [ ] `Q10.3` [LC 133] Clone Graph — `MEDIUM` `MUST DO`
- [ ] `Q10.4` [LC 994] Rotting Oranges (Multi-source BFS) — `MEDIUM` `MUST DO`
- [ ] `Q10.5` [LC 417] Pacific Atlantic Water Flow — `MEDIUM`
- [ ] `Q10.6` [LC 130] Surrounded Regions — `MEDIUM`
- [ ] `Q10.7` [LC 207] Course Schedule (Cycle Detection / Topological Sort) — `MEDIUM` `MUST DO`
- [ ] `Q10.8` [LC 210] Course Schedule II (Topological Sort Order) — `MEDIUM` `MUST DO`
- [ ] `Q10.9` [LC 684] Redundant Connection (DSU) — `MEDIUM`
- [ ] `Q10.10` [LC 323] Number of Connected Components in an Undirected Graph — `MEDIUM`
- [ ] `Q10.11` [LC 261] Graph Valid Tree — `MEDIUM`
- [ ] `Q10.12` [LC 743] Network Delay Time (Dijkstra) — `MEDIUM` `MUST DO`
- [ ] `Q10.13` [LC 787] Cheapest Flights Within K Stops (Bellman-Ford / Modified Dijkstra) — `MEDIUM`

### 11. Heaps & Priority Queues
- [ ] `Q11.1` [LC 703] Kth Largest Element in a Stream — `EASY`
- [ ] `Q11.2` [LC 973] K Closest Points to Origin — `MEDIUM` `MUST DO (Vector Space Search)`
- [ ] `Q11.3` [LC 215] Kth Largest Element in an Array (Heap vs QuickSelect) — `MEDIUM` `MUST DO`
- [ ] `Q11.4` [LC 621] Task Scheduler — `MEDIUM` `MUST DO`
- [ ] `Q11.5` [LC 355] Design Twitter — `MEDIUM`
- [ ] `Q11.6` [LC 295] Find Median from Data Stream — `HARD` `MUST DO`
- [ ] `Q11.7` [LC 1146] Snapshot Array — `MEDIUM` `MUST DO (Google Trending)`

### 12. Dynamic Programming (1D, 2D & Sequences)
- [ ] `Q12.1` [LC 198] House Robber — `EASY`
- [ ] `Q12.2` [LC 213] House Robber II — `MEDIUM`
- [ ] `Q12.3` [LC 5] Longest Palindromic Substring — `MEDIUM`
- [ ] `Q12.4` [LC 647] Palindromic Substrings — `MEDIUM`
- [ ] `Q12.5` [LC 91] Decode Ways — `MEDIUM` `MUST DO`
- [ ] `Q12.6` [LC 322] Coin Change — `MEDIUM` `MUST DO`
- [ ] `Q12.7` [LC 152] Maximum Product Subarray — `MEDIUM`
- [ ] `Q12.8` [LC 139] Word Break — `MEDIUM` `MUST DO (LLM Tokenization Decomposition)`
- [ ] `Q12.9` [LC 300] Longest Increasing Subsequence — `MEDIUM` `MUST DO`
- [ ] `Q12.10` [LC 416] Partition Equal Subset Sum — `MEDIUM` `MUST DO`
- [ ] `Q12.11` [LC 62] Unique Paths — `MEDIUM`
- [ ] `Q12.12` [LC 1143] Longest Common Subsequence — `MEDIUM` `MUST DO`
- [ ] `Q12.13` [LC 72] Edit Distance — `MEDIUM` `MUST DO (Core NLP & Sequence Metric)`
- [ ] `Q12.14` [LC 309] Best Time to Buy and Sell Stock with Cooldown — `MEDIUM`
- [ ] `Q12.15` [LC 518] Coin Change II — `MEDIUM`
- [ ] `Q12.16` [LC 494] Target Sum — `MEDIUM`

### 13. Intervals & Sweep Line
- [ ] `Q13.1` [LC 57] Insert Interval — `MEDIUM` `MUST DO`
- [ ] `Q13.2` [LC 56] Merge Intervals — `MEDIUM` `MUST DO (FAANG Standard)`
- [ ] `Q13.3` [LC 435] Non-overlapping Intervals — `MEDIUM`
- [ ] `Q13.4` [LC 253] Meeting Rooms II — `MEDIUM` `MUST DO (Google/Meta Priority)`
- [ ] `Q13.5` [LC 729 / LC 731] My Calendar I & II — `MEDIUM` `TRENDING IN POOL`
- [ ] `Q13.6` [LC 759] Employee Free Time — `HARD` `TRENDING IN POOL`

### 14. Backtracking
- [ ] `Q14.1` [LC 78] Subsets — `MEDIUM`
- [ ] `Q14.2` [LC 39] Combination Sum — `MEDIUM` `MUST DO`
- [ ] `Q14.3` [LC 46] Permutations — `MEDIUM` `MUST DO`
- [ ] `Q14.4` [LC 90] Subsets II (with duplicates) — `MEDIUM`
- [ ] `Q14.5` [LC 40] Combination Sum II — `MEDIUM`
- [ ] `Q14.6` [LC 79] Word Search — `MEDIUM` `MUST DO`
- [ ] `Q14.7` [LC 131] Palindrome Partitioning — `MEDIUM`
- [ ] `Q14.8` [LC 17] Letter Combinations of a Phone Number — `MEDIUM`
- [ ] `Q14.9` [LC 93] Restore IP Addresses — `MEDIUM`
- [ ] `Q14.10` [LC 51] N-Queens — `HARD`

### 15. Greedy & Math
- [ ] `Q15.1` [LC 55] Jump Game — `MEDIUM`
- [ ] `Q15.2` [LC 45] Jump Game II — `MEDIUM`
- [ ] `Q15.3` [LC 134] Gas Station — `MEDIUM`
- [ ] `Q15.4` [LC 846] Hand of Straights — `MEDIUM`
- [ ] `Q15.5` [LC 763] Partition Labels — `MEDIUM`
- [ ] `Q15.6` [LC 678] Valid Parenthesis String — `MEDIUM`
- [ ] `Q15.7` [LC 48] Rotate Image — `MEDIUM` `MUST DO (Matrix Transformations)`
- [ ] `Q15.8` [LC 54] Spiral Matrix — `MEDIUM` `MUST DO`
- [ ] `Q15.9` [LC 73] Set Matrix Zeroes — `MEDIUM`
- [ ] `Q15.10` [LC 50] Pow(x, n) (Fast Exponentiation) — `MEDIUM`

---

## Part 3: AI & Deep Learning Coding From Scratch (Live Coding Checklist)

> *FAANG AI Engineering loops routinely test writing core deep learning primitives from scratch in pure Python, NumPy, or basic PyTorch tensor ops without high-level library calls (`nn.MultiheadAttention`, `F.cross_entropy`, etc.).*

### C1: Attention Mechanisms & Transformer Architecture
- [ ] **C1.1 Scaled Dot-Product Attention (SDPA) from Scratch** `CRITICAL #1 MUST DO`
  - Formula: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}} + M\right) V$
  - Must handle: 4D batch tensor shapes `[B, num_heads, seq_len, head_dim]`, numerical stability, and additive causal mask ($-\infty$).
- [ ] **C1.2 Multi-Head Attention (MHA) Class Implementation** `MUST DO`
  - Linear projections for $W_q, W_k, W_v, W_o$, head splitting, attention calculation, head concatenation.
- [ ] **C1.3 Grouped-Query Attention (GQA) & Multi-Query Attention (MQA)** `2026 HOT TOPIC (Llama 3 / Mistral)`
  - Repeating/broadcasting key and value heads to match multiple query heads; VRAM saving computation.
- [ ] **C1.4 FlashAttention-1/2 Conceptual Tiling Simulation**
  - Block-wise tiling over SRAM memory, online softmax algorithm (tracking running max $m_i$ and running sum $l_i$).

---

### C2: KV-Cache & Autoregressive Decoding
- [ ] **C2.1 KV-Cache Tensor Storage & Update Mechanism** `CRITICAL (FAANG Live Coding)`
  - *Context:* Autoregressive generation where past tokens' $K$ and $V$ are cached so time step $t$ only computes $Q$ for the single new token: $O(1)$ new query instead of recomputing $O(t^2)$ sequence.
  - Implement: Cache initialization, tensor concatenation along sequence dimension, cache indexing.
- [ ] **C2.2 KV-Cache Memory Sizing Calculation (Exact Formula)** `FAANG SCREENING FAVORITE`
  $$\text{Memory (bytes)} = 2 \times 2 \times n_{\text{layers}} \times n_{\text{heads}} \times d_{\text{head}} \times \text{batch\_size} \times \text{seq\_len}$$
  - First $2$ is for $K$ and $V$; second $2$ is for FP16/BF16 bytes; calculate context budget for 128k context on 80GB A100.

---

### C3: Tokenization & Text Preprocessing
- [ ] **C3.1 Byte-Pair Encoding (BPE) Learner & Tokenizer from Scratch** `MUST DO (OpenAI/Anthropic/Meta)`
  - Implement: Frequency counter of adjacent symbol pairs, iterative pair merging, generating vocabulary and merge table.
- [ ] **C3.2 SentencePiece / WordPiece Prefix Splitting Logic**
- [ ] **C3.3 Sliding Window Chunking with Token Overlap**
  - Preserving chunk boundaries and sentence integrity for RAG ingest.

---

### C4: Sampling & Generation Algorithms
- [ ] **C4.1 Greedy Decoding vs Temperature Scaling**
  - Implement: Logits scaling by $T$: $\text{logits}' = \frac{\text{logits}}{T}$. Handling $T \to 0$ edge case.
- [ ] **C4.2 Top-K Sampling Implementation**
  - Mask out logits below $k$-th highest value to $-\infty$, apply softmax, sample using `torch.multinomial` / `np.random.choice`.
- [ ] **C4.3 Top-P (Nucleus) Sampling Implementation** `MUST DO`
  - Sort logits descending, compute cumulative softmax probabilities, mask elements where cumulative sum exceeds $p$, re-normalize and sample.
- [ ] **C4.4 Beam Search with Length Penalty** `HIGH YIELD`
  - Maintain beam width $B$ hypotheses, score with length normalization $\frac{(5 + |Y|)^\alpha}{(5 + 1)^\alpha}$, handle end-of-sequence (`<EOS>`) tokens.

---

### C5: Loss Functions & Numerical Stability
- [ ] **C5.1 Numerically Stable Softmax** `CRITICAL`
  $$\text{softmax}(x)_i = \frac{e^{x_i - \max(x)}}{\sum_j e^{x_j - \max(x)}}$$
  - Prevent floating-point overflow and underflow in NumPy / Pure Python.
- [ ] **C5.2 Cross-Entropy Loss with Log-Sum-Exp Trick** `MUST DO`
  - Negative Log-Likelihood over softmax probabilities avoiding direct `log(0)`.
- [ ] **C5.3 Contrastive Loss (InfoNCE / NT-Xent) for Embedding Models** `CRITICAL (RAG & Two-Tower RecSys)`
  - Temperature-scaled cosine similarity between positive pairs normalized across all in-batch negatives.

---

### C6: Normalization & Positional Embeddings
- [ ] **C6.1 Layer Normalization (LayerNorm)**
  - Normalizing across the feature dimension: $\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} \cdot \gamma + \beta$.
- [ ] **C6.2 RMSNorm (Root Mean Square Normalization)** `MODERN LLM STANDARD (Llama 3)`
  - $\text{RMS}(x) = \sqrt{\frac{1}{d}\sum_{i=1}^d x_i^2 + \epsilon}$, $x_{\text{norm}} = \frac{x}{\text{RMS}(x)} \odot \gamma$.
- [ ] **C6.3 Sinusoidal Positional Embeddings (Attention Is All You Need)**
  - $PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d})$, $PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d})$.
- [ ] **C6.4 Rotary Position Embedding (RoPE)** `MUST KNOW THEORY & CODE`
  - Complex rotation of 2D coordinate pairs; preserving relative distance inner product properties.

---

### C7: Autograd, Optimization & Vector Math
- [ ] **C7.1 Simple Micrograd-style Scalar Autograd Engine**
  - Node class with `.data`, `.grad`, `_backward` closures, topological sort DAG traversal for `.backward()`.
- [ ] **C7.2 Vectorized Cosine Similarity & Pairwise Distance Matrix**
  - Efficient NumPy matrix multiplication $A B^T / (\|A\|_2 \cdot \|B\|_2)$ avoiding slow Python loops.
- [ ] **C7.3 SGD with Momentum & Adam Optimizer from Scratch**
  - First moment $m_t$, second raw moment $v_t$, bias corrections $\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$.

---

### C8: Classical ML Algorithms from Scratch (NumPy)
- [ ] **C8.1 K-Means Clustering & K-Means++ Initialization** `MUST DO (Quantization & Vector Clustering)`
- [ ] **C8.2 Principal Component Analysis (PCA via SVD / Eigendecomposition)**
- [ ] **C8.3 Logistic Regression with L2 Regularization & Vectorized Gradient Descent**
- [ ] **C8.4 Decision Tree Classifier (Gini Impurity / Information Gain Splitter)**

---

## Part 4: Generative AI, LLMs & Modern AI Stack Checklist

### G1: Advanced Retrieval-Augmented Generation (RAG) Architecture
- [ ] **G1.1 Chunking Strategies**
  - Character, recursive token chunking, semantic chunking (embedding cosine similarity threshold split), parent-document retrieval (small-to-big).
- [ ] **G1.2 Hybrid Search Mechanics**
  - Dense semantic search (bi-encoder vector embeddings) combined with Sparse keyword search (BM25 / SPLADE).
- [ ] **G1.3 Reciprocal Rank Fusion (RRF)** `MUST IMPLEMENT`
  $$\text{RRF\_Score}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)} \quad (k \approx 60)$$
- [ ] **G1.4 Cross-Encoder Re-Ranking**
  - Two-stage retrieval: Fast bi-encoder vector search retrieves top 100 $\to$ Cross-encoder reranks top 5 for LLM prompt context.
- [ ] **G1.5 Query Transformation & Decomposition**
  - HyDE (Hypothetical Document Embeddings), Sub-query decomposition, multi-turn query rewriting.
- [ ] **G1.6 Lost-in-the-Middle Mitigation & Context Compression**
  - Ordering highest-relevance documents at the very start and end of prompt context window.

---

### G2: Vector Embeddings & Vector Database Indexing (ANN)
- [ ] **G2.1 HNSW (Hierarchical Navigable Small World) Internals** `CRITICAL SYSTEM DESIGN`
  - Multi-layer skip-list graph structure, greedy routing, parameters $M$ (max links), `efConstruction` (build quality), `efSearch` (query quality). Tradeoffs: latency vs recall vs memory.
- [ ] **G2.2 IVF-Flat & IVF-PQ (Inverted File with Product Quantization)**
  - Voronoi cell partitioning via K-Means, sub-vector quantization into codebooks, asymmetric distance computation (ADC).
- [ ] **G2.3 Distance Metrics & Tradeoffs**
  - Cosine Similarity vs Dot Product (normalized vectors) vs Euclidean Distance ($L2$).

---

### G3: Agentic Architectures & Tool Use
- [ ] **G3.1 ReAct Loop Implementation (Reasoning + Acting + Observation)** `MUST DO`
  - Parsing thought tokens, extracting action strings and JSON arguments, invoking sandboxed python tool, feeding observation back into prompt history.
- [ ] **G3.2 Structured Output Enforcement & Constrained Decoding**
  - JSON schema enforcement via context-free grammar (CFG) masking / logit bias manipulation during generation.
- [ ] **G3.3 Agent Memory Architectures**
  - Short-term sliding token buffer, hierarchical summarization memory, long-term episodic vector memory.
- [ ] **G3.4 Multi-Agent Workflows (Supervisor vs Swarm vs LangGraph DAG)**
  - State passing, cycle detection, deterministic fallback mechanisms.

---

### G4: LLM Serving, Inference Optimization & Hardware Mechanics
- [ ] **G4.1 PagedAttention & vLLM Architecture** `CORE FAANG SYSTEMS TOPIC`
  - Virtual memory paging for KV cache, eliminating internal & external VRAM fragmentation, zero-copy sharing during parallel sampling/beam search.
- [ ] **G4.2 Continuous Batching (In-Flight Batching) vs Static Batching**
  - Iteration-level scheduling: immediately evict finished sequences and inject incoming prompt requests without waiting for batch completion.
- [ ] **G4.3 Speculative Decoding Mechanics**
  - Draft model generates $K$ tokens cheaply $\to$ Target large model verifies all $K$ tokens in a single parallel forward pass using causal acceptance criteria.
- [ ] **G4.4 Model Quantization Paradigms**
  - Post-Training Quantization (PTQ) vs QAT.
  - Weight-Only (AWQ, GPTQ) vs Weight-and-Activation (SmoothQuant, FP8). INT4/INT8 scaling factors and zero-points.
- [ ] **G4.5 Distributed Training & Inference Parallelism**
  - **TP (Tensor Parallelism):** Megatron-LM row-parallel / column-parallel matrix multiplication with `AllReduce`.
  - **PP (Pipeline Parallelism):** Layer partitioning across GPUs, 1F1B schedule, pipeline bubbles.
  - **DP / FSDP / ZeRO:** ZeRO-1 (Optimizer state partitioning), ZeRO-2 (Gradient partitioning), ZeRO-3 (Full parameter sharding).

---

### G5: Model Adaptation, PEFT & Post-Training
- [ ] **G5.1 LoRA (Low-Rank Adaptation) Mathematical Formulation** `MUST KNOW`
  $$W = W_0 + \Delta W = W_0 + \frac{\alpha}{r} (B \cdot A) \quad \text{where } A \in \mathbb{R}^{r \times d_{in}}, B \in \mathbb{R}^{d_{out} \times r}, r \ll d$$
  - Forward pass computation, why $A$ is initialized with Gaussian and $B$ with zeros ($\Delta W = 0$ at start).
- [ ] **G5.2 QLoRA (Quantized LoRA)**
  - 4-bit NormalFloat (NF4), Double Quantization, Paged Optimizers to prevent VRAM spikes.
- [ ] **G5.3 Preference Alignment: DPO vs RLHF (PPO)**
  - Direct Preference Optimization (DPO) closed-form loss vs Actor-Critic-Reward-Value 4-model PPO setup.

---

### G6: LLM Evaluation, Guardrails & Security
- [ ] **G6.1 RAG Triad Evaluation Metrics (Ragas / TruLens)**
  - Context Relevance (retriever quality), Groundedness / Faithfulness (hallucination detector), Answer Relevance (instruction following).
- [ ] **G6.2 LLM-as-a-Judge Design & Bias Mitigation**
  - Pairwise vs Single-score evaluation; mitigating position bias (swap order), verbosity bias, and self-enhancement bias.
- [ ] **G6.3 AI Safety & Guardrails**
  - Jailbreak / Prompt injection detection (delimiter attacks, token smuggling), PII scrubbing, NeMo Guardrails / Llama Guard classifiers.

---

## Part 5: FAANG AI & ML System Design (MLSD) Blueprint

### SD1: Enterprise Knowledge RAG & Semantic Search System
- [ ] Architecture: Ingestion pipeline (OCR, chunking, embedding) $\to$ Kafka $\to$ Hybrid Vector Index (HNSW + OpenSearch BM25) $\to$ Cross-Encoder Reranker $\to$ Multi-tenant LLM Generator with citation attribution.
- [ ] Metrics: Mean Reciprocal Rank (MRR), NDCG@10, p99 Latency $< 800\text{ms}$, Faithfulness $> 98\%$.
- [ ] Scale: 50 Million enterprise documents, 10,000 queries per second (QPS).

### SD2: Real-Time Low-Latency Code Completion (Copilot)
- [ ] Architecture: IDE Client $\to$ WebSocket Streaming Gateway $\to$ Client-side prefix/suffix caching $\to$ Fill-in-the-Middle (FIM) prompt formatting $\to$ Speculative Decoding with 1B draft model $\to$ 7B target model on vLLM cluster.
- [ ] Metrics: Time-To-First-Token (TTFT) $< 50\text{ms}$, Acceptance Rate (Keystrokes saved $> 35\%$).

### SD3: Billion-Scale Vector Search Engine (1B+ Vectors)
- [ ] Architecture: Distributed Vector Database (e.g., Milvus / FAISS cluster). Two-level hierarchical partitioning: Inverted index (IVF) on cluster nodes + Product Quantization (PQ) for RAM reduction.
- [ ] Sizing: 1 Billion 1536-dim vectors in FP32 = $10^9 \times 1536 \times 4 \approx 6.14\text{ TB}$. Quantized via PQ to 64 bytes = $64\text{ GB}$ (fits in a single host RAM!).

### SD4: High-Throughput Multi-Tenant LLM Serving Platform
- [ ] Architecture: Reverse Proxy / API Gateway (API Key rate-limiting, semantic caching via Redis) $\to$ Triton / vLLM Inference Engine $\to$ Continuous Batching $\to$ Dynamic GPU autoscaler based on active token queue depth.
- [ ] Fault Tolerance: Graceful degradation, fallback to smaller model / quantized tier upon GPU cluster saturation.

### SD5: Multimodal Video/Image Recommendation System
- [ ] Architecture: Two-Tower Neural Network (User/Context Tower + Video Content Tower with CLIP vision embeddings) $\to$ Candidate Generation (ANN search top 1000) $\to$ Heavy Deep Ranking Network (DLRM / Transformer ranker top 100) $\to$ Re-ranking for diversity, freshness, and safety.

### SD6: Autonomous AI Agent Platform with Tool Execution
- [ ] Architecture: Orchestrator agent $\to$ Sub-agent task graph $\to$ Sandboxed microVM / Docker container for code execution $\to$ State management (Checkpointer in PostgreSQL) $\to$ Human-in-the-Loop approval gate for destructive actions.

### SD7: Continuous Fine-Tuning & Alignment Platform (RLHF/DPO)
- [ ] Architecture: User feedback collection (thumbs up/down, pairwise edits) $\to$ Data deduplication & quality filtering (LLM judge) $\to$ Distributed training cluster (Slurm / Ray with FSDP + LoRA) $\to$ Automated benchmark evaluation (MMLU, HumanEval) $\to$ Canary model deployment.

---

## Part 6: FAANG Python Speed, Testing & Edge-Case Cheat-Sheet

### E1: High-Performance Python Constructs & Standard Library
- [ ] **Collections:**
  - Always use `collections.deque` for $O(1)$ `popleft()`. Never use `list.pop(0)` ($O(N)$ penalty).
  - Use `collections.defaultdict(list)` or `collections.Counter` to avoid verbose `if key not in d` checks.
- [ ] **Heaps:**
  - Python's `heapq` is a **min-heap** by default. For max-heap, push `(-val, obj)`.
  - In-place heapify: `heapq.heapify(nums)` runs in $O(N)$, not $O(N \log N)$.
- [ ] **Binary Search:**
  - Use `bisect.bisect_left(arr, x)` for lower bound (first index $\ge x$).
  - Use `bisect.bisect_right(arr, x)` for upper bound (first index $> x$).
- [ ] **Recursion Depth:**
  - Standard Python recursion limit is 1000. In deep DFS tree/graph problems:
    ```python
    import sys
    sys.setrecursionlimit(200000)
    ```
- [ ] **Memoization:**
  - Use `@functools.lru_cache(None)` for clean DP memoization without manual cache dictionary boilerplate.

---

### E2: Numerical Precision Pitfalls in AI Coding
- [ ] **Floating Point Underflow in Probabilities:**
  - Never multiply small probabilities: $\prod_{i} p_i \to 0.0$ (underflow).
  - Always work in log-space: $\sum_{i} \log p_i$.
- [ ] **Log-Sum-Exp Trick:**
  - To compute $\log \sum_{i} e^{x_i}$:
    $$m = \max(x), \quad \log \left(\sum_{i} e^{x_i - m}\right) + m$$
- [ ] **Division by Zero in Normalization:**
  - Always include $\epsilon = 1e-5$ or $1e-8$ inside square roots: $\frac{x}{\sqrt{\sigma^2 + \epsilon}}$.
- [ ] **Matrix Multiplication Order & Dimensions:**
  - Double-check tensor shapes before calling `np.dot` or `@`:
    - `[B, S, D] @ [B, D, S] -> [B, S, S]` (Attention matrix shape).

---

### E3: FAANG Coding Round Execution Protocol (The 5-Step Formula)
- [ ] **Step 1: Clarify & Scope (3–5 min)**
  - Clarify input bounds ($N \le 10^5 \implies O(N \log N)$ or $O(N)$; $N \le 20 \implies O(2^N)$ backtracking).
  - Clarify data types (integers, negative numbers, empty inputs, single-node graphs, duplicate tokens).
- [ ] **Step 2: Propose Approaches & Analyze Complexity (5 min)**
  - State Brute Force first $\to$ Identify bottleneck $\to$ Propose optimal solution.
  - State explicit Big-O Time and Space complexity **before writing any code**.
- [ ] **Step 3: Clean, Modular Implementation (15–20 min)**
  - Write idiomatic Python with clean variable names (`left, right`, `cur_sum`, `visited`, `indegree`).
  - Keep helper functions cleanly modularized.
- [ ] **Step 4: Dry-Run on Concrete Example (5 min)**
  - Step through line-by-line using a small example on paper/comments before asking the interviewer if it looks good.
  - Trace pointers and variable updates.
- [ ] **Step 5: Edge Case Verification (3–5 min)**
  - Test: Empty input, single element, all duplicates, strictly increasing/decreasing array, disconnected graph, cycles.

---

## 📈 Weekly Milestone Execution Plan

- [ ] **Week 1–2: Algorithmic Core (P1–P4, P6)**: Graphs, Trees, Sliding Window, Prefix Sum, Binary Search. Complete LeetCode high-yield set (50 questions).
- [ ] **Week 3–4: Advanced DSA & Data Structures (P5, P7–P10)**: Monotonic Stack, Intervals, Heaps, DP, Trie. Complete remaining LeetCode questions (50 questions).
- [ ] **Week 5–6: AI & DL Coding from Scratch (C1–C8)**: Pure NumPy & PyTorch implementations of MHA, KV-Cache, BPE, Sampling, Autograd, RMSNorm, Losses.
- [ ] **Week 7–8: GenAI, RAG & LLM Systems (G1–G6)**: Deep dive into RAG, Vector Search, HNSW, vLLM serving, Quantization, LoRA, and Agent loops.
- [ ] **Week 9–10: AI / ML System Design (SD1–SD7)**: Master the 7 FAANG system architectures; practice end-to-end whiteboarding.
- [ ] **Week 11–12: Full Mock Interviews & Edge Cases**: Timed DSA mock rounds (45 min), ML coding mocks, and behavioral alignment.
