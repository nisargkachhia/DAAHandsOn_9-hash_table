from hash_table import HashTable

def main():
    ht = HashTable()

    while True:
        print("\nHash Table Operations:")
        print("1. Insert a key-value pair")
        print("2. Find a value by key")
        print("3. Delete a key-value pair")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                key = int(input("Enter key (integer): "))
                value = int(input("Enter value (integer): "))
                ht.insert(key, value)
                print(f"Inserted: ({key}, {value})")
            except ValueError:
                print("Invalid input. Please enter integers for both key and value.")

        elif choice == '2':
            try:
                key = int(input("Enter key to find: "))
                result = ht.find(key)
                if result is not None:
                    print(f"Value for key {key}: {result}")
                else:
                    print(f"Key {key} not found.")
            except ValueError:
                print("Invalid input. Please enter an integer for the key.")

        elif choice == '3':
            try:
                key = int(input("Enter key to delete: "))
                if ht.delete(key):
                    print(f"Key {key} deleted successfully.")
                else:
                    print(f"Key {key} not found.")
            except ValueError:
                print("Invalid input. Please enter an integer for the key.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
