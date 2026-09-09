# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Completed Implementation

For this assignment, I used a Binary Search Tree to organize an IT asset inventory by numeric asset ID. I completed recursive insertion, searching, and in-order traversal. I also tested existing and missing asset IDs along with an empty tree, a duplicate value, and a single-node tree.

The program used smaller asset IDs in the left subtree and larger IDs in the right subtree. I also built a second tree using sequential IDs to demonstrate how insertion order can create a skewed tree.

## Completed Reflection

For this assignment, I stayed with the IT theme and used a Binary Search Tree to organize equipment by asset ID. The biggest thing I learned was how much the shape of a BST depends on insertion order. With a reasonably balanced tree, each comparison sends the search down only one branch, which can keep search performance near O(log n) instead of checking every item like a linear search.

The recursive insertion and search methods took the most thought because each call had to move left for a smaller ID or right for a larger one until it reached a match or an empty position. In-order traversal was easier once I connected left-current-right with the BST ordering rule. That traversal returned the asset IDs in sorted order automatically.

I also tested an empty tree, a duplicate asset ID, and a single-node tree. Sequential IDs showed the main weakness of a basic BST. If every new value is larger than the previous one, the tree becomes skewed like a linked list and search performance can fall to O(n).