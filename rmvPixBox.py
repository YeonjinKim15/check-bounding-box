"""

This file needs debugging
Please duplicate the test XML file folder before you run this file to prevent permanent damage to the data

*** *** parts to be added

"""

from xml.etree import ElementTree as et


# *** Loop through and check all files in the folder (or folders) ***
# Copy and paste XML folder directory path here
"""
dirPath = ''
fileName = 
filePath = dirPath + filename
newFileName = dirPath + "New" + fileName
"""


tree = et.parse('Your/Xml/Path.xml')
root = tree.getroot()
objects = root.findall("object")

# Locate 4 points in bounding boxes
for object in objects:
    bndBoxs = object.findall('bndbox')
    for bndBox in bndBoxs:
        xmin = int(bndBox.findtext("xmin"))
        xmax = int(bndBox.findtext("xmax"))
        ymin = int(bndBox.findtext("ymin"))
        ymax = int(bndBox.findtext("ymax"))
        x = xmax - xmin
        y = ymax - ymin
        
        # Remove points if width is smaller than 4 pixels
        if x < 4:
            print("Hey, I found a pixel")
            print(xmax, xmin, ymax, ymin)
            root.remove(object)
        # Remove points if height is smaller than 4 pixels
        elif y < 4:
            print("Hey, I found a pixel")
            print(xmax, xmin, ymax, ymin)
            root.remove(object)
        # Keep the bounding box if both width and height are bigger than 3
        else:
            continue

"""
Choose one of the two methods below to save the new XML file
XML file will be saved in a different name as there can be an unexpected error in this code
"""


# Save to a current directory
# *** Name will be changed to "New"+ original file name ***
tree.write('New_changed.xml')


# *** Save to the same directory where original xml file is located ***