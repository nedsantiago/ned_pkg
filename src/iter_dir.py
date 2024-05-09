from os import walk
from os.path import join, isdir

class FilesFinder():
    """
    This class holds the find files function that takes a string of the root directory 
    to be parsed. This class needs to be instatiated with the root directory string, the payload
    function, and the filter function. When running the find files method, the instance will
    run through the directory looking for files that passes the filter function then executes
    the payload on each valid file directory.
    """
    
    def __init__(self, root_dir: str, payload, filter_func):
        assert callable(payload), "payload needs to be a function"
        assert callable(filter_func), "filter needs to be a function"
        assert isdir(root_dir), "invalid root directory"
        
        self.root_dir = root_dir
        self._payload = payload
        self._filter_func = filter_func
    
    def find_files(self):
        """
        Iterates through the directory then runs the payload at each file
        """

        for root, dirs, files in walk(self.root_dir, topdown=False):
            for filename in files:
                filename_full_dir = join(root, filename)
                if self._filter_func(filename_full_dir):
                    self._payload(filename_full_dir)