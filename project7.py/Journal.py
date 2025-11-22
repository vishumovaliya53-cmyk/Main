from datetime import datetime


class FileData:
    """Manage simple text-based journal."""

    def __init__(self, filename="main.txt"):
        self.filename = filename

    def add_entry(self, entry):
        with open(self.filename, "a") as file:
            now = datetime.now()
            file.write(f"[{now}] {entry}\n")
        print("\nEntry Added Successfully!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
            print("\n--- Journal Entries ---\n")
            print(content)
        except FileNotFoundError:
            print("\nNo Journal Entries found!")

    def search_entry(self):
        keyword = input("Enter keyword to search: ")
        found = False

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if keyword.lower() in line.lower():
                    print(i, "   ", line)
                    found = True

            if not found:
                print("No matching entries found.")

        except FileNotFoundError:
            print("Journal file does not exist.")

    def delete_entries(self):
        confirm = input("Are you sure you want to DELETE all entries? (y/n): ")

        if confirm.lower() == "y":
            open(self.filename, "w").close()
            print("\nAll journal entries deleted!")
        else:
            print("\nCancelled.")
         
jm=FileData("main.txt")

