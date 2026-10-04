  
# STACK

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def display(self):
        print("\n----- STACK (Recent Actions) -----")

        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            for item in reversed(self.stack):
                print("|", item, "|")


# QUEUE

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):

        if len(self.queue) == 0:
            return None

        return self.queue.pop(0)

    def display(self):

        print("\n----- NORMAL ORDER QUEUE -----")

        if len(self.queue) == 0:
            print("Queue is empty")
        else:

            print("FRONT → ", end="")

            for order in self.queue:
                print(
                    f"[Order {order['id']}]",
                    end=" → "
                )

            print("REAR")



# PRIORITY QUEUE


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def get_priority(self, order_type):

        if order_type == "Emergency":
            return 1

        elif order_type == "Express":
            return 2

        else:
            return 3

    def enqueue(self, order):

        order["priority"] = self.get_priority(
            order["type"]
        )

        self.queue.append(order)

        # Sort according to priority
        self.queue.sort(
            key=lambda x: x["priority"]
        )

    def dequeue(self):

        if len(self.queue) == 0:
            return None

        return self.queue.pop(0)

    def display(self):

        print("\n----- PRIORITY QUEUE -----")

        if len(self.queue) == 0:
            print("Priority Queue is empty")

        else:

            for order in self.queue:

                print(
                    f"Order {order['id']} | "
                    f"{order['customer']} | "
                    f"{order['food']} | "
                    f"{order['type']} | "
                    f"Priority: {order['priority']}"
                )



# LINKED LIST


class Node:

    def __init__(self, order):

        self.order = order

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None


    # INSERT
    def insert(self, order):

        new_node = Node(order)

        if self.head is None:

            self.head = new_node

            return

        current = self.head

        while current.next is not None:

            current = current.next

        current.next = new_node


    # TRAVERSE
    def display(self):

        print("\n----- LINKED LIST -----")

        if self.head is None:

            print("Linked List is empty")

            return

        current = self.head

        while current is not None:

            order = current.order

            print(
                f"[Order {order['id']} | "
                f"{order['customer']} | "
                f"{order['food']}]"
                ,
                end=" → "
            )

            current = current.next

        print("NULL")


    # SEARCH
    def search(self, order_id):

        current = self.head

        while current is not None:

            if current.order["id"] == order_id:

                return current.order

            current = current.next

        return None


    # DELETE
    def delete(self, order_id):

        if self.head is None:

            return False


        if self.head.order["id"] == order_id:

            self.head = self.head.next

            return True


        current = self.head

        while (
            current.next is not None
            and
            current.next.order["id"] != order_id
        ):

            current = current.next


        if current.next is not None:

            current.next = current.next.next

            return True


        return False



# 5. CIRCULAR QUEUE - DELIVERY RIDERS


class CircularQueue:

    def __init__(self):

        self.riders = [
            "Rider 1",
            "Rider 2",
            "Rider 3",
            "Rider 4"
        ]

        self.index = 0


    def assign_rider(self):

        rider = self.riders[self.index]

        self.index = (
            self.index + 1
        ) % len(self.riders)

        return rider



# MAIN PROGRAM


stack = Stack()

normal_queue = Queue()

priority_queue = PriorityQueue()

linked_list = LinkedList()

rider_queue = CircularQueue()


order_id = 100



# PLACE ORDER
  

def place_order():

    global order_id

    print("\n========== PLACE ORDER ==========")

    customer = input(
        "Enter customer name: "
    )

    print("\nFood Menu")

    print("1. Pizza")
    print("2. Burger")
    print("3. Biryani")
    print("4. Sandwich")
    print("5. Pasta")

    choice = input(
        "Select food: "
    )


    foods = {
        "1": "Pizza",
        "2": "Burger",
        "3": "Biryani",
        "4": "Sandwich",
        "5": "Pasta"
    }


    food = foods.get(
        choice,
        "Pizza"
    )


    print("\nOrder Type")

    print("1. Normal")
    print("2. Express")
    print("3. Emergency")

    type_choice = input(
        "Select order type: "
    )


    types = {
        "1": "Normal",
        "2": "Express",
        "3": "Emergency"
    }


    order_type = types.get(
        type_choice,
        "Normal"
    )


    order_id += 1


    order = {

        "id": order_id,

        "customer": customer,

        "food": food,

        "type": order_type
    }


    # Linked List
    linked_list.insert(order)


    # Queue
    if order_type == "Normal":

        normal_queue.enqueue(order)

    # Priority Queue
    else:

        priority_queue.enqueue(order)


    # Stack
    stack.push(
        f"Order {order_id} placed"
    )


    print("\n✅ ORDER PLACED SUCCESSFULLY")

    print(
        f"Order ID : {order_id}"
    )

    print(
        f"Customer : {customer}"
    )

    print(
        f"Food     : {food}"
    )

    print(
        f"Type     : {order_type}"
    )



# PROCESS NORMAL ORDER


def process_order():

    order = normal_queue.dequeue()


    if order is None:

        print(
            "\n❌ No normal orders available."
        )

        return


    rider = rider_queue.assign_rider()


    print("\n========== ORDER PROCESSING ==========")

    print(
        f"Order ID : {order['id']}"
    )

    print(
        f"Customer : {order['customer']}"
    )

    print(
        f"Food     : {order['food']}"
    )

    print(
        f"Rider    : {rider}"
    )


    stack.push(
        f"Order {order['id']} processed"
    )



# PROCESS PRIORITY ORDER


def process_priority_order():

    order = priority_queue.dequeue()


    if order is None:

        print(
            "\n❌ No priority orders available."
        )

        return


    rider = rider_queue.assign_rider()


    print("\n========== PRIORITY ORDER ==========")

    print(
        f"Order ID : {order['id']}"
    )

    print(
        f"Customer : {order['customer']}"
    )

    print(
        f"Food     : {order['food']}"
    )

    print(
        f"Type     : {order['type']}"
    )

    print(
        f"Priority : {order['priority']}"
    )

    print(
        f"Rider    : {rider}"
    )


    stack.push(
        f"Priority Order {order['id']} processed"
    )



# SEARCH ORDER


def search_order():

    try:

        order_id_search = int(
            input(
                "\nEnter Order ID to search: "
            )
        )

    except ValueError:

        print("❌ Invalid ID")

        return


    order = linked_list.search(
        order_id_search
    )


    if order is None:

        print(
            "\n❌ Order not found."
        )

    else:

        print("\n✅ ORDER FOUND")

        print(
            f"Order ID : {order['id']}"
        )

        print(
            f"Customer : {order['customer']}"
        )

        print(
            f"Food     : {order['food']}"
        )

        print(
            f"Type     : {order['type']}"
        )



# DELETE ORDER


def delete_order():

    try:

        order_id_delete = int(
            input(
                "\nEnter Order ID to delete: "
            )
        )

    except ValueError:

        print("❌ Invalid ID")

        return


    result = linked_list.delete(
        order_id_delete
    )


    if result:

        print(
            "\n✅ Order deleted successfully."
        )

        stack.push(
            f"Order {order_id_delete} deleted"
        )

    else:

        print(
            "\n❌ Order not found."
        )



# UNDO LAST ACTION


def undo_action():

    action = stack.pop()


    if action is None:

        print(
            "\n❌ Nothing to undo."
        )

    else:

        print(
            "\n↩️ Undo Action:"
        )

        print(action)



# DISPLAY ALL


def display_all():

    linked_list.display()

    normal_queue.display()

    priority_queue.display()

    stack.display()



# MAIN MENU


while True:

    print("\n")
    print("=" * 60)
    print("     🍔 ONLINE FOOD ORDER MANAGEMENT SYSTEM")
    print("=" * 60)

    print("\n1. Place New Order")

    print("2. Process Normal Order")

    print("3. Process Priority Order")

    print("4. Search Order")

    print("5. Delete Order")

    print("6. Display All Data Structures")

    print("7. Undo Last Action")

    print("8. Assign Delivery Rider")

    print("9. Exit")


    choice = input(
        "\nEnter your choice: "
    )


    if choice == "1":

        place_order()


    elif choice == "2":

        process_order()


    elif choice == "3":

        process_priority_order()


    elif choice == "4":

        search_order()


    elif choice == "5":

        delete_order()


    elif choice == "6":

        display_all()


    elif choice == "7":

        undo_action()


    elif choice == "8":

        rider = rider_queue.assign_rider()

        print(
            f"\n🛵 Assigned Delivery Rider: {rider}"
        )


    elif choice == "9":

        print(
            "\nThank you for using the system! 🍔"
        )

        break


    else:

        print(
            "\n❌ Invalid choice. Try again."
        )