- [Big O Notation](#big-o-notation)
- [Algorithms](#algorithms)
    - [Sorting](#sorting)
    - [Dynamic Programming](#dynamic-programming)
    - [Divide And Conquer](#divide-and-conquer)
- [Data Structures](#data-structures)
    - [Graph](#graph)
    - [Tree](#tree)
    - [Hash Table](#hash-table)
    - [List](#list)
# Big O Notation
```
+------+----------+-------------+-------+--------------+-----------+-------------+-----------+
|      | Constant | Logarithmic |Linear | Linearithmic | Quadratic | Exponential | Factorial |
+------+----------+-------------+-------+--------------+-----------+-------------+-----------+
| N    | O(1)     | O(log(n))   | O(n)  | O(n log(n))  | O(n**n)   | O(2**n)     | O(n!)     |
| 1    | 1        | 1           | 1     | 1            | 1         | 2           | 2         |
| 4    | 1        | 2           | 4     | 8            | 16        | 16          | 24        |
| 16   | 1        | 4           | 16    | 64           | 256       | 65536       | 16!       |
| 1024 | 1        | 10          | 1024  | 10240        | 1048576   | 2**1024     | 1024!     |
+------+----------+-------------+-------+--------------+-----------+-------------+-----------+
```
- **Constant** odd or even number or Look-up table (on average)
- **Logarithmic** finding element on sorted array with binary search
- **Linear** find max element in unsorted array or duplicate elements in array with Hash Map
- **Linearithmic** sorting elements in array with merge sort
- **Quadratic** duplicate elements in array or sorting array with bubble sort
- **Exponential** find all subsets
- **Factorial** find all permutations of a given set/string

Compare Quadratic to Linearithmic
```
n**n / (n log(n)) = n / log(n) = 1,000,000 / lg(1,000,000)
Since  2**20 is approximately 1 million, the ratio approximately 50,000
```
# Algorithms
## Sorting
```
+----------------+-----------------------------------------+-------------+
|                |             Time Complexity             | Space usage |
|   Algorithm    |-------------+-------------+-------------+-------------+
|                | Best        | Average     | Worst       | Worst       |
+----------------+-------------+-------------+-------------+-------------+
| Quick Sort     | Ω(n log(n)) | Θ(n log(n)) | O(n**2)     | O(n)        |
| Merge Sort     | Ω(n log(n)) | Θ(n log(n)) | O(n log(n)) | O(n)        |
| Heap Sort      | Ω(n log(n)) | Θ(n log(n)) | O(n log(n)) | O(1)        |
| Tim Sort       | Ω(n)        | Θ(n log(n)) | O(n log(n)) | O(n)        |
| Bubble Sort    | Ω(n)        | Θ(n**2)     | O(n**2)     | O(1)        |
| Insertion Sort | Ω(n)        | Θ(n**2)     | O(n**2)     | O(1)        |
| Selection Sort | Ω(n**2)     | Θ(n**2)     | O(n**2)     | O(1)        |
| Bucket Sort    | Ω(n+k)      | Θ(n+k)      | O(n**2)     | O(nk)       |
| Radix Sort     | Ω(nk)       | Θ(nk)       | O(nk)       | O(n+k)      |
+----------------+-------------+-------------+-------------+-------------+
```
[Sorting](sort.py) examples
## Dynamic Programming
There are two key attributes that a problem must have in order for dynamic programming to be applicable: optimal substructure and overlapping sub-problems. If a problem can be solved by combining optimal solutions to non-overlapping sub-problems, the strategy is called "divide and conquer" instead.

[Fibonacci memoization](fibonacci.py#L46) example
## Divide And Conquer
Technique is the basis of efficient algorithms for all kinds of problems, such as sorting (e.g., quick sort, merge sort), multiplying large numbers (e.g. the Karatsuba algorithm), finding the closest pair of points, syntactic analysis (e.g., top-down parsers), and computing the discrete Fourier transform.

[Fibonacci fast doubling](fibonacci.py#L65) and [multiply by Karatsuba algorithm](math.py#L1) examples
# Data structures
```
+----------------------+----------+------------+----------+-------------+
|                      |         Time Complexity          |             |
|   Data Structure     |----------+------------+----------| Space usage |
|                      |  Insert  |   Delete   |  Search  |             |
+----------------------+----------+------------+----------+-------------+
| Unsorted array       | O(1)     | O(1)       | O(n)     | O(n)        |
| Value-indexed array  | O(1)     | O(1)       | O(1)     | O(n)        |
| Sorted array         | O(n)     | O(n)       | O(log n) | O(n)        |
| Unsorted linked list | O(1)*    | O(1)*      | O(n)     | O(n)        |
| Sorted linked list   | O(n)*    | O(1)*      | O(n)     | O(n)        |
| Balanced binary tree | O(log n) | O(log n)   | O(log n) | O(n)        |
| Heap                 | O(log n) | O(log n)** | O(n)     | O(n)        |
| Hash table           | O(1)     | O(1)       | O(1)     | O(n)        |
+----------------------+----------+------------+----------+-------------+
```
`*` The cost to add or delete an element into a known location in the list (i.e. if you have an iterator to the location) is O(1). If you don't know the location, then you need to traverse the list to the location of deletion/insertion, which takes O(n) time.

`**` The deletion cost is O(log n) for the minimum or maximum, O(n) for an arbitrary element.
## Graph
[Graph](graph.py) examples
## Tree
### Tree Traversals: BFS vs DFS
BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. So if our problem is to search something that is more likely to closer to root, we would prefer BFS. And if the target node is close to a leaf, we would prefer DFS.

DFS stands for Depth First Search is a edge based technique. It uses the Stack data structure, performs two stages, first visited vertices are pushed into stack and second if there is no vertices then visited vertices are popped.
```
        1
       / \
      2   3
     / \
    4   5 
```
Breadth First Traversal
- Level Order Traversal: 1 2 3 4 5

Depth First Traversals
- Preorder Traversal: 1 2 4 5 3 
- Inorder Traversal:  4 2 5 1 3 
- Postorder Traversal: 4 5 2 3 1

Time Complexity: O(n)

Space usage:
- Extra Space required for Level Order Traversal is O(w) where w is maximum width of Binary Tree. In level order traversal, queue one by one stores nodes of different level.
- Extra Space required for Depth First Traversals is O(h) where h is maximum height of Binary Tree. In Depth First Traversals, stack (or function call stack) stores all ancestors of a node.

[Tree](tree.py) examples
## Union Find
```
+----------------------------------------------------------+
|               Algorithm                 | Worst-case time|
+-----------------------------------------+----------------+
| quick-find                              | MN             |
| quick-union                             | MN             |
| weighted quick-union                    | N + M log N    |
| quick-union & path compression          |  N + M log N   |
| weighted quick-union & path compression |  N + M lg N    |
+-----------------------------------------+----------------+
M union find operations on a set of N objects
```
## Hash Table
### Separate chaining vs linear probing
Separate chaining
- Easier to implement delete
- Performance degrades gracefully
- Clustering less sensitive to poorly-designed hash function

Linear probing
- Less wasted space
- Better cache performance
### Hash table vs balanced search trees
Hash tables
- Simpler to code
- No effective alternative for unordered keys
- Faster for simple keys (a few arithmetic ops versus log N compares)

Balanced search trees
- Stronger performance guarantee
- Support for ordered ST operations
- Easier to implement compareTo() correctly than equals() and hashCode()
## List
### Stack
LIFO - last in first out
### Queue
FIFO - first in first out (linked lists have a performance advantage over lists here)
### Singly linked list vs Doubly linked list
Complexity
- In singly linked list the complexity of insertion and deletion at a known position is O(n)
- In case of doubly linked list the complexity of insertion and deletion at a known position is O(1)

Implementation
- In singly linked list implementation is such as where the node contains some data and a pointer to the next node in the list
- While doubly linked list has some more complex implementation where the node contains some data and a pointer to the next as well as the previous node in the list
Order of elements
- Singly linked list allows traversal elements only in one way
- Doubly linked list allows element two-way traversal

Usage
- Singly linked list are generally used for implementation of stacks
- On other hand doubly linked list can be used to implement stacks as well as heaps and binary trees

Index performance
- Singly linked list is preferred when we need to save memory and searching is not required as pointer of single index is stored
- If we need better performance while searching and memory is not a limitation in this case doubly linked list is more preferred

Memory consumption
- As singly linked list store pointer of only one node so consumes lesser memory
- On other hand Doubly linked list uses more memory per node(two pointers)
### Binary Heap
Array representation of a heap-ordered complete binary tree
Time complicity insert/del max O(log n) and max O(1) 
Heap-ordered binary tree:
- keys in nodes
- parent's keys no smaller than children's keys

[List examples](list.py)
