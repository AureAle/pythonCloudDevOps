class Dictionary:
    def __init__(self):
        # Initialize an empty dictionary to store entries and meanings
        self.entries = {}

    def newentry(self, entry, meaning):
        """Add an entry with its meaning to the dictionary."""
        if entry in self.entries:
            print(f"'{entry}' already exists. Overwriting its meaning.")
        self.entries[entry] = meaning
        # print(f"Added: {entry} -> {meaning}")

    def look(self, entry):
        """Get the meaning of a given entry."""
        return self.entries.get(entry, f"Can't find {entry} in the dictionary.")

    def list_entries(self):
        """List all entries in the dictionary."""
        if not self.entries:
            return "The dictionary is empty."
        return"List of words:\n" + "\n".join(f"{entry}: {meaning}" for entry, meaning in self.entries.items())
