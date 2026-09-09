# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation

I created a network device asset lookup tool to compare linear search and binary search in an IT environment.

I implemented linear search by checking each asset ID from the beginning of the list until the target was found. If the target did not exist, the function returned -1.

I implemented binary search by using low, high, and middle positions to search a sorted list of asset IDs. After each comparison, half of the remaining search area was removed until the target was found or there were no values left to check.

I tested both algorithms with a small sorted device inventory and a larger inventory containing 5,000 asset IDs. Both methods returned the same results, but binary search became much more efficient as the dataset grew.

I also tested an empty inventory and asset IDs that were below and above the valid range. In each case, both search methods returned -1 without errors.

## Performance Analysis

Linear search had O(n) time complexity because it could require checking every asset ID in the list.

Binary search had O(log n) time complexity because each comparison cut the remaining search area in half.

For a large sorted device inventory, binary search was the better choice because it reduced the amount of data that had to be checked after every comparison.

Linear search still made sense for smaller or unsorted data. For example, devices returned from a recent network scan may be listed in discovery order instead of sorted asset-ID order. If an administrator only needed one quick lookup, checking those results from beginning to end could be simpler than sorting the entire list first.

## Edge Cases

I tested three edge cases:

- An empty device inventory
- A target asset ID below the smallest stored ID
- A target asset ID above the largest stored ID

These tests showed that both algorithms handled missing data safely and returned -1 when the target could not be found.

## Real-World Application

The program modeled a basic IT asset lookup system.

An organization may keep thousands of workstations, laptops, servers, switches, and other devices in an inventory system. If the asset IDs are sorted, binary search can locate a specific device much more efficiently than checking every record one at a time.

Linear search can still be useful when the data is unsorted, newly collected, or small enough that sorting it first would not be worth the extra work.

## Discussion Board Reflection

This assignment helped me better understand how the way data is organized affects which search algorithm makes the most sense. Linear search was easier to follow because it simply checked each asset ID from beginning to end. Binary search took more thought because I had to keep track of the low, high, and middle positions and make sure the correct half of the list was removed after each comparison.

The edge cases were useful because they showed what happens when the target is completely outside the range of the stored data. I tested an empty inventory along with asset IDs below and above the valid range, and both methods returned -1 correctly.

For a large sorted IT asset inventory, binary search makes more sense because it cuts the remaining search area in half each time. Linear search is still useful for smaller or unsorted data, such as results from a newly completed network scan. Sorting those results first may not be worth the effort if an administrator only needs to perform one quick lookup.