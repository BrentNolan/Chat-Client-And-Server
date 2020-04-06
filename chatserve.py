#!/bin/python

from socket import *
import sys


def chat(connection_socket, client_name, user_name):
    """
    Initiates a chat session with the client
    The client sends the first messages
    """

    while 1:

        # get all of the characters from the user
        received = connection_socket.recv(501)[0:-1]
        # if we received nothing, print connection closed and close connection
        if received == "":
            print "Connection closed"
            print "Waiting for new connection"
            break
        # print clients name with their message
        print "{}> {}".format(client_name, received)
        # grab input on our side to send to user
        to_send = ""
        while len(to_send) == 0 or len(to_send) > 500:
            to_send = raw_input("{}> ".format(user_name))
            # send it to the client if the message is not \quit
        if to_send == "\quit":
            print "Connection closed"
            print "Waiting for new connection"
            break
        connection_socket.send(to_send)


def hand_shake(connection_socket, user_name):
    """    
    This function exchanges user names with the incoming connection
    """
    # get the client's name
    client_name = connection_socket.recv(1024)
    # send our user name to the client
    connection_socket.send(user_name)
    return client_name


if __name__ == "__main__":
    # Check valid args
    if len(sys.argv) != 2:
        print "You must specify the port number for the server to run"
        exit(1)
    # get port number and create a TCP socket
    server_port = sys.argv[1]
    server_socket = socket(AF_INET, SOCK_STREAM)
    # bind the socket to the port
    server_socket.bind(('', int(server_port)))
    # listen on the port for incoming messages
    server_socket.listen(1)
    # ask user for name, less than 11 characters
    user_name = ""
    while len(user_name) == 0 or len(user_name) > 10:
        user_name = raw_input("Please enter a user name of 10 characters or less: ")
        print "The server is ready to receive incoming messages"
    while 1:
        # loop until sigint from user
        # create a new socket if there is an incoming connection
        connection_socket, address = server_socket.accept()
        # print that we have received a connection
        print "received connection on address {}".format(address)
        # chat with the incoming connection, hand_shake with them first
        chat(connection_socket, hand_shake(connection_socket, user_name), user_name)
        # close the connection when we are done chatting
        connection_socket.close()
