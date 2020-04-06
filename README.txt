Brent Nolan


Running chatserve.py:

1. Give it executable permissions:
chmod +x chatserve.py

2. Run the executable and give a valid, but not likely used port number argument, with the command below:

./chat_server.py <server port>

If it asks for interpreter run with this command:

python chat_server.py <server port>



Compiling and running chatclient.c:

1. Compile chatclient with the command below:
gcc chatclient.c -o chatclient

2.  To run the client type the command below giving the current server ip/address (e.g. which flip the server is on) 
and the port you specified above as arguments:
./chatclient <server ip/address> <server port>

3. Send a message via the chatclient.



Misc:
The first message must be sent on chatclient and not on chatserve..
