# Python101 - TCM Security

This folder contains my notes and Python scripts created whilst completing the **Python 101 for Hackers** course by TCM Security.

It can be found at the following link: https://academy.tcm-sec.com/p/python-101-for-hackers

---

## About the Course

Python 101 for Hackers is an introductory course offered by TCM Security that teaches the fundamentals of Python with a focus on practical applications in cybersecurity.

It covers:
- Python basics: variables, data types, loops, and functions  
- File handling and string manipulation  
- Working with libraries such as `requests`   
- Error handling and input validation  
- Writing scripts for automation and penetration testing tasks  

---

## About the Scripts

This repository includes several Python scripts built during the course.  
Each script is for **educational purposes and lab testing only**.

| Script | Purpose |
|--------|---------|
| **SSH Brute Force Script** | Attempts to brute force SSH credentials using a password list. |
| **SHA256 Password Cracking Script** | Attempts to brute-force a SHA256 hash using a password list. |
| **Login Brute-Force Script** | Attempts to brute-force login credentials against a target web application using a username list and password wordlist.  |
| **Blind SQL Injection Hash Extractor** | Automates Boolean-based Blind SQL Injection to extract password hashes from a deliberately vulnerable web application.  |


My notes are also available. 
---

## Example Usage
Navigate into a script folder and run it:
```bash
cd ssh-bruteforce
python3 ssh_bruteforce.py
