#!/usr/bin/python3
# INET4031
# Oliif Itana
# Date Created: April 30, 2026
# Date Last Modified: May 6, 2026
import os
import re
import sys

def main():
    # Check if user passed Y or N as argument for dry-run mode
    if len(sys.argv) < 2 or sys.argv[1].upper() not in ['Y', 'N']:
        print("Usage: ./create-users2.py Y|N < create-users.input")
        print("Y = dry-run mode, N = normal mode")
        sys.exit(1)

    dry_run = sys.argv[1].upper()

    if dry_run == 'Y':
        print("==> Running in DRY-RUN mode. No changes will be made.")
    else:
        print("==> Running in NORMAL mode. Users will be created.")

    for line in sys.stdin:
        # Check if the line starts with # meaning it should be skipped
        match = re.match("^#", line)
        # Strip whitespace and split the line into fields using colon as delimiter
        fields = line.strip().split(':')
        # If line starts with # skip it
        if match:
            if dry_run == 'Y':
                print("==> Skipping commented line: %s" % line.strip())
            continue
        # If line does not have exactly 5 fields skip it
        if len(fields) != 5:
            if dry_run == 'Y':
                print("==> ERROR: Invalid line skipped: %s" % line.strip())
            continue
        # Extract username, password, and full name from the fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        # Split the groups field by comma to get individual group names
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))
        # Build the adduser command and run it to create the user account
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        print(cmd)
        if dry_run != 'Y':
            os.system(cmd)

        print("==> Setting the password for %s..." % (username))
        # Build the password command and run it to set the user password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        print(cmd)
        if dry_run != 'Y':
            os.system(cmd)

        for group in groups:
            # If the group is not - then assign the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                print(cmd)
                if dry_run != 'Y':
                    os.system(cmd)

if __name__ == '__main__':
    main()
