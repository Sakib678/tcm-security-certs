# Python 101 for Hackers - Notes

## Python 2 vs Python 3
- Python 2 code will mostly not run in Python 3.  
- Python 2 is now **EOL** (end of life).  
- An **interpreter** executes code line by line. You can use it for quick testing, but it’s not efficient for larger programs.  

**Tip:** When making a script in Linux, add this line at the top so the OS knows it’s Python:

```bash
#!/usr/bin/python3
```

## Syntax Basics
- **Indentation** is critical - Python uses it for code blocks.  
- A `\` can be used to split code over multiple lines (Python will treat it as the same line).  
- `help(functionname)` can be used to view information about a function.  

---

## Variables & Data Types
- A variable stores data in a named location using the `=` sign.  
- **Case-sensitive**: `Variable` and `variable` are different.  

**Main data types:**  
- **Tuple** - Immutable list of items (cannot be changed).  
- **List** - Mutable and ordered collection.  
- **Dictionary** - Stores data in key-value pairs.  
- **Set** - Unordered collection of unique items.  

### Tuples
- Cannot be changed (immutable).  
- Can contain mixed data types.  
- Use `.index()` to find an item’s position.  
- `len()` returns the number of items (indexing starts at 0).  

### Lists
- Ordered and changeable.  
- Can hold mixed data types.  

### Dictionaries
```python
dict1 = {"a": 1, "b": 2, "c": 3}
```
- `.keys()` - view keys  
- `.values()` - view values  
- `.items()` - view all key-value pairs  
- Can contain dictionaries inside dictionaries.  

### Sets
- Store multiple unique values.  
- No duplicate elements.  
- Unordered (order may vary when printed).  

---

## Strings
- Use a **backslash** `\` to escape characters inside a string.  
- `\n` - new line  
- `\\` - backslash  

---

## Booleans & Operators
- **Booleans**: `True` or `False`.  
- `==` - equal to  
- `!=` - not equal to  

**Logical operators:**  
- `and` = both must be true  
- `or` - only one must be true  
- `not` - inverts a boolean value  

---

## Conditionals
```python
if True:
    print("True")

if not False:
    print("Not false")
```

---

## Loops
- **For loop** - repeats a set number of times.  
- **While loop** - repeats until a condition is met.  

```python
for i in range(5):
    print(i + 6)

a = 1
while a < 5:
    a += 1
    print(a)
```

**Control statements:**  
- `break` - exit loop immediately.  
- `continue` - skip to the next iteration.  
- `pass` - placeholder, avoids syntax errors.  

---

## File Reading & Writing
```python
open(filename, mode)
```
**Modes:**  
- `r` - read  
- `w` - write (overwrites)  
- `a` - append  
- `rt` - read text  

**Common methods:**  
- `.read()` - read file contents  
- `.seek()` - change read position  
- `.close()` - close the file  

---

## User Input
```python
name = input("Enter your name: ")
```
- Stores user input as a string unless converted.  

---

## Exceptions & Error Handling
An **exception** is an error during execution (runtime).

**Common errors:**
- `Arithmetic Error` - calculation issues  
- `Syntax Error` - code syntax is wrong  
- `Indentation Error` - unexpected indentation  

```python
try:
    # code
except:
    # handle error
finally:
    # always runs
```

---

## Comprehensions
**List comprehensions** - shorter way to create lists.

```python
nums = [x*2 for x in range(5) if x > 1]
```
- Works with loops and conditionals.  
- An **iterable** is an object you can loop over (e.g., list, tuple, string).  

---

## Functions & Code Reuse
- A **function** is a block of reusable code.  
- Defined with `def` and run when called.  

```python
def function1():
    print("Hello from function!")

function1()
```

- Functions can return values.  
- Can take parameters, including an unknown number of arguments with `*args`.  
- Use `global` to modify a global variable inside a function.  
- **Recursive functions** call themselves until a condition is met.  

---

## Lambdas
- Anonymous (nameless) functions with a single expression.

```python
add_4 = lambda x: x + 4
print(add_4(4))
```
---

## Python Package Manager
- Functions that aren’t built into the standard library.  
- A package contains a bundle of files required for a module.  
- Provides prewritten Python functions for reuse.  

---

## Python Virtual Environment
- An isolated environment to test Python projects.  
- Keeps dependencies and packages separate from the global system.  

---

## Intro to `sys` Module
- Provides functions to interact with the Python runtime environment.  
- Can manipulate program execution and the interpreter itself.  
- Documentation: [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)  

---

## Intro to `requests` Module
- Simplifies making and processing HTTP requests in Python.  
- Useful for interacting with APIs and automation.  
- Documentation: [https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)  

---

## Intro to `pwntools`
- Useful for exploit development and CTF challenges.  
- Allows direct interaction with shellcode and assembly code.  
- Can send and receive data over the network.  
- Documentation: [https://docs.pwntools.com/en/stable/](https://docs.pwntools.com/en/stable/)  
