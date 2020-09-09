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
| Quicksort      | O(n log(n)) | O(n log(n)) | O(n**2)     | O(n)        |
| Mergesort      | O(n log(n)) | O(n log(n)) | O(n log(n)) | O(n)        |
| Heapsort       | O(n log(n)) | O(n log(n)) | O(n log(n)) | O(1)        |
| Bubble Sort    | O(n)        | O(n**2)     | O(n**2)     | O(1)        |
| Insertion Sort | O(n)        | O(n**2)     | O(n**2)     | O(1)        |
| Selection Sort | O(n**2)     | O(n**2)     | O(n**2)     | O(1)        |
| Bucket Sort    | O(n+k)      | O(n+k)      | O(n**2)     | O(nk)       |
| Radix Sort     | O(nk)       | O(nk)       | O(nk)       | O(n+k)      |
+----------------+-------------+-------------+-------------+-------------+
```
[Sorting](sort.py) examples
## Dynamic Programming
There are two key attributes that a problem must have in order for dynamic programming to be applicable: optimal substructure and overlapping sub-problems. If a problem can be solved by combining optimal solutions to non-overlapping sub-problems, the strategy is called "divide and conquer" instead.

[Fibonacci memoization](math.py#L45) example
## Divide And Conquer
Technique is the basis of efficient algorithms for all kinds of problems, such as sorting (e.g., quicksort, merge sort), multiplying large numbers (e.g. the Karatsuba algorithm), finding the closest pair of points, syntactic analysis (e.g., top-down parsers), and computing the discrete Fourier transform.

[Fibonacci fast doubling](math.py#L64) and [multiply by Karatsuba algorithm](math.py#L139) examples
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
### Singly linked list vs Doubly linked list
Complexity
- In singly linked list the complexity of insertion and deletion at a known position is O(n)
- In case od doubly linked list the complexity of insertion and deletion at a known position is O(1)

Implementation
- In singly linked list implementation is such as where the node contains some data and a pointer to the next node in the list
- While doubly linked list has some more complex implementation where the node contains some data and a pointer to the next as well as the previous node in the list
Order of elements
- Singly linked list allows traversal elements only in one way
- Doubly linked list allows element two way traversal

Usage
- Singly linked list are generally used for implementation of stacks
- On other hand doubly linked list can be used to implement stacks as well as heaps and binary trees

Index performance
- Singly linked list is preferred when we need to save memory and searching is not required as pointer of single index is stored
- If we need better performance while searching and memory is not a limitation in this case doubly linked list is more preferred

Memory consumption
- As singly linked list store pointer of only one node so consumes lesser memory
- On other hand Doubly linked list uses more memory per node(two pointers)
