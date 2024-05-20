# Python Socket Server with Pickle Serialization

## Overview

This project implements a multi-threaded TCP server in Python that handles client connections and uses `pickle` for serializing and deserializing data. The server can gracefully handle shutdown signals.

## Features

- Multi-threaded to handle multiple client connections simultaneously.
- Uses `pickle` for serialization and deserialization of Python objects.
- Handles shutdown signals (SIGINT and SIGTERM) to allow graceful shutdown.
- Communicates with clients using a fixed-length header to indicate message length.

## Requirements

- Python 3.x

## Setup and Installation

1. **Clone the repository**:
   ```sh
   git clone (https://github.com/IR02/pythonSocket.git)
   cd pythonSocket
2. **Run the server**:
   ```sh
   python server.py
3. **Run the clients**:
   ```sh
   python client.py
4. **On another command line**
    ```sh
   python client.py

## How to Stop the server
   Press `Ctrl+C` in the terminal where the server is running. This triggers the signal handler, which shuts down the server gracefully.

## Usage
   **Server**
   The server listens for incoming connections on a specified port and handles each client in a separate thread. It serializes responses using pickle and can shut down gracefully on receiving termination signals.

   **Client**
   The client connects to the server and sends dictionary messages serialized with pickle. It also handles the server's response by deserializing it.

## Conclusion
This project demonstrates how to implement a multi-threaded TCP server in Python using pickle for serializing and deserializing data, and how to handle graceful shutdowns. This setup can be extended to handle more complex communication protocols and larger data structures.
