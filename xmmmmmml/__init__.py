from pprint import pprint
from xml.etree import ElementTree as ET

doc = ET.parse('nasa.xml')
root = doc.getroot()

# pprint(list(map(lambda x: x.attrib, root[:15])))

# authors = root.iter('author')
# pprint(['{0} {1}'.format(author[0].text, author[1].text) for author in authors])

name = 'Spencer'
spencer = root.find(".//lastName[.='%s']/ancestor::dataset/subject" % name)

pprint(spencer.text)
