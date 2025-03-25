#!/usr/bin/python3

# INET4031
# Nkwele Ngole
# Date Created: 03/25/25
# Date Last Modified: 03/25/25


import os  # Interacts with the operating system, executes shell commands, and manages files
import re  # Handles regular expressions for pattern matching and text parsing
import sys  # Provides access to system-specific parameters like standard input

def main():
    # Prompts user for dry-run mode
    dry_run = input("Would you like to run the script in dry-run mode? (Y/N): ").strip().upper()
    for line in sys.stdin:  # Reads each line from standard input

        # This checks if the line starts with "#"
        # The script skips these lines because they do not contain user data
        match = re.match("^#", line)

        # Splits the line into fields using ":" just like  /etc/passwd format
        fields = line.strip().split(':')

        # If the line is a comment or does not contain exactly 5 fields, skip it
        # This makes sure the script only processes properly formatted lines
        if match or len(fields) != 5:
            if dry_run == 'Y':
                print(f"Skipping line: {line.strip()} (Invalid format or comment)")
            continue

        # Extract user information from the parsed fields:
        username = fields[0]  # Username
        password = fields[1]  # Password (plaintext, which is not secure)
        gecos = "%s %s,,," % (fields[3], fields[2])  # Combines full name fields into GECOS format

        # Groups are stored in the 5th field, separated by commas
        # Splitting allows multiple group assignments
        groups = fields[4].split(',')

        # Inform the user that an account is being created
        print("==> Creating account for %s..." % (username))

        # Makes the command to create a user without setting a password first
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run == 'Y':
            # If it's a dry run, print the command instead of executing it
            print(f"Dry Run: {cmd}")
        else:
            # Normally, execute the command to create the user
            os.system(cmd)

        # The first time running the script, this should be printed for debugging.
        # Uncomment to actually create the user.
        # print(cmd)
        

        # Tells the user that a password is being set
        print("==> Setting the password for %s..." % (username))

        # Makes the  command to set the user's password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run == 'Y':
            # If it's a dry run, print the command instead of executing it
            print(f"Dry Run: {cmd}")
        else:
            # Normally, execute the command to set the password
            os.system(cmd)
        # The first time running the script, print for debugging.
        # Uncomment to actually set the password.
        # print(cmd)
       

        for group in groups:
            # If the group field is "-", skip this step because there are no additional groups for the user
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                # Makes the command to add the user to the specified group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry_run == 'Y':
                    # If it's a dry run, print the command instead of executing it
                    print(f"Dry Run: {cmd}")
                else:
                    # Normally, execute the command to assign the user to the group
                    os.system(cmd)
    
    # If it's a dry run, remove the users using deluser to clean up
    if dry_run == 'Y':
        print("\nDry Run Complete. Cleaning up by removing users (No actual changes were made).")
        for line in sys.stdin:
            fields = line.strip().split(':')

            if len(fields) != 5 or re.match("^#", line):
                continue

            username = fields[0]
            cmd = f"/usr/sbin/deluser --remove-home {username}"

            # Print the command to be run (dry run removal)
            print(f"Dry Run: {cmd}")
# Ensures the script runs only if executed directly and not imported
if __name__ == '__main__':
    main()

