# Main code for the project

# Initialize an empty list to store contacts
contacts = []

# Import necessary functions from the contacts module
from contacts import (
    add_contact, list_contacts, edit_contact, 
    mark_contact_as_favorite, list_favorite_contacts, delete_contact
)

# Initialize the option variable to None
option = None

# Start a loop that will run until the user chooses to exit (option 7)
while option != 7:

    # Print the menu options
    print('\n')
    print("Contacts Menu\n")
    print("1 - Add New Contact")
    print("2 - View All Contacts")
    print("3 - Edit a Contact")
    print("4 - Mark/Unmark as Favorite")
    print("5 - Show Favorite Contacts")
    print("6 - Delete a Contact")
    print("7 - Exit")

    # Try to get the user's option and handle invalid input
    try:
        option = int(input("\nEnter your option number: "))
    except ValueError:
        # If the input is not a valid integer, print an error message and restart the loop
        print("Invalid input! Please select a number between 1 and 7.")
        continue  # Restart the loop without crashing

    # Execute the corresponding function based on the user's option
    if option == 1:
        add_contact(contacts)
    elif option == 2:
        list_contacts(contacts)
    elif option == 3:
        edit_contact(contacts)
    elif option == 4:
        mark_contact_as_favorite(contacts)
    elif option == 5:
        list_favorite_contacts(contacts)
    elif option == 6:
        delete_contact(contacts)
    elif option == 7:
        print("Exiting program. Goodbye!")
    else:
        print("Invalid option! Please select a number between 1 and 7.")