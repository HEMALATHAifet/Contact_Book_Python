import os

CONTACT_FILE = "contacts.txt"

# ---------- Load & Save Contacts ----------
def load_contacts():
    """Load contacts from a text file into a dictionary."""
    contacts = {}
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    name, phone, email = line.split(",")
                    contacts[name] = {"phone": phone, "email": email}
    return contacts

def save_contacts(contacts):
    """Save contacts from dictionary to a text file."""
    with open(CONTACT_FILE, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

# ---------- Contact Operations ----------
def add_contact(contacts):
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip().lower()
    if name in contacts:
        print("⚠️ Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("✅ Contact added successfully!")
    save_contacts(contacts)

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n📒 Contact List:")
        for name, info in contacts.items():
            print(f"- {name}: {info['phone']} | {info['email']}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip().title()
    if name in contacts:
        info = contacts[name]
        print(f"🔍 {name} → Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("❌ Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")

# ---------- Main Menu ----------
def main():
    contacts = load_contacts()

    while True:
        print("\n===== 📞 CONTACT BOOK MENU =====")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
