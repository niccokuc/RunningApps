# 1. Obtain list of runnig PID's
# 2. List them in a list
# 3. Make a loop to check the total count
# 4. If there is a change in count, compare the list and determine the new PID
# 5. Print "new PID is running"


import psutil, re
from shutil import copyfile
from difflib import ndiff

# 1. Obtain list of running PID's
x = 1
old_number_line = 0

while x > 0:
    if x%2==0:
        filestr="list_pid_EVEN" #even
    else:
        filestr="list_pid_ODD"

    f = open(filestr, "w")

    # 2. List PID Process in a file, "filstr"
    #This the the main thread to open the PIDs and have a look at them and store them. """
    for proc in psutil.process_iter():
        try:
            pid_info = proc.as_dict(attrs=['pid', 'name'])
            str_pinfo = str(pid_info)
            f.write(str_pinfo+'\n')#It stores them one line at a time."""
        except psutil.NoSuchProcess:
            e = open("no_such_process", "w+")#If a process that has not been recognised is started, make a no_such_process file"""
            str_pinfo = str(pid_info)
            e.write(str_pinfo)
            break
    num_lines = 0 #I only use the line count, but i could use the words and char.'''
    num_words = 0
    num_chars = 0
    f.close() #It's important to close the file, since the file that is open cna still be written into it thus creating bogus results.'''
    fname = f.name #associate a fname to count the lines'''

    with open(fname, 'r') as fu:
        for line in fu:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    # 3. Make a loop to check the total count
    # 4. If there is a change in count, compare the list and determine the new PID
    print(old_number_line)
    print(num_lines)
    if (old_number_line>0) and (old_number_line != num_lines):
        print("NEW NUMBER")
        print("old number", old_number_line)
        print("new number", num_lines)
        diff = open("difference_file", "w+")
        with open("list_pid_EVEN") as a, open("list_pid_ODD") as b:
            for dif in ndiff(a.readlines(), b.readlines()):
                # 5. Print "new PID is running"
                diff.write(dif+'\n')
        diff.close()
        old_number_line = num_lines
    else:
        old_number_line = num_lines
    f.close()
    x=x+1
