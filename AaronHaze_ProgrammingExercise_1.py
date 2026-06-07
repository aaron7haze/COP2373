# Programming Exercise 1
# This program pre-sells a limited number of cinema tickets.
# A maximum of 20 tickets can be sold, and each buyer may purchase up to 4.
# The program repeatedly asks the user how many tickets they want,
# validates the request, updates the remaining ticket count,
# and displays the total number of buyers when tickets run out.

MAX_TICKETS = 10        # Total tickets available
MAX_PER_BUYER = 4       # Maximum tickets one buyer can purchase


def get_ticket_request():
    """
    Ask the user how many tickets they want and validate the input.
    Returns:
        int: number of tickets requested (1–4)
    """
    while True:
        try:
            # Input from user
            num = int(input("How many tickets are you purchasing (1–4)? "))

            # Validate range
            if 1 <= num <= MAX_PER_BUYER:
                return num
            else:
                print("You can only buy between 1 and 4 tickets.")

        except ValueError:
            # Handles non-numeric input
            print("Please enter a valid number.")


def sell_tickets():
    """
    Main loop that sells tickets until all 20 are gone.
    Tracks remaining tickets and counts total buyers.
    """
    remaining = MAX_TICKETS   # Accumulator for tickets left
    customers = 0                # Accumulator for number of customers

    # Loop until all tickets are sold
    while remaining > 0:
        print(f"\nTickets remaining: {remaining}")

        # Get a valid ticket request
        request = get_ticket_request()

        # Ensure request does not exceed remaining tickets
        if request > remaining:
            print(f"Only {remaining} tickets left. You cannot buy {request}.")
            continue

        # Process purchase
        remaining -= request
        customers += 1

        print(f"Purchase successful. {remaining} tickets remain.")

    # All tickets sold
    print("\nAll tickets sold!")
    print(f"Total customers: {customers}")


# Start the program
sell_tickets()
