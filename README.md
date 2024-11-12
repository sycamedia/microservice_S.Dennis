# To-Do List Suggestion Microservice


## Overview 

This microservice provides motivational suggestions and task examples for different categories in a to-do list application. The client application can send category requests, and the microservice will respond with a relevant suggestion and an example task.

## Features

* Returns a motivational suggestion and task example for a requested category.
* Supports categories such as "Physical Health", "Work", "Personal Development", and more.
* Uses a REQ-REP (Request-Reply) pattern with ZeroMQ to communicate between the client and server.

## Requirements

* Python 3.8+
* ZeroMQ (zmq)


## Request Data From Microservice

To make a request, the client application will need to connect to the microservice via a REQ (request) socket. Once connected, they can send a string message containing the category they want suggestions for.

* The client code initializes a zmq.REQ socket to send requests.
* The client connects to the server at tcp://localhost:5555.
* The client sends a category request (e.g., "Physical Health").
* The socket.recv_string() function pauses the client’s execution until a response is received from the server.

![Programmatically REQUEST Data](images/request-data-from-microservice.png)

![Programmatically REQUEST Data](images/send-data-to-client.png)

## Recieve Data From Microservice

* The microservice code initializes a zmq.REP socket to receive requests from clients.
* It binds the socket to tcp://localhost:5555, meaning it listens for incoming connections on port 5555 from any IP address or localhost.
* After sending the request, the client waits for the microservice to respond.
* The microservice, upon receiving the request, processes it and prepares a relevant response (e.g., a motivational suggestion related to the provided category).
* The microservice sends the response back to the client using socket.send_string().

![Programmatically RECIEVE Data](images/recieve-request-from-client.png)

![Programmatically REQUEST Data](images/recieve-data-from-microservice.png)
