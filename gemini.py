import google.generativeai as genai
import google.api_core.client_options as client_options

# Set up the API key
genai.configure(api_key="AIzaSyBz-kF-1yOLBjKPKzGmWiDvpg3Yvt4ptho")

# Use HTTP instead of gRPC
genai.client_options = client_options.ClientOptions(api_endpoint="https://generativelanguage.googleapis.com/")

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Example usage
if __name__ == "__main__":
    user_input = input("Ask Jarvis: ")
    response = get_gemini_response(user_input)
    print("Jarvis:", response)

