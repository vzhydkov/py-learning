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

### Compare Quadratic to Linearithmic
```
n**n / (n log(n)) = n / log(n) = 1,000,000 / lg(1,000,000)
Since  2**20 is approximately 1 million, the ratio approximately 50,000
```

# Sorting algorithms
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
[Sorting examples](sort.py)

