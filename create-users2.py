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
    # Use /dev/tty to read the Y/N prompt directly from the keyboard
    # This is needed because stdin is redirected to the input file, so input() would
    # read from the file instead of the keyboard without this fix
    sys.stdout.write("Would you like to do a dry run? (Y/N): ")
    sys.stdout.flush()
    with open('/dev/tty') as tty:
        response = tty.readline().strip().upper()
    dry_run = response == 'Y'

    if dry_run:
        print("==> Running in dry-run mode. No changes will be made to the system.\n")

    for line in sys.stdin:
        # This checks if a line starts with #, therefore it means it's a comment.
        # Comment lines can be skipped since they aren't user account data
        match = re.match("^#", line)

        # This removes whitespace and splits the line into fields using ':'
        fields = line.strip().split(':')

        # Skips comments and lines that don't have all required fields
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("==> Skipping comment line: %s" % line.strip())
                else:
                    print("==> ERROR: Skipping line due to incorrect number of fields: %s" % line.strip())
            continue

        # This maps each field index to its meaning
        username = fields[0]
        password = fields[1]
        # Standard Linux user info string format
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group field by , to get what groups the user belongs to
        groups = fields[4].split(',')

        # Prints out that the user is being created
        print("==> Creating account for %s..." % (username))

        # This is the command for creating a user with a disabled password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print("    [DRY RUN] Would run: %s" % cmd)
        else:
            os.system(cmd)

        # Prints out what's happening (password creation)
        print("==> Setting the password for %s..." % (username))

        # Build the command to set the user's password non-interactively
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print("    [DRY RUN] Would run: %s" % cmd)
        else:
            os.system(cmd)

        for group in groups:
            # Only assign the user to a group if the group isn't '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print("    [DRY RUN] Would run: %s" % cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
