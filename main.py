from insertion_controller import insert_menu
from console_config import clear_screen, loading_progress_bar

def main():
    clear_screen()
    
    while True:
        print("SSC Automation:")
        print("-------------------")
        print("1. Inspect Data")
        print("2. Data Automation")
        print("3. Exit")
        
        # Get user input
        choice = input("SSC Automation: ")
        if choice == "1":
            clear_screen()
        elif choice == "2":
            # ... (other menu actions)
            # clear_screen()
            insert_menu()  # Call the function from the separate file
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    
    main()