# SSH Brute Force Script

**Purpose:**  
Attempts to brute force SSH credentials using a password list.  
**Intended for educational use and lab testing only.**

**Author:** Sakib Arif | Date: 13-08-2025

---

## Requirements
- Python 3 
- [pwntools](https://pypi.org/project/pwntools/)  
- [paramiko](https://pypi.org/project/paramiko/)  

Install dependencies:
```bash
pip install pwntools paramiko
```

---

## Usage
Run the script from the command line:

```bash
python3 ssh_brute.py -H <host> -U <username> -W <wordlist>
```

## Arguments
- `-H, --host` : Target host IP

- `-U, --username` : Target SSH username

- `-W, --wordlist` : Path to password list file

- `-h, --help` : Show this help message

### Example
```bash
python3 ssh_brute.py -H 127.0.0.1 -U notroot -W best110.txt
```
**Output:**
- `[>] Valid password found: 'password'` → correct password discovered  
- `[X] Invalid password!` → authentication failed  

---

## Notes
- Ensure an SSH server is running on the target host:
```bash
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

---

## Ethical Disclaimer
**For learning and lab use only. Unauthorized attacks on live systems are illegal and unethical.**
