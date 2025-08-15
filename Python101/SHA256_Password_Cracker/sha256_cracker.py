from pwn import *  # Importing libaries
import sys


# Check that exactly one argument (the SHA256 hash) is provided
if len(sys.argv) != 2:
	print("Invalid arguments!")
	print(">> {} <sha256sum>".format(sys.argv[0]))
	exit() #exit if the wrong number of arguments 

# The target SHA256 hash to crack
wanted_hash=sys.argv[1]

# Path to the password list file
password_file = "rockyou.txt"

# Counter to track the number of password attempts
attempts = 0


# Initialising the dynamic progress display
with log.progress("Attempting  to crack {}!".format(wanted_hash)) as p:
	with open(password_file, "r", encoding ='latin-1') as password_list: #Opening the wordlist file
		for password in password_list: # A for loop to iterate over every password in the list
			password = password.strip("\n").encode('latin-1') #Clean password up
			password_hash = sha256sumhex(password) #Calculate the SHA256 hash of the current password
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash)) #Update the dynamic status line in the terminal
			if password_hash == wanted_hash: # if statement to check if the generated hash matches the target hash
				p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash ))
				exit() # Displays the found password and exits
			attempts += 1 # Increments the number of attempts counter
		p.failure("Password hash not found!") # If all passwords are tried and none match, print the failrue statement