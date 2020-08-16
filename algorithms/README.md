# Big O Notation
```
     | Constant | Logarithmic |Linear | Linearithmic | Quadratic | Exponential | Factorial |
N    | O(1)     | O(log(n))   | O(n)  | O(n log(n))  | O(n**n)   | O(2**n)     | O(n!)     |
1    | 1        | 1           | 1     | 1            | 1         | 2           | 2         |
4    | 1        | 2           | 4     | 8            | 16        | 16          | 24        |
16   | 1        | 4           | 16    | 64           | 256       | 65536       | 16!       |
1024 | 1        | 10          | 1024  | 10240        | 1048576   | 2**1024     | 1024!     |
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
# Sorting
```
Algorithm      |             Time Complexity             | Space Complexity |
               | Best        | Average     | Worst       | Worst            |
Quicksort      | O(n log(n)) | O(n log(n)) | O(n**2)     | O(n)             |
Mergesort      | O(n log(n)) | O(n log(n)) | O(n log(n)) | O(n)             |
Heapsort       | O(n log(n)) | O(n log(n)) | O(n log(n)) | O(1)             |
Bubble Sort    | O(n)        | O(n**2)     | O(n**2)     | O(1)             |
Insertion Sort | O(n)        | O(n**2)     | O(n**2)     | O(1)             |
Select Sort    | O(n**2)     | O(n**2)     | O(n**2)     | O(1)             |
Bucket Sort    | O(n+k)      | O(n+k)      | O(n**2)     | O(nk)            |
Radix Sort     | O(nk)       | O(nk)       | O(nk)       | O(n+k)           |
```
[Sorting](sort.py) examples
# Graph
# Tree
### BFS vs DFS (for Binary Tree)
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

Space Complexity:
- Extra Space required for Level Order Traversal is O(w) where w is maximum width of Binary Tree. In level order traversal, queue one by one stores nodes of different level.
- Extra Space required for Depth First Traversals is O(h) where h is maximum height of Binary Tree. In Depth First Traversals, stack (or function call stack) stores all ancestors of a node.

[Tree](tree.py) examples
# Hash Table
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
# Dynamic Programming
[Fibonacci memoization](math.py#L45) example
# Divide And Conquer algorithm
[Fibonacci fast doubling](math.py#L64) example
