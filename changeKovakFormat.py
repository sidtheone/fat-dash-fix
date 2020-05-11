# The following code will search 'HH:MM:SS.XXX' ,
# and replace with 'HH:MM:SS:XXX' in multi-line mode.
import re
import os
import fnmatch
for dname, dirs, files in os.walk("."):
    # raw_input returns the empty string for "enter"
    print("This file will find all the csv file in the given folder/directory and replace the string.\nPlease proceed with caution.")
    print("Please confirm the directory path before proceeding \n")
    cwd = os.getcwd()
    msg = 'Process ' + cwd
    proceed = raw_input("%s (y/N) " % msg).lower() == 'y'
    if(proceed):
        for fname in files:
            if (fnmatch.fnmatch(fname, '*.csv')):            
                print("processing "+fname)
                fpath = os.path.join(dname, fname)
                with open (fpath, 'r' ) as f:
                    content = f.read()
                    #regex for replacement
                    content_new = re.sub('(..:..:..)(\.)(..)',r'\1:\3', content, flags = re.M)
                with open(fpath, "w") as f:
                    f.write(content_new)