# pythonSocket
Python Socket Server with Pickle Serialization
Overview
This project implements a multi-threaded TCP server in Python that handles client connections and uses pickle for serializing and deserializing data. The server can gracefully handle shutdown signals.

Features
Multi-threaded to handle multiple client connections simultaneously.
Uses pickle for serialization and deserialization of Python objects.
Handles shutdown signals (SIGINT and SIGTERM) to allow graceful shutdown.
Communicates with clients using a fixed-length header to indicate message length.
Requirements
Python 3.x
