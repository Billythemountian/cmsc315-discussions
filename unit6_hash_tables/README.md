# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Inserted key-value pairs
- Retrieved values efficiently
- Updated existing values
- Removed entries
- Learned basic hashing concepts

## Requirements

1. Created and populated a dictionary.
2. Demonstrated lookup operations.
3. Demonstrated update operations.
4. Demonstrated delete operations.
5. Tested edge cases.
6. Created a real-world scenario.

## Design Approach

I created a simple IT help desk ticket tracker using a Python dictionary. Each ticket number was used as the key, and the current ticket status was stored as the value.

I added five tickets, looked up two existing tickets, updated one ticket from Open to Resolved, and removed a completed ticket. I also tested two missing ticket numbers to make sure the program could handle them without stopping with an error.

## Discussion Board Reflection

For this assignment, I created a simple IT help desk ticket tracker using a Python dictionary. Each ticket number was used as the key, and the current ticket status was stored as the value. I practiced adding new tickets, looking up existing tickets, updating a ticket status, and removing tickets that were no longer needed.

The main challenge was handling ticket numbers that did not exist. Instead of allowing the program to stop with an error, I used methods such as get() and pop() with default values so missing tickets could be handled safely.

I learned that Python dictionaries use hash tables to store and retrieve information efficiently. A hash function uses the key to determine where the value should be stored. A collision happens when two different keys map to the same location, which can require extra work to locate the correct value. With a good hash function and few collisions, dictionary lookups are normally O(1) on average. This makes hash tables useful for help desk systems where technicians need to find ticket information quickly.