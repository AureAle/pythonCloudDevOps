# main.py

from dictionary.dictionary import Dictionary

def main():
    d = Dictionary()

    # Add entries
    d.newentry("Apple", "A fruit that grows on trees.")
    d.newentry("Me", "Myself and I.")
    
    
    # Get meanings
    print(d.look("Apple"))
    
    
    print(d.look("Banana"))
    
    # List all entries
    print(d.list_entries())

if __name__ == "__main__":
    main()
