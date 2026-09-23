"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:

- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # Copy the response times so the original data stays unchanged.
    arr = lst.copy()

    # Store the number of response times.
    n = len(arr)

    # Make passes through the list until everything is sorted.
    for i in range(n - 1):

        # Track whether any values were swapped during this pass.
        swapped = False

        # Compare neighboring response times.
        for j in range(n - 1 - i):

            # Move the larger response time to the right.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # No swaps means the list is already sorted.
        if not swapped:
            break

    # Nested loops give Bubble Sort O(n²) worst-case time.
    return arr


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # A list with zero or one response time is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle and divide the response times into two halves.
    mid = len(lst) // 2

    # Recursively sort both halves.
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # Combine the sorted halves into one sorted list.
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    # Create a list to hold the sorted response times.
    result = []

    # Track our position in each half.
    i = 0
    j = 0

    # Keep comparing while both halves have values remaining.
    while i < len(left) and j < len(right):

        # Add the smaller response time from the left half.
        # Using <= keeps equal values in their original order.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        # Otherwise, take the smaller value from the right half.
        else:
            result.append(right[j])
            j += 1

    # Add any response times remaining in either half.
    result.extend(left[i:])
    result.extend(right[j:])

    # Merge Sort takes O(n log n) time and uses extra memory.
    return result


def main():

    print("=== UNIT 7: SORTING ALGORITHMS ===")
    print("IT Scenario: Server Response Time Monitoring")
    print("All response times are measured in milliseconds (ms).")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1: NORMAL SERVER ACTIVITY ===")

    # Response times collected during a normal streaming period.
    # The values are unsorted and represent different server requests.
    normal_times = [
        142, 87, 215, 96, 301, 74, 168, 109
    ]

    print("Original response times:", normal_times)

    # Sort the same measurements using both algorithms.
    bubble_normal = bubble_sort(normal_times)
    merge_normal = merge_sort(normal_times)

    print("Bubble Sort:", bubble_normal)
    print("Merge Sort: ", merge_normal)

    # Verify that both algorithms produced the correct order.
    print(
        "Both algorithms match:",
        bubble_normal == merge_normal == sorted(normal_times)
    )

    print(
        "Interpretation: Sorting makes it easier to identify "
        "the fastest and slowest recorded responses."
    )

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2: PEAK STREAMING ACTIVITY ===")

    # Response times collected during a major streaming event.
    # This list is nearly sorted but includes slower responses.
    peak_times = [
        85, 98, 114, 128, 145,
        139, 165, 420, 610, 145
    ]

    print("Original response times:", peak_times)

    # Test both algorithms using the same peak activity data.
    bubble_peak = bubble_sort(peak_times)
    merge_peak = merge_sort(peak_times)

    print("Bubble Sort:", bubble_peak)
    print("Merge Sort: ", merge_peak)

    # Confirm that both produce the expected sorted results.
    print(
        "Both algorithms match:",
        bubble_peak == merge_peak == sorted(peak_times)
    )

    print(
        "Interpretation: Higher response times stand out "
        "after sorting, including the 420 ms and 610 ms requests."
    )

    print("\n=== ALGORITHM PERFORMANCE COMPARISON ===")

    # Bubble Sort compares neighboring values using nested loops.
    print(
        "Bubble Sort: O(n²) average and worst-case time. "
        "It may require many comparisons as the dataset grows."
    )

    # The swapped flag stops Bubble Sort when no more changes occur.
    print(
        "Bubble Sort best case: O(n) when the list is already sorted."
    )

    # Merge Sort repeatedly divides the list and combines sorted halves.
    print(
        "Merge Sort: O(n log n) time because it divides the "
        "data into smaller parts before merging them."
    )

    print(
        "Memory tradeoff: Bubble Sort creates one list copy, "
        "while Merge Sort also creates temporary lists during sorting."
    )

    print(
        "For large monitoring datasets, Merge Sort offers "
        "more predictable sorting performance."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Test several situations that may occur when collecting
    # server response times.

    edge_cases = [
        ("Empty measurements", []),
        ("Single response", [125]),
        ("Already sorted", [70, 85, 100, 120, 150]),
        ("Reverse sorted", [500, 400, 300, 200, 100]),
        ("Duplicate times", [120, 85, 120, 95, 85, 150])
    ]

    # Explain why each edge case matters.
    explanations = [
        "No measurements were collected. Both return an empty list.",
        "One measurement does not require any sorting.",
        "Bubble Sort can stop after one pass with no swaps.",
        "Bubble Sort must move many values into the correct order.",
        "Equal response times remain in the sorted results."
    ]

    # Run both algorithms on every edge case.
    for i in range(len(edge_cases)):

        name, data = edge_cases[i]

        print(f"\n{i + 1}. {name}")

        print("Original:", data)
        print("Bubble:  ", bubble_sort(data))
        print("Merge:   ", merge_sort(data))

        # Check correctness without using sorted() as our algorithm.
        print(
            "Test passed:",
            bubble_sort(data) == merge_sort(data) == sorted(data)
        )

        print("Explanation:", explanations[i])

    print("\n=== FINAL INTERPRETATION ===")

    print(
        "Both algorithms sorted the server response times correctly."
    )

    print(
        "Bubble Sort is straightforward for small datasets, "
        "but Merge Sort scales better when many measurements "
        "need to be organized."
    )

    print(
        "The original measurements remain unchanged because "
        "both sorting functions return new lists."
    )


if __name__ == "__main__":
    main()