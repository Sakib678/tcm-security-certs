Kali Linux is the version of Linux used for this course.

- Kali Linux is specialised for penetration testing and forensic purposes.

- Sudo command allows users with the right privileges to execute commands as a superuser or another user.
- Root is the ultimate user.

- File System Commands:
    * pwd - Displays the current working directory
    * cd - changes the current working directory
   *  mkdir - makes a directory in the current directory
    * rmdir - removes an empty directory
    * man - displays the manual pages for a specific command
    * echo - displays text or variables as output
    * '>'- redirects the output of a command to a file and overwrites the file if it already exists
    * '>>' - redirects the output of a command and appends it to a file
    * rm - deletes files or directories
    * mv - moves or renames files and directories
    * cp - copies files and directories
    * locate - searches for files and directories in a prebuild database
    * updatedb - updated the database used by the locate command so that recent changes are reflected
    * passwd - allows a user to change their password

Users and privileges:

- ls -la "rwx" output refers to file or directory permissions
- read (r) - allows the user to read or view the contents
- write (w) - allows the user to write to a file
- execute (x) - grants the user the permission to execute a file or enter a directory

The 'chmod' command can change the permissions of a file or a directory
- Chmod can use numbers, which are explained below

<img width="757" height="274" alt="image" src="https://github.com/user-attachments/assets/7bcda73a-8eb3-4b65-a483-ecbad74b73a3" />

"sudo - l" - this command displays the commands and permissions that are available to the current user with sudo access. 


Network Commands:

- ip a: This displays the current network interfacesand their ip addresses
- ifconfig: Displays the configuration and status of network interfaces
- iwconfig: Displays the configuration and stats of wireless network interfaces
- ip n: Displays the Neighbour table, also known as the ARP (Address Resolution Protocol) table. ARP resolves IP addresses to their corresponding MAC addresses within a LAN.
- arp -a: Displays the ARP cache, which maps IP addresses to MAC addresses.
- ip r: Displays the routing table, which tontains information about network routes, including destination networks, where our traffic is routing. 
- ping:  sends ICMP echo request to a specified IP address to check network conectivity and measure round-trip time. If there isnt a response, it doesnt mean the device or network is not online, as they may have ICMP requests disabled.

Starting and Stopping Services:

- apache can be used to host files
- sudo service (service) start/stop
- python3 -m http.server 80 (run the module "http.server" on port 80 using python)
- sudo systemctl enable/disable (service name)

Installing and Updating Tools:

- sudo apt update && apt upgrade : This updates the package list so information about available updates can be retrieved. These packages are then upgraded to the latest versions.


