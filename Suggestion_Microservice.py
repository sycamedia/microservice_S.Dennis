import zmq
import os
import json
import random

def load_suggestions():
    """Load existing suggestion data from a JSON file"""
    
    # Check if the 'suggestions.json' file exists before attempting to open it
    if os.path.exists('suggestions.json'):
        with open('suggestions.json', 'r', encoding='utf-8') as file:
            try:
                
                # Load and return the JSON data as a dictionary
                return json.load(file)  
            
            except json.JSONDecodeError:
                
                # Handle case where the JSON file is empty or corrupted
                print("Suggestion bank is empty.")
                return {}  
    
    # Return an empty dictionary if the file doesn't exist
    return {}  
    
def get_suggestion(category, data):
    """
    Fetch a random suggestion and example task for the given category from the loaded data
    """
    
    # Check if the category exists in the loaded data
    if category in data:
        suggestions = data[category]["suggestions"]
        example_tasks = data[category]["example_tasks"]
        
        # Randomly select a suggestion and an example task from the category
        suggestion = random.choice(list(suggestions.values()))  
        task = random.choice(list(example_tasks.values()))  
        return suggestion, task
    
    # Return an error message if the category is not found
    else:
        return "Category not found", None

def main():
    """
    Program that recieves a to do list, and returns a suggestion and example
    task that cooresponds with the category.
    """
    
    context = zmq.Context()
    
    # REP socket for server-side replies
    socket = context.socket(zmq.REP)  
    
    # Bind to port 5555 to listen for incoming connections
    socket.bind("tcp://*:5555")  
    print("Suggestion server is awaiting messages...")

    # Load suggestions from the JSON file
    suggestions = load_suggestions()
    
    while True:
        
        # Wait for a category request from the client
        category = socket.recv_string()
        
        # Prepare the suggestion or error message based on the category request
        if category in suggestions:
            suggestion, task = get_suggestion(category, suggestions)
            response = f'Suggestion: {suggestion}\nExample Task: {task}'
        else:
            response = "Invalid category."
        
        # Send the response back to the client
        socket.send_string(response)
        print(f'Message ({response}) has been sent successfully.')

if __name__ == "__main__":
    main()