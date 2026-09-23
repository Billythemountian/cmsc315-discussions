# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and contrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to use each.

## Completed Implementation

For this assignment, I created a server response time sorter to compare Bubble Sort and Merge Sort in an IT environment.

The program organized server response times measured in milliseconds. I used one dataset representing normal streaming activity and another representing peak activity with slower server responses.

Both sorting algorithms returned new lists, allowing the original measurements to remain unchanged.

## Bubble Sort

I implemented Bubble Sort using nested loops that compared neighboring response times and swapped values when they were out of order.

I also included a swapped flag to stop sorting when a complete pass made no changes.

Bubble Sort has O(n²) average and worst-case time complexity because the number of comparisons can grow quadratically as more values are added.

The early-stop optimization allows O(n) best-case time when the list is already sorted.

## Merge Sort

I implemented Merge Sort using recursion to divide the response times into smaller halves.

The merge() helper compared values from both sorted halves and combined them into one sorted list.

A list containing zero or one element provided the recursive base case.

Merge Sort has O(n log n) time complexity because the data is repeatedly divided and each level requires merging the elements.

## Dataset Testing

Dataset #1 represented response times during normal streaming activity.

Original values:

142, 87, 215, 96, 301, 74, 168, 109

Both algorithms returned:

74, 87, 96, 109, 142, 168, 215, 301

Dataset #2 represented response times during peak streaming activity.

Original values:

85, 98, 114, 128, 145, 139, 165, 420, 610, 145

Both algorithms returned:

85, 98, 114, 128, 139, 145, 145, 165, 420, 610

The second dataset was nearly sorted but included duplicate values and much slower responses.

Both algorithms produced the same ascending results.

## Edge Cases

I included five edge cases:

- Empty measurements
- A single response time
- Already-sorted response times
- Reverse-sorted response times
- Duplicate response times

The empty list and single-element list required no sorting.

The already-sorted list demonstrated Bubble Sort's early-stop optimization.

The reverse-sorted list required additional swaps in Bubble Sort.

The duplicate-value test confirmed that repeated response times were preserved.

Both algorithms were implemented to preserve the relative order of equal values. Bubble Sort avoided swapping equal values, and Merge Sort selected from the left half first when values were equal.

## Performance Analysis

Bubble Sort was straightforward to implement, but its O(n²) average and worst-case time complexity makes it inefficient for large monitoring datasets.

Merge Sort used O(n log n) time in the best, average, and worst cases.

This makes Merge Sort more predictable when organizing large amounts of monitoring data.

The tradeoff is memory usage. The standard Bubble Sort algorithm can sort in place, although this assignment required copying the original list. Merge Sort also required temporary lists while dividing and merging data.

## Real-World Application

A streaming platform may collect thousands of server response time measurements during a major premiere or live sporting event.

Sorting these measurements makes unusually slow responses easier to identify.

For a small collection of measurements, Bubble Sort can organize the data with simple comparison and swap operations.

For large collections of monitoring data, Merge Sort provides more predictable sorting performance and can divide work into smaller tasks.

The sorted measurements can help administrators investigate performance problems and identify possible areas of congestion.

## Completed Reflection

For this assignment, I stayed with the IT theme and created a server response time sorter using Bubble Sort and Merge Sort. I wanted to demonstrate how a streaming platform could organize performance measurements during normal activity and periods of heavier demand.

Bubble Sort was easier to follow because it compared neighboring response times and swapped them when necessary. I added a swapped flag so the algorithm could stop when everything was already in order. Merge Sort took more thought because I had to understand how the recursive calls divided the list and how the merge() function put everything back together without losing any values.

Testing empty lists, duplicate response times, and reverse-sorted data helped me understand why the algorithms need to work beyond a single example.

The biggest difference was efficiency. Bubble Sort uses O(n²) time on average and in the worst case, so comparisons grow quickly with larger datasets. Merge Sort uses O(n log n) time and handles larger collections more predictably, although it requires additional memory. Bubble Sort is straightforward for small datasets, while Merge Sort makes more sense for large monitoring systems.