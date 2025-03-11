# Functions for managing contacts

def add_contact(contacts):
    # Prompt user for contact details
    name = input('\nInput your contact name: ')
    telephone = input('\nInput your contact telephone number: ')
    email = input('\nInput your contact email address: ')

    # Create a new contact dictionary
    contact = {'contact': name, 'telephone': telephone, 'email': email, 'favorite': False}

    # Add the new contact to the contacts list
    contacts.append(contact)

    print(f'\n✅ Contact "{name}" added successfully! 🎉')

    input("\nPress Enter to return to the menu...")

def list_contacts(contacts, mode=1):
    # Display the list of contacts
    print('\n📌 Contact List')

    for index, contact in enumerate(contacts, start=1):
        status_favorite = '★' if contact['favorite'] else ''
        name = contact['contact']
        telephone = contact['telephone']
        email = contact['email']

        print(f"{index}. [ {status_favorite} ] {name:<20} | 📞 {telephone:<15} | ✉️  {email}")
    
    if mode == 1:
        input("\nPress Enter to return to the menu...")

def edit_contact(contacts):
    # List contacts without the "Press Enter..." prompt
    list_contacts(contacts, 2)

    # Prompt user for the index of the contact to edit
    index_edit = input('\n Enter the index of the contact you want to edit: ')
    try:
        index_edit = int(index_edit) - 1  # Adjust index for zero-based list
    except ValueError:
        print("Invalid input! Please enter a valid contact index.")
        return contacts

    if index_edit < 0 or index_edit >= len(contacts):
        print(f'There is no contact registered with the index: {index_edit + 1}')
    else:
        contact = contacts[index_edit]
        
        # Show current contact details
        print(f"\nCurrent details of {contact['contact']}:")
        print(f"Name: {contact['contact']}")
        print(f"Telephone: {contact['telephone']}")
        print(f"Email: {contact['email']}")

        # Ask user which attribute to edit
        print("\nWhich attribute would you like to update?")
        print("1 - Name")
        print("2 - Telephone")
        print("3 - Email")
        print("4 - Cancel")

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            new_name = input('\nEnter new name: ')
            contact['contact'] = new_name
            print(f'\n✅ Name updated to {new_name}! 🎉')
        elif choice == '2':
            new_telephone = input('\nEnter new telephone number: ')
            contact['telephone'] = new_telephone
            print(f'\n✅ Telephone updated to {new_telephone}! 🎉')
        elif choice == '3':
            new_email = input('\nEnter new email address: ')
            contact['email'] = new_email
            print(f'\n✅ Email updated to {new_email}! 🎉')
        elif choice == '4':
            print("\nNo changes were made.")
        else:
            print("\nInvalid option. No changes were made.")

    input("\nPress Enter to return to the menu...")

def mark_contact_as_favorite(contacts):
    # List contacts without the "Press Enter..." prompt
    list_contacts(contacts, 2)

    # Prompt user for the index of the contact to mark/unmark as favorite
    index_edit = input('\nEnter the index of the contact you want to mark/unmark as favorite: ')
    try:
        index_edit = int(index_edit) - 1  # Adjust index for zero-based list
    except ValueError:
        print("Invalid input! Please enter a valid contact index.")
        return contacts

    if index_edit < 0 or index_edit >= len(contacts):
        print(f'There is no contact registered with the index: {index_edit + 1}')
    else:
        contact = contacts[index_edit]

        # Toggle the favorite status
        if contact['favorite']:
            contact['favorite'] = False  # Unmark as favorite
            status = "removed from"
        else:
            contact['favorite'] = True  # Mark as favorite
            status = "marked as"

        print(f'\nContact "{contact["contact"]}" has been {status} favorite.')

        input("\nPress Enter to return to the menu...")

    return contacts

def list_favorite_contacts(contacts):
    # Display the list of favorite contacts
    print('\n📌 Favorite Contacts')

    favorites = [contact for contact in contacts if contact['favorite']]
    
    if not favorites:
        print("No favorite contacts found.")
    else:
        for index, contact in enumerate(favorites, start=1):
            name = contact['contact']
            telephone = contact['telephone']
            email = contact['email']

            print(f"{index}. ★ {name} | 📞 {telephone} | ✉️ {email}")

    input("\nPress Enter to return to the menu...")

def delete_contact(contacts):
    # List contacts without the "Press Enter..." prompt
    list_contacts(contacts, 2)

    # Prompt user for the index of the contact to delete
    index_delete = input('\nEnter the index of the contact you want to delete: ')

    try:
        index_delete = int(index_delete) - 1  # Adjust index for zero-based list
    except ValueError:
        print("Invalid input! Please enter a valid contact index.")
        return contacts

    if index_delete < 0 or index_delete >= len(contacts):
        print(f'There is no contact registered with the index: {index_delete + 1}')
    else:
        # Get the contact to delete
        contact = contacts[index_delete]

        # Remove the contact from the list
        contacts.remove(contact)

        print(f'Contact "{contact["contact"]}" has been removed from the agenda.')

        input("\nPress Enter to return to the menu...")

    return contacts
