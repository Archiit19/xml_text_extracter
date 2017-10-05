from XMLFile import XMLFile
import os


class ExtractData(object):

    def __init__(self, json_data):
        self.json_data = json_data

    def extract_data_from_xml_file(self):
        for root, dirs, files in os.walk(self.json_data.input_dir.get_path()):
            if self.json_data.xml_file_name in files:
                xml_file = XMLFile(self.json_data, root)
                xml_file.read_xml_file()

    def generate_output(self):
        self.json_data.output_dir.make_archive()
