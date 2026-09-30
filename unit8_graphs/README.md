# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

## Implementation

For this assignment, I created a small IT network using an adjacency list. The graph used devices and services as nodes, including a User PC, Wi-Fi Access Point, Network Switch, Router, Printer, DNS Server, Authentication Server, and File Server. The edges represented direct network connections between those systems.

I implemented BFS with `collections.deque` so the queue followed first-in, first-out order. I marked nodes as visited when they were added to the queue so the same node could not be added multiple times by different neighbors. Starting from the User PC, the traversal moved outward through the network one level at a time. I then added a VPN Gateway connected to the Router and ran BFS again to show how the traversal changed.

I also tested a disconnected network, a graph containing a cycle, and a missing starting node. The disconnected test showed that BFS only visited reachable systems. The cycle test showed why the visited set was necessary, and the missing-node test returned an empty list without crashing.

## How I Ran It

From the project folder, I ran:

`python unit8_graphs/unit8_discussion.py`

The first traversal started at the User PC and visited the network in this order:

User PC, Wi-Fi Access Point, Network Switch, Router, Printer, DNS Server, Authentication Server, File Server

After I added the VPN Gateway to the Router, the new node appeared later in the BFS traversal because it was discovered from the Router.

## Discussion Board Reflection

The biggest thing I learned from this assignment was how the queue controls the way BFS moves through a graph. Using an adjacency list made the network easy to picture because each device stored only the systems directly connected to it. The part that took the most thought was deciding when a node should count as visited. I marked each node as visited when it entered the queue instead of waiting until it was removed. That prevented two different devices from adding the same neighbor before it was processed.

BFS and DFS can both traverse the same graph, but they answer different kinds of questions. BFS uses a FIFO queue and works outward one level at a time, so I would use it when the closest connection matters, such as tracing which network devices are one or two hops away from a user. DFS uses a stack or recursion and follows one path as far as possible before backtracking. That makes DFS more useful when I want to trace one dependency chain deeply, check for cycles, or explore a path before trying alternatives.