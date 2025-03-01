import webbrowser

def search_google():
    while True:
        query = input("Enter the search query(To exit write 'exit'): ")
        if query.lower() == "exit":
            print("Exiting...")
            break
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

# Example usage
search_google()
