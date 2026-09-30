"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # A missing start node cannot be traversed safely.
    if start not in graph:
        return []

    # BFS uses a queue because FIFO order keeps closer nodes ahead of
    # nodes discovered later. That creates the level-by-level traversal.
    queue = deque([start])

    # Mark a node when it enters the queue so another neighbor cannot
    # add the same node again before it is processed.
    visited = {start}

    # Store the exact order in which nodes are processed.
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        # Add each unvisited neighbor to the back of the queue.
        # BFS checks nearby nodes first, while DFS would follow one path
        # as deeply as possible before backtracking.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # This graph represents a small IT network.
    # Each key is a device or service, and each value lists its direct
    # network connections. Those relationships are the graph's edges.
    network_graph = {
        "User PC": ["Wi-Fi Access Point"],
        "Wi-Fi Access Point": ["User PC", "Network Switch"],
        "Network Switch": ["Wi-Fi Access Point", "Router", "Printer"],
        "Router": ["Network Switch", "DNS Server", "Authentication Server"],
        "Printer": ["Network Switch"],
        "DNS Server": ["Router"],
        "Authentication Server": ["Router", "File Server"],
        "File Server": ["Authentication Server"]
    }

    print("IT network adjacency list:")
    for node, neighbors in network_graph.items():
        print(f"{node} -> {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start_node = "User PC"
    first_traversal = bfs(network_graph, start_node)

    print("Starting node:", start_node)
    print("BFS traversal:", first_traversal)
    print("Level 0: User PC")
    print("Level 1: Wi-Fi Access Point")
    print("Level 2: Network Switch")
    print("Level 3: Router, Printer")
    print("Level 4: DNS Server, Authentication Server")
    print("Level 5: File Server")
    print("BFS checks the closest network connections before moving farther away.")

    # Add a VPN Gateway and connect it to the Router in both directions.
    network_graph["VPN Gateway"] = ["Router"]
    network_graph["Router"].append("VPN Gateway")

    updated_traversal = bfs(network_graph, start_node)

    print("\nAdded VPN Gateway connected to Router.")
    print("Updated BFS traversal:", updated_traversal)
    print("VPN Gateway appears after the Router because it is discovered from that node.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: A disconnected network has two separate components.
    disconnected_graph = {
        "Laptop": ["Switch A"],
        "Switch A": ["Laptop"],
        "Backup Server": ["Switch B"],
        "Switch B": ["Backup Server"]
    }

    print("\nDisconnected network:")
    print("BFS from Laptop:", bfs(disconnected_graph, "Laptop"))
    print("Backup Server and Switch B are not visited because no path connects them to Laptop.")

    # Edge case 2: The graph contains a cycle.
    # The visited set prevents the traversal from going around the loop forever.
    cyclic_graph = {
        "PC": ["Switch"],
        "Switch": ["Router"],
        "Router": ["PC"]
    }

    print("\nNetwork cycle:")
    print("BFS from PC:", bfs(cyclic_graph, "PC"))
    print("Each node is visited once even though the connections form a loop.")

    # Edge case 3: A missing starting node is handled without crashing.
    print("\nMissing start node:")
    print("BFS from Unknown Device:", bfs(network_graph, "Unknown Device"))
    print("The function returns an empty list because the starting node does not exist.")


if __name__ == "__main__":
    main()
