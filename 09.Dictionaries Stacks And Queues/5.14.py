import queue

# Initialize variables for customer service
customer_queue = queue.Queue()
ticket_number = 0


def add_customer():
    global ticket_number
    ticket_number += 1
    customer_queue.put(ticket_number)
    print(f"Customer with ticket #{ticket_number} has been added to the queue.")
    return ticket_number


def serve_customer():
    if customer_queue.empty():
        print("No customers in the queue to serve.")
    else:
        next_customer = customer_queue.get()
        print(f"Now serving customer with ticket #{next_customer}.")


while True:
    print("\nCustomer Service Menu:")
    print("1. Add customer to queue")
    print("2. Serve next customer")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        serve_customer()
    elif choice == "3":
        print("Exiting Customer Service System")
        break
    else:
        print("Invalid choice. Please try again.")

