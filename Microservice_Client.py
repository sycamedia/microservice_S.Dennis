import zmq  

def main():
    
    # Create a ZeroMQ context for handling socket communication
    context = zmq.Context()

    # Create a REQ (request) socket for sending requests to the server
    socket = context.socket(zmq.REQ)  # REQ socket for client-side requests

    # Connect to the server running on localhost at port 5555
    #  '*' may need to be updated to localhost or 127.0.0.1
    #  Port number may be altered to avoid collisions
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