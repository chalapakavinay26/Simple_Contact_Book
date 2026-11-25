def show_menu():
    print("\n=== Simple Contact Book ===")
    print("1. (Add Contact)")
    print("2. (View All Contacts)")
    print("3. (Search Contact)")
    print("4. (Delete Contact)")
    print("5. (Exit)")


def contact_book():
    contacts = {}

    while True:
        show_menu()
        choice = input("enter your option (1-5): ").strip()

        if choice == "1":
            name = input("(Name) enter now: ").strip()
            if not name:
                print("name blank should not stay !\n")
                continue

            phone = input("enter phone number: ").strip()
            email = input("email (Optional): ").strip()

            contacts[name.lower()] = {
                "name": name,
                "phone": phone,
                "email": email
            }
            print(f"'{name}' context save!")

        elif choice == "2":
            if not contacts:
                print("\ncontext book empty.")
            else:
                print("\n--- save context---")
                for idx, data in enumerate(contacts.values(), start=1):
                    email_part = f" | Email: {data['email']}" if data["email"] else ""
                    print(f"{idx}. {data['name']} - {data['phone']}{email_part}")

        elif choice == "3":
            query = input("search names enter now: ").strip().lower()
            matches = [
                data for key, data in contacts.items()
                if query in key
            ]
            if not matches:
                print(f"'{query}' name no context can't find.")
            else:
                print("\n--- find context---")
                for data in matches:
                    email_part = f" | Email: {data['email']}" if data["email"] else ""
                    print(f"- {data['name']}: {data['phone']}{email_part}")

        elif choice == "4":
            name = input("deleted names enter now: ").strip().lower()
            if name in contacts:
                removed = contacts.pop(name)
                print(f"'{removed['name']}' context removed!")
            else:
                print("that name context can't find.")

        elif choice == "5":
            print("program completed.!")
            break

        else:
            print("wrong option! 1 to 5 option enter now.")


if __name__ == "__main__":
    contact_book()
