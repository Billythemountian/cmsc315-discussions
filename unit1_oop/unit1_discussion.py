"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class NetworkDevice:
    # Class variable shared by all NetworkDevice objects
    device_type = "Network Device"

    def __init__(self, hostname, ip_address):
        # Instance variables belong to each individual object
        self.hostname = hostname
        self.ip_address = ip_address

    def display_info(self):
        # Display basic information about the device
        print(f"Hostname: {self.hostname}, IP Address: {self.ip_address}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Router(NetworkDevice):
    # Class variable shared by all Router objects
    role = "Router"

    def __init__(self, hostname, ip_address, model):
        # Use the parent constructor for hostname and IP address
        super().__init__(hostname, ip_address)

        # New instance variables for Router objects
        self.model = model
        self.networks = []

    def add_network(self, network):
        # Add a network to the router's list
        # The inner list gives us nested mutable data for the copying demo
        self.networks.append([network])

    def display_info(self):
        # Override the parent method with additional Router information
        print(
            f"Hostname: {self.hostname}, IP Address: {self.ip_address}, "
            f"Model: {self.model}, Networks: {self.networks}"
        )

    # Student-created extension
    def network_count(self):
        # Return the number of networks stored by the router
        return len(self.networks)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two separate Router objects
    router1 = Router("RTR-01", "192.168.1.1", "R100")
    router2 = Router("RTR-02", "192.168.2.1", "R200")

    # Access the same class variable in two different ways
    print("Through class:", Router.role)
    print("Through object:", router1.role)

    # Add an attribute only to router1
    router1.location = "Server Room"

    # __dict__ shows attributes stored in each object's namespace
    print("Router 1 namespace:", router1.__dict__)
    print("Router 2 namespace:", router2.__dict__)

    # Display the namespace belonging to the Router class
    print("Router class namespace:", Router.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create a Router with a nested list inside networks
    router = Router("RTR-03", "10.0.0.1", "R300")
    router.add_network("LAN")

    # Shallow copy still shares nested mutable data
    shallow_router = copy(router)

    # Deep copy creates a completely separate copy of nested data
    deep_router = deepcopy(router)

    # Change the nested list in the original object
    router.networks[0].append("Active")

    # The shallow copy changes because it shares the nested list.
    # The deep copy does not change because its nested list is separate.
    print("Original:", router.networks)
    print("Shallow copy:", shallow_router.networks)
    print("Deep copy:", deep_router.networks)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    device = NetworkDevice("PC-01", "192.168.1.10")
    device.display_info()

    # Create and test a child object
    router = Router("RTR-MAIN", "192.168.1.1", "R500")
    router.add_network("Home")
    router.display_info()

    # Test the student-created extension
    print("Network count:", router.network_count())

    # Test an empty network list as an edge case
    empty_router = Router("RTR-EMPTY", "192.168.1.2", "R100")
    empty_router.display_info()
    print("Empty router network count:", empty_router.network_count())

    # Run the namespace and copying demonstrations
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()