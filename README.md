# INET4031 - Create Users ScriptAdd Users Script and User List

## Program Description

This script allows you to automatically add users onto your Linux (Ubuntu) machine without having to manually do it yourself. You give it a text file with a list of users and it runs the 'adduser' and 'passwd' commands for you. This saves you time and you don't have to worry about forgetting a step.

---

## Program User Operation

You set up an input file with your list of users, make sure the script is executable, and run it. The script reads through the file line by line and creates each account. Any line that is a comment or does not have the right number of fields gets skipped automatically.

---

### Input File Format

Each line should have 5 fields separated by colons:

username:password:lastname:firstname:group1,group2

- **username** — the login name for the account
- **password** — the password for the account
- **lastname** — user's last name
- **firstname** — user's first name
- **groups** — groups to add the user to, separated by commas

**To skip a line** — put a `#` at the start of it.

**If you don't want the user in any groups** — put a `-` in the groups field.

### Command Execution

First make sure the script is executable:
 
```bash
chmod +x create-users.py
```
 
Then run it with sudo and point it at your input file:
 
```bash
sudo ./create-users.py < create-users.input
```
 
---
 
### Dry Run
 
If you want to test the script without actually creating any accounts, you can do a dry run. In the script, uncomment the `print(cmd)` lines and leave `os.system(cmd)` commented out:
 
```python
print(cmd)      # uncomment this
#os.system(cmd) # leave this commented out
```
 
This will print out every command the script would run so you can check that everything looks right before running it for real.
