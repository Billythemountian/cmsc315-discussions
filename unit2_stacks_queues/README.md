# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Completed Work

I used an IT help-desk scenario for this assignment. The queue stored incoming support tickets, while the stack stored completed help-desk actions.

I used a Python list for the stack and deque for the queue. I also tested empty stack and queue operations and single-item cases.

As more tickets or actions were added, both structures needed more memory because they had more items to store.

## Reflection

For this assignment, I worked with stacks and queues using a simple IT help desk example. Using actual support tickets made it easier for me to see the difference between FIFO and LIFO than using random numbers. The queue stored incoming tickets, so the oldest ticket was handled first. The stack stored completed actions, so the newest action was removed first.

The biggest thing I learned was how much the order of adding and removing items matters. I also got more practice using a Python list and deque. The main challenge was keeping track of which end of each structure I needed to use. Once I ran the program and saw the order of the output, it made a lot more sense.

I also tested empty stacks and queues so pop, peek, dequeue, and front returned None instead of causing problems. In a real help desk, a queue makes sense for incoming tickets, while a stack could be useful for tracking recent actions that may need to be reviewed or undone.