
from collections import deque


class SocialNetwork:
    def __init__(self):
        # Graph represented using an adjacency list
        self.graph = {}

    # Add a new user
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()
            print(user, "added successfully!")
        else:
            print("User already exists!")

    # Add friendship between two users
    def add_friendship(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist first!")
            return

        if user1 == user2:
            print("A user cannot be friends with themselves!")
            return

        self.graph[user1].add(user2)
        self.graph[user2].add(user1)
        print("Friendship added successfully!")

    # Display the social network
    def display_network(self):
        print("\n--- Social Network ---")
        for user in sorted(self.graph):
            friends = sorted(self.graph[user])
            print(user, "->", friends)

    # Breadth First Search (BFS)
    def bfs(self, start):
        if start not in self.graph:
            print("User not found!")
            return

        visited = set()
        queue = deque([start])
        visited.add(start)

        print("\nBFS Traversal:")

        while queue:
            user = queue.popleft()
            print(user, end=" ")

            for friend in sorted(self.graph[user]):
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)

        print()

    # Depth First Search (DFS)
    def dfs(self, start):
        if start not in self.graph:
            print("User not found!")
            return

        visited = set()
        stack = [start]

        print("\nDFS Traversal:")

        while stack:
            user = stack.pop()

            if user not in visited:
                visited.add(user)
                print(user, end=" ")

                for friend in sorted(self.graph[user], reverse=True):
                    if friend not in visited:
                        stack.append(friend)

        print()


# Main program
network = SocialNetwork()

while True:
    print("\n===== Social Network Analysis =====")
    print("1. Add User")
    print("2. Add Friendship")
    print("3. Display Network")
    print("4. BFS Traversal")
    print("5. DFS Traversal")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user = input("Enter user name: ").strip()
        if user:
            network.add_user(user)
        else:
            print("User name cannot be empty!")

    elif choice == "2":
        user1 = input("Enter first user name: ").strip()
        user2 = input("Enter second user name: ").strip()
        network.add_friendship(user1, user2)

    elif choice == "3":
        network.display_network()

    elif choice == "4":
        start = input("Enter starting user for BFS: ").strip()
        network.bfs(start)

    elif choice == "5":
        start = input("Enter starting user for DFS: ").strip()
        network.dfs(start)

    elif choice == "6":
        print("Exiting Social Network Analysis.")
        break

    else:
        print("Invalid choice! Please try again.")
