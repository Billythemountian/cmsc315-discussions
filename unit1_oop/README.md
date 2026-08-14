# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation

I used a `NetworkDevice` parent class and a `Router` child class. The router inherited the hostname and IP address from `NetworkDevice`, then added its own model and network list.

I showed how class and instance namespaces work by creating two router objects, accessing the class variable in different ways, and adding a location to only one router. I also used `__dict__` to show what was stored in each object and in the class.

For the copying section, I created a router with nested list data and made both a shallow copy and a deep copy. After changing the original nested list, the shallow copy changed with it, while the deep copy stayed separate.

For my extra feature, I added a `network_count()` method that returned how many networks were stored in the router.

I also tested a router with no networks assigned to make sure the program handled an empty list correctly. The router displayed an empty network list and returned a network count of 0.

A setup like this could be used as the starting point for a simple network inventory program that keeps track of routers and the networks assigned to them.