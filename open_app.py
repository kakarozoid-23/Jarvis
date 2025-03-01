import pyautogui
import time

def open_app_by_search(app_name):

    """
    Opens an application by searching in the Windows search bar.

    :param app_name: Name of the application to search and open.
    """
    try:
        pyautogui.press("win")  # Open the Start menu
        time.sleep(1)  # Wait for the search bar
        
        pyautogui.write(app_name, interval=0.1)  # Type app name
        time.sleep(1)  # Wait for search results
        
        pyautogui.press("enter")  # Open the app
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"Error opening {app_name}: {e}")

# Continuous loop to listen for user input
while True:
    app_name = input("Enter the app name to open (or 'exit' to stop): ").strip()
    if app_name.lower() == "exit":
        print("Exiting...")
        break  # Stop the loop
    open_app_by_search(app_name)
