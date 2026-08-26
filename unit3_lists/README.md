# Unit 3 Discussion: List Operations

## Overview

This assignment examined insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

Complete all TODO sections:

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Completed Work

I used an IT asset inventory scenario for this assignment. The list stored devices such as firewalls, switches, servers, routers, access points, and workstations.

I tested insertion and deletion at the beginning, middle, and end of the inventory. I also used a linear search to find existing and missing devices.

For edge cases, I tested an invalid deletion index and an attempt to delete from an empty inventory. Both returned None instead of causing an error.

## Reflection

For this assignment, I worked with Python list operations using a small IT asset inventory. Using actual network devices made the operations easier for me to follow than using random numbers. I inserted devices at the beginning, middle, and end of the list, removed devices from different positions, and used a linear search to locate a specific device.

The biggest thing I learned was how changing one position can affect the rest of the list. When an item was inserted, the items after it shifted to make room. Removing an item caused the remaining items to shift as well. The main challenge was keeping track of the inventory after several operations. Running the program after each section helped me verify that the devices were still in the positions I expected.

I also tested invalid and empty-list operations so the program returned None instead of failing. In a real IT environment, a list could be used to organize devices, software assets, or other inventory that needs to be added, removed, and searched regularly.