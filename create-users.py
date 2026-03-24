#!/usr/bin/python3

# INET4031
# Fenky Wah
# Comments modified
# 3/23/2026

# The os import is used to execute system level commands
# The re import is used for regular expression matching to detect comment lines
# The sys import is used to read the inputs from stdin
import os
import re
import sys

def main():
    for line in sys.stdin:

        # This checks if a line starts with #, therefore it means it's a comment.
	# Comment lines can be skipped since they aren't user account data
        match = re.match("^#",line)

        # This removes whitespace and split the line into fields using ':'
        fields = line.strip().split(':')

        # Skips comments and lines that don't have all required fields
        if match or len(fields) != 5:
            continue

        # This maps each field index to its meaning 
        username = fields[0]
        password = fields[1]
	# standard Linux user info string format
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the group field by , to get what groups the user belongs to
        groups = fields[4].split(',')

        # Prints out that the user is being created
        print("==> Creating account for %s..." % (username))
        # This is the command for creating a user with a disabled password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
	
	# The print(cmd) line is to check to see if the command is typed correctly
        # If the os.system(cmd) comment were to be uncommented, it will execute the adduser command (cmd) and create a user account
        #print(cmd)
        os.system(cmd)

        # This purpose is to print out what's happening (password creation)
        print("==> Setting the password for %s..." % (username))
        # 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # If the os.system(cmd) were to be executed, it will set the user's password on the system
        #print(cmd)
        os.system(cmd)

        for group in groups:
            # It only assign the user to a group if the group isn't '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
