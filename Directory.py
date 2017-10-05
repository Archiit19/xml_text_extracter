import os
import shutil


class Directory(object):
    """ A Directory will have path and name with following properties:

        Attributes:
            dir_name: A string representing the directory name.
            dir_path: path where the directory will be created.
    """

    def __init__(self, dir_name, dir_path=os.getcwd()):
        self.dir_name = dir_name
        self.dir_path = os.path.join(dir_path, self.dir_name)
        self.create_directory(self.dir_path)

    @staticmethod
    def create_directory(dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def set_path(self, dir_path):
        self.dir_path = os.path.join(dir_path, self.dir_name)

    def get_path(self):
        return self.dir_path

    def set_dir_name(self, dir_name):
        self.dir_name = dir_name

    def get_dir_name(self):
        return self.dir_name

    def make_archive(self):
        shutil.make_archive(self.get_path(), 'zip', root_dir=self.get_path())