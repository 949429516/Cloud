from xml.dom import minidom

# dom = minidom.Document()
# root_node = dom.createElement("root")
#
# dom.appendChild(root_node)
#
# book_node = dom.createElement("book")
#
# root_node.appendChild(book_node)
#
# name_node = dom.createElement("name")
#
# book_node.appendChild(name_node)
#
# name_text = dom.createTextNode('')
#
# name_node.appendChild(name_text)
#
#
# try:
#     with open('dom.xml','w',encoding= 'UTF-8')as f:
#         dom.writexml(f,indent='',addindent='\t',newl='\n',encoding='UTF-8')
# except Exception:
#     pass


L = ['book1', 'book2', 'book3']

class XmlWrite:
    def __init__(self, root, child):
        self.root = root
        self.child = child
        self.dom = minidom.Document()

    def work(self):
        root_node = self.dom.createElement(self.root)
        self.dom.appendChild(root_node)
        for i in self.child:
            child_node = self.dom.createElement(i)
            name_text = self.dom.createTextNode('')
            child_node.appendChild(name_text)
            root_node.appendChild(child_node)

    def wirte(self):
        try:
            with open('dom.xml', 'w', encoding='UTF-8')as f:
                self.dom.writexml(f, indent='', addindent='\t', newl='\n', encoding='UTF-8')
        except Exception:
            pass

a = XmlWrite('auth', L)
a.work()
a.wirte()