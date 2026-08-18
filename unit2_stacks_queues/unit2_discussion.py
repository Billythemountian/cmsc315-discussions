"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        # A list works fine for keeping track of the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Add to the end so the newest item comes out first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # Nothing to remove if the stack is empty.
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Check the newest item without removing it.
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # deque makes it easy to work from both ends.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # New tickets go to the back of the line.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Nothing to remove if the queue is empty.
        if self.is_empty():
            return None

        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Check the first ticket without removing it.
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        return len(self.items) == 0


def main():
    print("=== IT HELP DESK: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK: COMPLETED HELP DESK ACTIONS ===")

    actions = Stack()

    completed_actions = [
        "Reset Maya's password",
        "Reconnected front office printer",
        "Restored VPN access for Jordan",
        "Installed accounting software"
    ]

    # Add each completed job to the history.
    for action in completed_actions:
        actions.push(action)
        print(f"Added to history: {action}")

    # This should show the last job that was added.
    print(f"\nMost recent action: {actions.peek()}")

    # The newest action should come back out first.
    print("\nActions come back out newest first:")

    while not actions.is_empty():
        print(f"Removed: {actions.pop()}")

    # See what happens when there is nothing left.
    print(f"\nPop from empty stack: {actions.pop()}")
    print(f"Peek at empty stack: {actions.peek()}")

    # Quick test with only one item.
    one_action = Stack()
    one_action.push("Unlock one user account")

    print(f"\nSingle item removed: {one_action.pop()}")
    print(f"Stack empty afterward: {one_action.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE: INCOMING HELP DESK TICKETS ===")

    tickets = Queue()

    incoming_tickets = [
        "Password reset - Maya",
        "Printer offline - Front Office",
        "VPN connection issue - Jordan",
        "Install accounting software - Finance"
    ]

    # Add new tickets to the back of the queue.
    for ticket in incoming_tickets:
        tickets.enqueue(ticket)
        print(f"New ticket: {ticket}")

    # This should still be the first ticket that came in.
    print(f"\nNext ticket to work: {tickets.front()}")

    # Tickets should be handled in the order they came in.
    print("\nHandling tickets oldest first:")

    while not tickets.is_empty():
        print(f"Processing: {tickets.dequeue()}")

    # See what happens when there are no tickets left.
    print(f"\nDequeue from empty queue: {tickets.dequeue()}")
    print(f"Front of empty queue: {tickets.front()}")

    # Quick test with only one ticket.
    one_ticket = Queue()
    one_ticket.enqueue("Email not syncing - Sam")

    print(f"\nSingle ticket removed: {one_ticket.dequeue()}")
    print(f"Queue empty afterward: {one_ticket.is_empty()}")


if __name__ == "__main__":
    main()