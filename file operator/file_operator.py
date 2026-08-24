import datetime as datetime
import os

class JournalManager:

    def Add_journal(self):
            write_journal = input("Enter your journal entry: ")
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("journal.txt", "a") as file:
                file.write(f"[{date_str}]\n{write_journal}\n\n")
                print("Entry added successfully!")
    def view_journal(self):
        try:
            with open("journal.txt", "r") as file:
                data = (file.read())
                if data.strip():
                    print("Ouput (If a match is found):")
                    print("Your Journal Entries:")
                    print("--------------------------------------")
                    print(data)
                else:
                    print("Output (If no match is found):")
                    print("No journal entries found. Start by adding a new entry!")
        except FileExistsError as e:
            print("Error",e)
        except FileNotFoundError as e:
            print("Error", e)
        except PermissionError as e:
            print("Error", e)
        
    def Search_journal(self):
        Keyword = input("Enter a keyword or data to search: ")
        try:
            with open("journal.txt", "r") as file:
                data = (file.read())
                if not data.strip():
                    print("Output (If no match is found):")
                    print("No journal entries found. Start by adding a new entry!")

                entries = data.strip().split("\n\n")
                found_any = False

                print("Output (If a match is found):")
                print("Matching Entries:")
                print("-------------------------------------")
                for entry in entries:
                    if Keyword.lower() in entry.lower():
                        print(entry)
                        print("-"*40)
                        found_any = True

                if not found_any:
                    print("Output (If no match is found):")
                    print(f"No entries were found for the Keyword: {Keyword}")

        except FileExistsError as e:
            print("Error",e)
        except FileNotFoundError as e:
            print("Error",e)
        except PermissionError as e:
            print("Error",e)
    
    def Delete_journal(self):
        Delete_option = input("Are you sure you want to delete all entries? (yes/no): ")
        if Delete_option == "yes":
            try:
                if os.path.exists("journal.txt"):
                    os.remove("journal.txt")
                    print("Output (If the file is deleted successfully):")
                    print("All journal entries have been deleted.")
                else:
                    print("Output (If the file does not exist):")
                    print("No journal entries to delete.")
            except Exception as e:
                print("Error",e)
        else:
            print("Deletion canceled.")

    def run(self):
        print("Welcome to personal Journal Manager!")
        while True:
            print("\nPlease select an option:")

            print(
                f"\n1. Add a New Entry"
                f"\n2. View All Entries"
                f"\n3. Search for an Entry"
                f"\n4. Delete All Entries"
                f"\n5. Exit"
            )

            choice = int(input("\nUser Input:"))

            match choice:
                case 1:
                    self.Add_journal()
                case 2:
                    self.view_journal()
                case 3:
                    self.Search_journal()
                case 4:
                    self.Delete_journal()
                case 5:
                    print("Thank you for using Personal Journal Manager. Goodbye!")
                    break
                case _:
                    print("Invaild option. Please select a vaild option from from the menu.")

system = JournalManager()

system.run()