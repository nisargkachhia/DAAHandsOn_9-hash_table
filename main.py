from hash_table import HashTable

def main():
    ht = HashTable()

    # Insert some values
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(30, 300)
    ht.insert(40, 400)

    # Find a value
    print("Find key 20:", ht.find(20))  # Output: 200

    # Delete a value
    ht.delete(20)
    print("Find key 20 after deletion:", ht.find(20))  # Output: None

    # Dynamic resizing (will trigger resize)
    ht.insert(50, 500)
    ht.insert(60, 600)
    ht.insert(70, 700)
    
    # Display final values
    print("Find key 50:", ht.find(50))  # Output: 500
    print("Find key 30:", ht.find(30))  # Output: 300

if __name__ == "__main__":
    main()
