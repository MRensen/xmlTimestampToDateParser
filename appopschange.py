#!/usr/bin/env/ python3
# coding=utf-8

import xml.etree.ElementTree as ET
from datetime import datetime
tree = ET.parse('appops.xml')
root = tree.getroot()

for op in root.iter('op'):
    attrib = op.attrib.keys()
    for key in attrib:
        value = op.get(key)
        if len(value) == 13:
            newvalue = datetime.utcfromtimestamp(int(value)/1000).strftime('%Y-%m-%d %H:%M:%S')
            op.set(key, str(newvalue))
            print("key: " + key + ", value: " + newvalue)

tree.write("Newappops.xml")



