import json
from ExtractData import ExtractData
from JsonHelper import JsonHelper


class ExtractXML(object):

    def __init__(self, json_data):
        self.js = JsonHelper(json_data)
        self.ed = ExtractData(self.js)

    def process_and_generate_output(self):
        self.ed.extract_data_from_xml_file()
        self.ed.generate_output()


with open('config.json') as data_file:
    json_data = json.load(data_file)
    ex = ExtractXML(json_data)
ex.process_and_generate_output()
