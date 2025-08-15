# SHA256 Password Cracking Script

**Purpose:**\
Attempts to brute-force a SHA256 hash using a password list. Intended for lab testing and educational use only.

**Author:** Sakib Arif | Date: 15-08-2025

---

## Requirements

- Python 3.x
- [pwntools](https://pypi.org/project/pwntools/) (for dynamic progress display)

Install dependencies:

```bash
pip install pwntools
```

---

## Usage

Run the script from the command line:

```bash
python3 sha256_cracker.py <sha256sum>
```

### Arguments

- `<sha256sum>`: The target SHA256 hash you want to crack.

### Output

- Each attempt dynamically updates the terminal line with the format:

```
[attempt_number] password == password_hash
```

- If the password is found, the script prints:

```
Password hash found after X attempts! <password> hashes to <hash>
```

- If the password is not found after all attempts, the script prints:

```
Password hash not found!
```

---

## Wordlist

- Default: `rockyou.txt` (should be in the same folder as the script).
- Can be replaced with any text file containing potential passwords.

---

## Notes

- Uses `latin-1` encoding to handle special characters.
- Large wordlists may take time to process.
- Relies on `pwntools.log.progress` for dynamic single-line display.

---

## Ethical Disclaimer

**For educational purposes only. Unauthorized attacks on live systems are illegal and unethical.**

