#etree
import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("student.xml")
print("利用getiterator访问：")
nodes = root.getiterator()
for node in nodes:
    print("{0}--{1}".format(node.tag, node.text))



print("利用find和findall方法：")
ele_hobby = root.find("hobby")
print(type(ele_hobby))
print("{0}--{1}".format(ele_hobby.tag, ele_hobby.text))


ele_clsmate = root.findall("classmate")
print(type(ele_clsmate))
for ele in ele_clsmate:
    print("{0}--{1}".format(ele.tag, ele.text))
    for sub in ele.getiterator():
        if sub.tag =="classmate":
            if "other" in sub.attrib.keys():
                print(sub.attrib['other'])