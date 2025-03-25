# inet_4031_adduser_script
# Program Discription 
This Python script automates the creation of user accounts on Unix-based systems utilizing input data. It retrieves user information from an input file, processes the information, and later establishes user accounts with specified attributes, including the individual’s full name and group. By automating this process, the script eliminates the necessity for manual entry of each user’s details and their group assignments, thereby saving time and reducing the likelihood of human error.

# Program User Operation
To use this script, the user provides an input file in a specific format, that has the necessary details for each user (username, password, full name). The script runs each line, skipping lines that are comments or improperly formatted, then creates users and assigns them to groups.

# Input File Format
Each line in the input file should contain five fields separated by colons (:):

  Username: The username of the user to be created.
  
  Password: The password to be assigned to the user.
  
  Full Name: The user’s full name (can be a first and last name.
  
  Group(s): Comma-separated list of groups to which the user should belong. If the      user does not need to be assigned to any groups, this field can be left as "-".
  
  Additional Information: A placeholder for any additional information; not currently 
  used in this script.

# Command Execution
Make sure the Python script is executable. If it's not, you can make it executable by running the following command:

`chmod +x create-users.py`
To run the script, provide the input file via standard input. Use the following command:

`./create-users.py < createusers.input`
This command runs the script and processes each line from the input file to create users and set their passwords. The script will print messages to the terminal showing the progress of each operation.

# Dry Run?
If you just want to try out the script without it actully making chaged to your system you can do something called a "Dry Run". Doing this will pring the commands it would execute but not preform any system changes. This allows you to verify if the script is working as intended before you fully implement it. 

To enable the dry run, you can uncomment the print(cmd) statements in the script to display the commands that would be run. For example:
`# print(cmd)  # Uncomment for dry run (print commands without executing them)`
