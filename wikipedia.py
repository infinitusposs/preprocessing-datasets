import os
import re
import lxml.etree as ET

parser = ET.XMLParser(recover=True)
# The directory of the original texts (in XML files)
directory = r'wikipedia_dataset/texts'

# The directory that you want to save your texts
target_path = r'wikipedia_dataset/audio/'

# Check if the sentence is more than 100 characters
def check(str):
    sentence = str[0]
    i = 1
    while len(sentence) < 100:
        sentence = sentence + '. ' + str[i]
        i += 1
    return sentence
# For every file in the directory
for filename in os.listdir(directory):
    path = directory + '/' + filename
    root = ET.parse(path, parser=parser)
    # Get the text in the tag 'text'
    for text in root.iter('text'):
        str = re.split('\.\s*[A-Z]', text.text)
        # Set the name of the TXT file to the same name as the corresponding image
        for file in root.iter('image'):
           image_name = file.attrib['id'] + '.txt'
        sentence = check(str)
        f = open(target_path + image_name, "w", encoding='utf-8')
        f.write(sentence)
        f.close()

