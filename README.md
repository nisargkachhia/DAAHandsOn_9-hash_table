# DAAHandsOn_9-hash_table

# Hash Table Implementation in Python

## Overview

This project implements a hash table data structure using Python, featuring:
- A custom hash function using both multiplication and division methods.
- Collision resolution through chaining using a doubly linked list.
- Dynamic resizing of the hash table (doubling and halving based on occupancy).

## Project Structure

N:/UTA/1st SEM/DAA/DAAHandsOn_9-hash_table/
│
├── hash_table.py          # Contains the HashTable and DoublyLinkedListNode classes
├── doubly_linked_list.py  # Contains the DoublyLinkedList class
└── main.py                # Contains the main program logic to use the hash table (with user input)

## Requirements

- Python 3.10.5

## Usage

1. **Clone the repository** or download the files:
    ```bash
    git clone <repository_url>
    cd hash_table_project
    ```

2. **Run the program**:
    ```bash
    python main.py
    ```

3. **Follow the on-screen instructions** to interact with the hash table:
   - Insert a key-value pair
   - Find a value by key
   - Delete a key-value pair
   - Exit the program

## Features

- **Insertion**: Insert key-value pairs into the hash table. If the key already exists, the value is updated.
- **Finding**: Retrieve the value associated with a given key.
- **Deletion**: Remove a key-value pair from the hash table.
- **Dynamic Resizing**: The hash table automatically resizes when it becomes full or is sparsely populated (less than 1/4 of its capacity).

## Implementation Details

- **Hash Function**: The hash function combines multiplication and division methods to calculate the index for storing key-value pairs.
- **Chaining with Doubly Linked List**: Each index in the hash table points to a doubly linked list, allowing multiple entries to be stored at the same index in case of collisions.
- **Dynamic Growth and Shrinking**: The hash table grows by doubling its size when full and shrinks by halving its size when the load factor drops below 1/4.

## Example Usage

1. **Inserting a Key-Value Pair**:
Enter your choice (1-4): 1
Enter key (integer): 10
Enter value (integer): 100
Inserted: (10, 100)

2. **Finding a Value by Key**:
Enter your choice (1-4): 2
Enter key to find: 10
Value for key 10: 100

4. **Deleting a Key-Value Pair**:
Enter your choice (1-4): 3
Enter key to delete: 10
Key 10 deleted successfully.

5. **Exiting the Program**:
Enter your choice (1-4): 4
Exiting program.
