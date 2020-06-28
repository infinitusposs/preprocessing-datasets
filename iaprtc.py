import lxml.etree as ET
import os

parser = ET.XMLParser(encoding="utf-8")

# Directory of the ENG files
directory = r'iaprtc12/annotations_complete_eng/'
# Directory to save the TXT files
target_path = r'iaprtc12/text/'

for dir_name in os.listdir(directory):
    dir_path = directory + dir_name + '/'
    for filename in os.listdir(dir_path):
        path = dir_path + filename
        root = ET.parse(path, ET.XMLParser(encoding='ISO-8859-1', ns_clean=True, recover=True))
        # ET.XMLParser(encoding='ISO-8859-1', ns_clean=True, recover=True)
        for description in root.iter('DESCRIPTION'):
            image_name = os.path.splitext(filename)[0] + '.txt'
            f = open(target_path + image_name, "w", encoding='utf-8')
            f.write(description.text)
            f.close()
