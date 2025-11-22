def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Add Item: ")
            shopping_list.append(item)
            print(f"added {item} to the list.")
            
        elif choice == "2":
            item = input("Enter the item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed")

        elif choice == "3":
            print("Current Shopping List")
            if len(shopping_list) == 0:
                print("Your list is empty")
            else:
                for i in shopping_list:
                    print(i)

        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()