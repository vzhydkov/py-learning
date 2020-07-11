# Big O Notation
```
     | Constant | Logarithmic |Linear | Linearithmic | Quadratic | Exponential |Factorial
N    | O(1)     | O(log(n))   | O(n)  | O(n*log(n))  | O(n**n)   | O(2**n)     | O(n!) |
1    | 1        | 1           | 1     | 1            | 1         | 2           | 2     |
4    | 1        | 2           | 4     | 8            | 16        | 16          | 24    |
16   | 1        | 4           | 16    | 64           | 256       | 65536       | 16!   |
1024 | 1        | 10          | 1024  | 10240        | 1048576   | 2**1024     | 1024! |
```
### Constant
- Odd or Even number
- Look-up table (on average)
### Logarithmic
- Finding element on sorted array with binary search
### Linear
- Find max element in unsorted array,
- Duplicate elements in array with Hash Map
### Linearithmic
- Sorting elements in array with merge sort
### Quadratic
- Duplicate elements in array
- Sorting array with bubble sort
### Exponential
- Find all subsets
### Factorial
- Find all permutations of a given set/string

## Compare O(n**n) to O(n*log(n))
```
n**n / (n lg n) = n / lg n = 1,000,000 / lg(1,000,000)
Since  2**20 is approximately 1 million, we obtain approximately 50,000
```
