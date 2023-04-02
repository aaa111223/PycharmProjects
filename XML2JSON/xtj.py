import xml.etree.ElementTree as ET
import json,base64

# 读取XML文件
tree = ET.parse('data.xml')
root = tree.getroot()

# 将XML转换为字典
data = {}
for child in root:
    data[child.tag] = {}
    for subchild in child:
        data[child.tag][subchild.tag] = subchild.text

# 将字典转换为JSON格式
json_data = json.dumps(data, indent=4)

# 将JSON数据写入文件
with open('data.json', 'w') as f:
    f.write(json_data)


base64_str ="SGVsbG8sIHdvcmxkIQ=="

encoded_bytes = base64_str.encode("utf-8")
decoded_bytes = base64.b64decode(encoded_bytes)
decoded_str = decoded_bytes.decode()

print(decoded_str)