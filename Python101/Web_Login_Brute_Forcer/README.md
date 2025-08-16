# Login Brute-Force Script

**Purpose:**\
Attempts to brute-force login credentials against a target web
application using a username list and password wordlist. Intended for
lab testing and educational use only.

**Author:** Sakib Arif \| Date: 16-08-2025

------------------------------------------------------------------------

## Requirements

-   Python 3

Install dependencies:

``` bash
pip install requests
```

------------------------------------------------------------------------

## Usage

Run the script from the command line:

``` bash
python3 brute_force.py
```

### Configuration

Inside the script, you can set:

-   `target`: The target URL (e.g., `http://127.0.0.1:5000`)
-   `usernames`: A list of usernames to attempt
-   `passwords`: Path to the password wordlist file
-   `needle`: A keyword in the HTTP response indicating a successful
    login (e.g., `"Welcome back"`)

------------------------------------------------------------------------

## Wordlist

-   Default: `best110.txt` (must exist in the same folder as the
    script).
-   Can be replaced with any custom password list.

------------------------------------------------------------------------

## Notes

-   Encodes passwords as UTF-8 before sending.
-   Works against basic login forms expecting POST requests with
    `username` and `password` fields.
-   Modify `needle` according to the web app's success message.

------------------------------------------------------------------------

## Ethical Disclaimer

**For educational purposes only. Unauthorized brute-force attacks on
live systems are illegal and unethical. Always use in controlled
environments with explicit permission.**
