import os
import shutil
import xml.etree.ElementTree as ET
from Directory import Directory


class XMLFile(object):
    """A Directory will have path and name with
        following properties:

        Attributes:
            file_name: A string representing the directory name.
            file_path: path where the directory will be created.
        """

    def __init__(self, json_data, file_path=os.getcwd()):
        self.json_data = json_data
        self.set_file_name()
        self.set_file_path(file_path)
        self.set_file_root()

    def set_file_name(self):
        self.file_name = self.json_data.xml_file_name

    def set_file_path(self, file_path):
        self.file_path = os.path.join(file_path, self.file_name)

    def set_file_root(self):
        with open(self.file_path) as f:
            tree = ET.parse(f)
            self.file_xml_root = tree.getroot()

    def get_file_path(self):
        return self.file_path

    def get_file_name(self):
        return self.file_name

    def get_xml_root(self):
        return self.file_xml_root

    def read_xml_file(self):
        for elem in self.file_xml_root.getiterator():
            if self.json_data.tag == elem.tag:
                if self.json_data.attribute == "":
                    text_xml_to_search = elem.text
                else:
                    text_xml_to_search = elem.get(self.json_data.attribute)
                if text_xml_to_search in self.json_data.search_text_list:
                    output_inside_dir = Directory(text_xml_to_search, self.json_data.output_dir.get_path())
                    self.copydwf(output_inside_dir)


    def copydwf(self, output_inside_dir):
        path_list = self.file_path.split('\\')
        src = os.path.join( self.json_data.input_dir.get_path(), path_list[-1] )
        dst = os.path.join( output_inside_dir.get_path(), path_list[-1])
        shutil.copyfile(src, dst)
