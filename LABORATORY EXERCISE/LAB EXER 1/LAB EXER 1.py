tickets = [] 
def add_ticket(incident_id, bot, description):
    """Add a new incident ticket to the list (linear insertion at the end)."""

    for ticket in tickets:
        if ticket["incident_id"] == incident_id:
            print(f"[!] Ticket {incident_id} already exists. Ticket not added.\n")
            return
    tickets.append({
        "incident_id": incident_id,
        "bot": bot,
        "description": description
    })
    print(f"[+] Ticket {incident_id} added successfully.\n")


def display_tickets():
    """Display all active incident tickets by traversing the list."""
    print("\n" + "=" * 70)
    print("ACTIVE INCIDENT TICKETS")
    print("=" * 70)
    if not tickets:
        print("No active incident tickets.")
    else:
        print(f"{'Incident ID':<15}{'Bot':<20}{'Short Description':<35}")
        print("-" * 70)
        for ticket in tickets:
            print(f"{ticket['incident_id']:<15}{ticket['bot']:<20}{ticket['description']:<35}")
    print("=" * 70 + "\n")


def search_ticket(incident_id):
    """Search for a specific ticket using its Incident ID (linear search)."""
    for index, ticket in enumerate(tickets):
        if ticket["incident_id"] == incident_id:
            print(f"\n[FOUND] Ticket located at position {index}:")
            print(f"    Incident ID : {ticket['incident_id']}")
            print(f"    Bot         : {ticket['bot']}")
            print(f"    Description : {ticket['description']}\n")
            return ticket
    print(f"\n[NOT FOUND] No ticket with Incident ID '{incident_id}' exists.\n")
    return None


def remove_ticket(incident_id):
    """Remove a resolved incident ticket from the list (linear search + delete)."""
    for index, ticket in enumerate(tickets):
        if ticket["incident_id"] == incident_id:
            removed = tickets.pop(index)
            print(f"[-] Ticket {removed['incident_id']} ({removed['bot']}) "
                  f"marked resolved and removed.\n")
            return True
    print(f"[!] Cannot remove. No ticket with Incident ID '{incident_id}' found.\n")
    return False


def count_active_tickets():
    """Display the total number of active incident tickets."""
    total = len(tickets)
    print(f"\n[COUNT] Total active incident tickets: {total}\n")
    return total


def load_sample_data():
    sample_tickets = [
        ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
        ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
        ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
        ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
        ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
        ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
        ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
        ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
        ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
        ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
    ]
    print("\nLoading 10 sample incident tickets...\n")
    for incident_id, bot, description in sample_tickets:
        add_ticket(incident_id, bot, description)


def run_demo():
    print("#" * 70)
    print("DEMONSTRATION: IT AUTOMATION INCIDENT TICKET MANAGER")
    print("#" * 70)

    # 1. ADD - load the 10 sample tickets
    print("\n--- 1. ADDING TICKETS ---")
    load_sample_data()

    # 2. DISPLAY - show all active tickets
    print("--- 2. DISPLAYING ALL ACTIVE TICKETS ---")
    display_tickets()

    # 3. SEARCH - look up an existing ticket and a non-existing one
    print("--- 3. SEARCHING FOR A TICKET ---")
    search_ticket("INC1392944")   # existing ticket
    search_ticket("INC0000000")   # non-existing ticket (demonstrates NOT FOUND)

    # 4. REMOVE - resolve/remove a ticket
    print("--- 4. REMOVING A RESOLVED TICKET ---")
    remove_ticket("INC1392940")   # BOT-Email ticket has been resolved

    # Display again to show the updated list
    print("--- DISPLAY AFTER REMOVAL ---")
    display_tickets()

    # 5. COUNT - show total active tickets remaining
    print("--- 5. COUNTING ACTIVE TICKETS ---")
    count_active_tickets()

    print("#" * 70)
    print("END OF DEMONSTRATION")
    print("#" * 70 + "\n")


def print_menu():
    print("\n" + "-" * 45)
    print(" IT AUTOMATION INCIDENT TICKET MANAGER")
    print("-" * 45)
    print(" [1] Add a new incident ticket")
    print(" [2] Display all active incident tickets")
    print(" [3] Search for an incident ticket")
    print(" [4] Remove a resolved incident ticket")
    print(" [5] Display total number of active tickets")
    print(" [6] Load sample data (10 tickets)")
    print(" [0] Exit")
    print("-" * 45)


def main_menu():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            incident_id = input("Enter Incident ID: ").strip()
            bot = input("Enter Bot name: ").strip()
            description = input("Enter Short Description: ").strip()
            add_ticket(incident_id, bot, description)

        elif choice == "2":
            display_tickets()

        elif choice == "3":
            incident_id = input("Enter Incident ID to search: ").strip()
            search_ticket(incident_id)

        elif choice == "4":
            incident_id = input("Enter Incident ID to remove: ").strip()
            remove_ticket(incident_id)

        elif choice == "5":
            count_active_tickets()

        elif choice == "6":
            load_sample_data()

        elif choice == "0":
            print("Exiting IT Automation Incident Ticket Manager. Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please select a valid menu option.\n")


if __name__ == "__main__":
    
    run_demo()

    
    main_menu()