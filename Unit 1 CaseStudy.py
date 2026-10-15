
# Financial Data Sorting Using Quick Sort

def partition(data, low, high):
    pivot = data[high]["amount"]
    i = low - 1

    for j in range(low, high):
        if data[j]["amount"] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def quick_sort(data, low, high):
    if low < high:
        pivot_index = partition(data, low, high)

        quick_sort(data, low, pivot_index - 1)
        quick_sort(data, pivot_index + 1, high)


def display_transactions(data):
    print("\n--- Financial Transaction Records ---")
    print("{:<12} {:<20} {:>12}".format(
        "ID", "Description", "Amount"
    ))
    print("-" * 46)

    for transaction in data:
        print("{:<12} {:<20} {:>12.2f}".format(
            transaction["id"],
            transaction["description"],
            transaction["amount"]
        ))


# Main program
transactions = []

n = int(input("Enter number of financial transactions: "))

for i in range(n):
    print("\nEnter details for transaction", i + 1)

    transaction_id = input("Transaction ID: ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    transactions.append({
        "id": transaction_id,
        "description": description,
        "amount": amount
    })

print("\nBefore Sorting:")
display_transactions(transactions)

quick_sort(transactions, 0, len(transactions) - 1)

print("\nAfter Sorting (Ascending Amount):")
display_transactions(transactions)

# Display in descending order
transactions.reverse()

print("\nAfter Sorting (Descending Amount):")
display_transactions(transactions)
