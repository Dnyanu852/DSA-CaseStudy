
from collections import deque


class GamingNetwork:
    def __init__(self):
        # Adjacency list for gamer friendships
        self.friends = {}

        # Store gamers belonging to each team
        self.teams = {}

    # Add a new gamer
    def add_gamer(self, gamer):
        if gamer not in self.friends:
            self.friends[gamer] = set()
            print(gamer, "joined the gaming network!")
        else:
            print("Gamer already exists!")

    # Add friendship between gamers
    def add_friendship(self, gamer1, gamer2):
        if gamer1 not in self.friends or gamer2 not in self.friends:
            print("Both gamers must be registered first!")
            return

        if gamer1 == gamer2:
            print("A gamer cannot be friends with themselves!")
            return

        self.friends[gamer1].add(gamer2)
        self.friends[gamer2].add(gamer1)
        print("Friendship added successfully!")

    # Create a gaming team
    def create_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = set()
            print("Team", team_name, "created successfully!")
        else:
            print("Team already exists!")

    # Add gamer to a team
    def join_team(self, gamer, team_name):
        if gamer not in self.friends:
            print("Gamer not found!")
            return

        if team_name not in self.teams:
            print("Team not found!")
            return

        self.teams[team_name].add(gamer)
        print(gamer, "joined team", team_name)

    # Display all gamers and friends
    def display_network(self):
        print("\n--- Gaming Friends Network ---")

        if not self.friends:
            print("No gamers registered!")
            return

        for gamer in sorted(self.friends):
            print(gamer, "->", sorted(self.friends[gamer]))

    # Display teams and their members
    def display_teams(self):
        print("\n--- Gaming Teams ---")

        if not self.teams:
            print("No teams created!")
            return

        for team in sorted(self.teams):
            print(team, "->", sorted(self.teams[team]))

    # Breadth First Search
    def bfs(self, start):
        if start not in self.friends:
            print("Gamer not found!")
            return

        visited = {start}
        queue = deque([start])

        print("\nBFS Friend Network:")

        while queue:
            gamer = queue.popleft()
            print(gamer, end=" ")

            for friend in sorted(self.friends[gamer]):
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)

        print()

    # Depth First Search
    def dfs(self, start):
        if start not in self.friends:
            print("Gamer not found!")
            return

        visited = set()
        stack = [start]

        print("\nDFS Friend Network:")

        while stack:
            gamer = stack.pop()

            if gamer not in visited:
                visited.add(gamer)
                print(gamer, end=" ")

                for friend in sorted(
                    self.friends[gamer], reverse=True
                ):
                    if friend not in visited:
                        stack.append(friend)

        print()


# Main program
network = GamingNetwork()

while True:
    print("\n===== Online Gaming Friends Network =====")
    print("1. Add Gamer")
    print("2. Add Friendship")
    print("3. Create Team")
    print("4. Join Team")
    print("5. Display Friends Network")
    print("6. Display Teams")
    print("7. BFS Traversal")
    print("8. DFS Traversal")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        gamer = input("Enter gamer name: ").strip()
        if gamer:
            network.add_gamer(gamer)
        else:
            print("Gamer name cannot be empty!")

    elif choice == "2":
        gamer1 = input("Enter first gamer: ").strip()
        gamer2 = input("Enter second gamer: ").strip()
        network.add_friendship(gamer1, gamer2)

    elif choice == "3":
        team = input("Enter team name: ").strip()
        if team:
            network.create_team(team)
        else:
            print("Team name cannot be empty!")

    elif choice == "4":
        gamer = input("Enter gamer name: ").strip()
        team = input("Enter team name: ").strip()
        network.join_team(gamer, team)

    elif choice == "5":
        network.display_network()

    elif choice == "6":
        network.display_teams()

    elif choice == "7":
        start = input("Enter starting gamer: ").strip()
        network.bfs(start)

    elif choice == "8":
        start = input("Enter starting gamer: ").strip()
        network.dfs(start)

    elif choice == "9":
        print("Exiting Gaming Network. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
