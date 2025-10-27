class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)
        
        if self.data[index] is None:
            self.data[index] = new_node
            return

        current = self.data[index]
        while current:
            if current.key == key:
                current.value.number = number
                return
            if current.next is None:
                break
            current = current.next
        
        current.next = new_node  
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if not current:
                print(f"Index {i}: Empty")
            else:
                contacts = []
                while current:
                    contacts.append(str(current.value))
                    current = current.next
                print(f"Index {i}: - " + " - ".join(contacts))


# ---------- TESTING ----------
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()
    print("\n--- Adding Contacts ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n--- Search Test ---")
    contact = table.search("John")
    print("Search result:", contact)

    print("\n--- Collision & Duplicate Test ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  
    table.print_table()

    print("\n--- Duplicate Key Test ---")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\n--- Missing Contact Search ---")
    print(table.search("Chris"))  


    '''
    Design Memo
    For this assignment we were working with hash tables for a small contact management system, 
    with this program it will be able to store the contacts, as well as adding, updating, and 
    searching them in the smoothest way possible. For this assignment using a hash table is the 
    best way going about it because it will allow faster look ups, updates, and it will convert 
    each of the contacts names into a numeric index so that it cam be found and stores immediately 
    and directly. There are many different methods used, such as hash_function(key), insert(key,value), 
    search(key), and print_table(). Now in the hash table there are collisions and these are handled 
    through separate chaining. With this each of the index’s in the table hold the head of the 
    linked lists, and if there are many in the same index then it will be stored in that list. 
    This is so that there is no data lost. A lot of people actually choose hash tables over a 
    list or even a tree when the goal is quick access by key. So with this assignment I was able to 
    learn more about how hashing works, and learn how collision handling works while using separate chaining. 
    '''