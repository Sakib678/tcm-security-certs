# SSH Brute Force Script

**Purpose:**  
Attempts to brute force SSH credentials using a password list.  
**Intended for educational use and lab testing only.**

**Author:** Sakib Arif | Date: 13-08-2025

---

## Requirements
- Python 3.x  
- [pwntools](https://pypi.org/project/pwntools/)  
- [paramiko](https://pypi.org/project/paramiko/)  

Install dependencies:
```bash
pip install pwntools paramiko
```

---

## Usage
1. Set the target host and username in the script:
```python
host = "127.0.0.1"
username = "notroot"
```

2. Provide a password list in `best110.txt`.

3. Run the script:
```bash
python3 ssh_bruteforce.py
```

**Output:**
- `[>] Valid password found: 'password'` → correct password discovered  
- `[X] Invalid password!` → authentication failed  

---

## Notes
- `attempts` counts how many passwords have been tried.  
- Ensure an SSH server is running on the target host:
```bash
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

---

## Ethical Disclaimer
**For learning and lab use only. Unauthorized attacks on live systems are illegal and unethical.**
