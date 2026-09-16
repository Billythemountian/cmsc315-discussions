"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary for help desk tickets.
    tickets = {}

    # The ticket number is the key and the ticket status is the value.
    tickets["INC1001"] = "Open"
    tickets["INC1002"] = "In Progress"
    tickets["INC1003"] = "Waiting on User"
    tickets["INC1004"] = "Open"
    tickets["INC1005"] = "Resolved"

    # Python dictionaries use hashing to quickly find a value by its key.
    print("Help desk tickets:", tickets)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Use the ticket number to quickly find its current status.
    print("INC1001 status:", tickets["INC1001"])
    print("INC1003 status:", tickets["INC1003"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", tickets)

    # Assigning a new value to the same key updates the ticket.
    tickets["INC1001"] = "Resolved"

    print("After update:", tickets)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", tickets)

    # Remove a resolved ticket from the dictionary.
    del tickets["INC1005"]

    print("After deletion:", tickets)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Look up a ticket that does not exist.
    # get() returns the message instead of causing an error.
    missing_ticket = tickets.get("INC9999", "Ticket not found")
    print("Missing ticket lookup:", missing_ticket)

    # Edge case 2: Try to remove a ticket that does not exist.
    # pop() with a default value prevents an error.
    removed_ticket = tickets.pop("INC9999", "Ticket not found")
    print("Missing ticket removal:", removed_ticket)


if __name__ == "__main__":
    main()