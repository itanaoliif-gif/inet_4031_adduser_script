#!/usr/bin/python3

# INET4031

# Oliif Itana

# Date Created: April 30, 2026

# Date Last Modified: April 30, 2026


import os
import re
import sys

def main():

    for line in sys.stdin:

        # Check if the line starts with # meaning it should be skipped
        match = re.match("^#",line)

        # Strip whitespace and split the line into fields using colon as the delimiter
        fields = line.strip().split(':')

        # Skip the line if it starts with # or does not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract username, password, and full name from the fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the groups field by comma to get individual group names
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))

        # Build the adduser command and run it to create the user account
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        print(cmd)
        os.system(cmd)

        print("==> Setting the password for %s..." % (username))

        # Build the password command and run it to set the user password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        os.system(cmd)

        for group in groups:
            # If the group is not - then assign the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()










             
