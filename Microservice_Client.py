"""
Cal Ikai
ikaic@oregonstate.edu
11/13/2024

Client For Suggestions Microservice

This program implements the client-side logic to communicate with a server using ZeroMQ.
It uses the Request-Reply pattern to send requests and receive responses from a
remote microservice. The client sends data requests and processes responses to provide
real-time functionality for the end-user.
"""

import zmq


def main():

    # Create a ZeroMQ context for handling socket communication
    context = zmq.Context()

    # Create a REQ (request) socket for sending requests to the server
    socket = context.socket(zmq.REQ)  # REQ socket for client-side requests

    # Connect to server running on localhost at port 5555
    socket.connect("tcp://localhost:5555")

    # Prompt the user for a category input
    category_request = input("Please enter a category:\n")

    # Send the category input to the server as a string
    socket.send_string(category_request)

    # Wait for the server to send a response, and assign response to 'suggestion'
    suggestion = socket.recv_string()

    # Print suggestion and task example
    print(suggestion)


if __name__ == "__main__":
    main()
