import json
import xml.etree.ElementTree as ET

# 读取JSON文件
with open('data.json', 'r') as f:
    data = json.load(f)

# 创建根元素
root = ET.Element('root')

# 创建子元素并添加到根元素中
person = ET.SubElement(root, 'person')
name = ET.SubElement(person, 'name')
name.text = data['person']['name']
age = ET.SubElement(person, 'age')
age.text = str(data['person']['age'])
city = ET.SubElement(person, 'city')
city.text = data['person']['city']

# 将XML数据写入文件
tree = ET.ElementTree(root)
tree.write('data.xml', encoding='utf-8', xml_declaration=True)
