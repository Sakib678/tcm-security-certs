# Linux100 - TCM Security

This folder contains my notes and a bash script created whilst completing the **Linux 100: Fundamentals** course by TCM Security
It can be found at the following link: https://academy.tcm-sec.com/p/linux-fundamentals

## About the Course

Linux 100 is a short course offered by TCM Security that introduces key Linux concepts that are essential to know.
It covers:
- File System Navigation
- User and permission management
- Bash Scripting
- Updating and upgrading packages
- System services and networking


## About the script
The script pings addresses from .1 to .254 when given a partial IP address. It filters successful responses and returns those IP addresses to the screen.
However, this script is only a basic script. Many firewalls block ICMP requests so it may be unreliable. 

Example Usage:
./ipsweep.sh 192.172.1

