
class XmlUtil:
    def __init__ (self, filePath):
        self.filePath = filePath

    def readXml(self):
        from xml.etree import ElementTree
        tree = ElementTree.parse(self.filePath)    # xmlファイルを読み込む
        root = tree.getroot()          # ルートを取得する
        print(root.tag)                # fruit

xml_util = XmlUtil("sample.xml")
xml_util.readXml()