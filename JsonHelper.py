from Directory import Directory


class JsonHelper(object):

    def __init__(self, data):
        self.data = data
        self.xml_file_name = ""
        self.tag = "root"
        self.attribute = ""
        self.search_text_list = []
        self.set_input_directory()
        self.set_output_directory()
        self.set_xml_file_name()
        self.set_tag()
        self.set_attribute()
        self.set_search_text_list()

    def set_input_directory(self):
        try:
            self.input_dir = Directory(self.data['input_directory'])
        except ValueError or KeyError:
            self.input_dir = Directory("input_directory")
            print "Input directory name is not provided. Default - input_directory"

    def set_output_directory(self):
        try:
            self.output_dir = Directory(self.data['output_directory'])
        except ValueError or KeyError:
            self.output_dir = Directory("output_directory")
            print "Output directory name is not provided. Default - output_directory"

    def set_xml_file_name(self):
        try:
            self.xml_file_name = self.data["xml_file_name"]
        except ValueError or KeyError:
            print "XML File Name is not provided."

    def set_tag(self):
        try:
            self.tag = self.data["xml_tag"]
        except ValueError or KeyError:
            print "XML Tag to search is not provided."

    def set_attribute(self):
        try:
            self.attribute = self.data["xml_attribute"]
        except ValueError or KeyError:
            print "XML Attribute inside tag search is not provided."

    def set_search_text_list(self):
        try:
            self.search_text_list = self.data["search_text_list"]
        except ValueError or KeyError:
            print "Text to Search is not provided."
