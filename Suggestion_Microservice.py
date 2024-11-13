"""
Carl Ikai
ikaic@oregonstate.edu
11/13/2024

Microservice Module for ZeroMQ Communication

This program implements the server-side logic for a microservice that responds to requests
from a client using ZeroMQ. It employs the Request-Reply pattern, where it listens for
incoming client requests, processes them, and sends back the appropriate responses.
"""


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

    # ZeroMQ format based on Flores, L. (2024, June 11). Introduction to ZeroMQ.
    # Oregon State University. Licensed under Creative Commons Attribution-NonCommercial 4.0 License.

    context = zmq.Context()

    # REP socket for server-side replies
    socket = context.socket(zmq.REP)

    # Bind to port 5555 to listen for request from client
    socket.bind("tcp://localhost:5555")
    print("Suggestion server is awaiting messages...")

    # Load suggestions from the JSON file
    suggestions = load_suggestions()

    while True:

        # Wait for a category request from the client, and assign request to 'category'
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
