"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Start at the root and let the recursive helper find
        # where the asset ID belongs.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position means the new asset ID belongs here.
        if node is None:
            return Node(value)

        # Smaller asset IDs go left and larger asset IDs go right.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Equal IDs are ignored so duplicate assets are not added.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST follows only one branch after each comparison.
        # In a balanced tree, this keeps search near O(log n)
        # instead of checking every item like a linear search.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching an empty position means the ID was not found.
        if node is None:
            return False

        # The current node matches the asset ID.
        if value == node.value:
            return True

        # Smaller IDs are searched on the left.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Larger IDs are searched on the right.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # In-order visits left, current, then right.
        # Since smaller IDs are on the left and larger IDs are
        # on the right, the asset IDs are returned in sorted order.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== IT ASSET INVENTORY ===")

    # Build a BST containing numeric asset IDs for IT equipment.
    asset_tree = BST()

    asset_ids = [
        500, 250, 750, 125, 375,
        625, 875, 300, 425
    ]

    # These IDs create both left and right branches.
    # Each comparison sends an ID down only one side of the tree.
    for asset_id in asset_ids:
        asset_tree.insert(asset_id)

    print("Asset IDs inserted:", asset_ids)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Left-current-right traversal returns the asset IDs
    # from smallest to largest.
    print("Asset IDs in sorted order:", asset_tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # These asset IDs exist and should return True.
    print("Search for asset 375:", asset_tree.search(375))
    print("Search for asset 875:", asset_tree.search(875))

    # These IDs were never inserted and should return False.
    print("Search for asset 200:", asset_tree.search(200))
    print("Search for asset 900:", asset_tree.search(900))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # An empty inventory returns False instead of causing an error.
    empty_tree = BST()
    print("Search empty inventory for asset 500:",
          empty_tree.search(500))
    print("Empty inventory traversal:", empty_tree.inorder())

    # Duplicate asset IDs are ignored, so the tree stays unchanged.
    before_duplicate = asset_tree.inorder()
    asset_tree.insert(375)

    print(
        "Duplicate asset 375 changed inventory:",
        asset_tree.inorder() != before_duplicate
    )

    # A tree containing only one asset still searches normally.
    single_tree = BST()
    single_tree.insert(111)

    print(
        "Single-asset inventory contains 111:",
        single_tree.search(111)
    )
    print(
        "Single-asset inventory traversal:",
        single_tree.inorder()
    )

    # ===============================
    # INSERTION ORDER COMPARISON
    # ===============================

    print("\n=== INSERTION ORDER MATTERS ===")

    # Sequential asset IDs all travel to the right. This produces
    # a skewed tree that behaves more like a linked list.
    sequential_tree = BST()
    sequential_ids = [100, 200, 300, 400, 500, 600, 700]

    for asset_id in sequential_ids:
        sequential_tree.insert(asset_id)

    print("Sequential asset IDs:", sequential_ids)
    print(
        "Sequential tree traversal:",
        sequential_tree.inorder()
    )

    print(
        "Sequential insertion creates a right-skewed tree. "
        "Search can degrade from O(log n) to O(n)."
    )


if __name__ == "__main__":
    main()