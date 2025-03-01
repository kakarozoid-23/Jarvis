import google.generativeai as genai
import google.api_core.client_options as client_options
import pyautogui
import time
import webbrowser
import re  # Import the regular expression module

def open_app_by_search(app_name):
    """Opens an application by searching in the Windows search bar."""
    try:
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write(app_name, interval=0.1)
        time.sleep(1)
        pyautogui.press("enter")
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"Error opening {app_name}: {e}")

def ask_jarvis(prompt):
    """Asks Jarvis (Gemini) a question and returns the response."""
    genai.configure(api_key="AIzaSyBz-kF-1yOLBjKPKzGmWiDvpg3Yvt4ptho")
    genai.client_options = client_options.ClientOptions(api_endpoint="https://generativelanguage.googleapis.com/")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def search_google(query):
    """Searches Google for the given query."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def main():
    """Main function to handle user input and call appropriate functions."""
    while True:
        user_input = input("Enter command (e.g., open Chrome, ask Jarvis what is the capital of France, search Google for weather): ").lower()

        if "open" in user_input:
            # Extract app name using regular expression
            match = re.search(r"open (.*)", user_input)
            if match:
                app_name = match.group(1).strip()
                open_app_by_search(app_name)
            else:
                print("Invalid open command.")

        elif "ask jarvis" in user_input:
            # Extract the query for Jarvis
            match = re.search(r"ask jarvis (.*)", user_input)
            if match:
                jarvis_query = match.group(1).strip()
                response = ask_jarvis(jarvis_query)
                print("Jarvis:", response)
            else:
                print("Invalid ask Jarvis command.")

        elif "search google" in user_input:
            # Extract the search query
            match = re.search(r"search google (.*)", user_input)
            if match:
                search_query = match.group(1).strip()
                search_google(search_query)
            else:
                print("Invalid search Google command.")

        elif user_input == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Try 'open app', 'ask Jarvis', or 'search Google'.")

if __name__ == "__main__":
    main()