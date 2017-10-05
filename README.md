# xml_text_extracter

Searches xml files tags for specific attribute or text and generates output containing files where search is found.

Config.json :- User needs to modify this file.

Input_directory : Directory name containing input data. This folder should be present besides your scripts.

Output_directory : Directory generated with this name contains 'specific search text' folders. These folders contains xml files in which that text is found.

Xml_file_name : Provide XML file name to be searched.

Xml_tag" : XML Tag to be searched for the text.

Xml_attribute" : If you want to search specifically in some attribute then provide this name.

Search_text_list : Comma separated list of strings to search.


Sample Config.json File :- 

{
    "input_directory" : "input_data",
    "output_directory" : "output_data",
    "xml_file_name" : "Content.xml",
    "xml_tag" : "type",
    "xml_attribute" : "hardcopy",
    "search_text_list" : 
    [
      "book_name_1",
      "book_name_some",
      "book_name_5"
    ]
}
