"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Start at the beginning and check each asset ID one at a time.
    for index in range(len(lst)):

        # If this ID matches what we are looking for, return its index.
        if lst[index] == target:
            return index

    # If the ID is near the end or missing, we may check the whole list.
    # That is why linear search is O(n).
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Start with the entire sorted list.
    low = 0
    high = len(lst) - 1

    # Keep searching while there is still part of the list left.
    while low <= high:

        # Find the middle of the current search area.
        middle = (low + high) // 2

        # If the middle ID is the one we want, return its index.
        if lst[middle] == target:
            return middle

        # If the target is bigger, we can ignore the left half.
        if lst[middle] < target:
            low = middle + 1

        # If the target is smaller, we can ignore the right half.
        else:
            high = middle - 1

    # If we run out of places to search, the asset ID is not there.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # A small sorted list of asset IDs from a network inventory.
    small_inventory = [1012, 1048, 1075, 1103, 1144, 1189, 1210]

    # Asset 1103 is in the list, so both searches should find index 3.
    print(
        "Linear search for asset 1103:",
        linear_search(small_inventory, 1103)
    )

    print(
        "Binary search for asset 1103:",
        binary_search(small_inventory, 1103)
    )

    # Asset 1160 is not in the list, so both searches should return -1.
    print(
        "Linear search for asset 1160:",
        linear_search(small_inventory, 1160)
    )

    print(
        "Binary search for asset 1160:",
        binary_search(small_inventory, 1160)
    )

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Build a larger inventory with 5,000 sorted asset IDs.
    large_inventory = list(range(1000, 11000, 2))

    # Search for an asset near the end of the list.
    print(
        "Linear search for asset 9998:",
        linear_search(large_inventory, 9998)
    )

    print(
        "Binary search for asset 9998:",
        binary_search(large_inventory, 9998)
    )

    # Both searches find the same asset, but they get there differently.
    # Linear search may check thousands of IDs one at a time.
    # Binary search cuts the list in half each time, so it scales much better.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: There are no devices in the inventory.
    empty_inventory = []

    print(
        "Linear search empty inventory:",
        linear_search(empty_inventory, 1050)
    )

    print(
        "Binary search empty inventory:",
        binary_search(empty_inventory, 1050)
    )

    # There is nothing to search, so both methods return -1.

    # Edge case 2: The target is lower than every asset ID in the list.
    print(
        "Linear search below inventory range:",
        linear_search(small_inventory, 900)
    )

    print(
        "Binary search below inventory range:",
        binary_search(small_inventory, 900)
    )

    # Binary search keeps moving left until there is nothing left to check.

    # Edge case 3: The target is higher than every asset ID in the list.
    print(
        "Linear search above inventory range:",
        linear_search(small_inventory, 1500)
    )

    print(
        "Binary search above inventory range:",
        binary_search(small_inventory, 1500)
    )

    # Binary search keeps moving right until there is nothing left to check.


if __name__ == "__main__":
    main()