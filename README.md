# inet 4031 adduser script

## description
This python script automates the creation of user account and group assignments on an Ubuntu Linux system. 


# program Operation

### How to run

sudo ./create-users.py < create-users.input

### Input file format
username:password:lastname:firstname:group1, group2

Lines starting with # are skipped.
use - in the groups field if the user has no groups.
Lines with fewer than 5 fields are skipped.

### Dry Run
Comment out the three os.system(cmd) Lines before running to test without making changeshow
