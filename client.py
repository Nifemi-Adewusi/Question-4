
import socket

IP_ADDRESS = 'localhost'
PORT = 9090

cs = socket.socket(family=socket.AF_INET, type= socket.SOCK_STREAM)
cs.connect((IP_ADDRESS, PORT))
msg_to_server = "I need your assistance as follows: I want to know weekday of my birthday and zodiac sign of my birthday"
cs.send(msg_to_server.encode("ascii"))

msg_from_server = cs.recv(1024).decode()
print(msg_from_server)

birthdayDetails = input("Enter Birthday year month date: ")
cs.send(birthdayDetails.encode("ascii"))

msg = cs.recv(1024).decode()
print(msg)