import sys
import os

class FileHandling:

    """
    Read the files as lines
    """
    def read_file_lines(self, filename):
        obj  = open(filename, 'r')
        data = obj.readlines()
        lines = []
        for d in data:
            lines.append(d.strip())
        return lines

    """
    Read the file as a string
    """
    def read_file(self, filename):
        obj  = open(filename, 'r')
        return obj.read()
    
    """
    Save the file with the content and filename passed
    Creates the directory if not present
    """
    def save_file(self, content, filename):
        try:
            dir = os.path.dirname(filename)
            if dir != '' and not os.path.exists(dir):
                os.makedirs(dir)
            f = open(filename, 'w+')
            f.write(content)
            f.close()
        except:
            print('Save File:: System Error! Looks like the file/folder was not found')
            sys.exit()