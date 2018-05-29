# -*- coding: utf-8 -*-
class XmlUtil:
    def readXml(filePath):
        from xml.etree import ElementTree
        tree = ElementTree.parse(filePath)    # xmlファイルを読み込む
        root = tree.getroot()          # ルートを取得する
        print(root.tag)                # fruit

    readXml("sample.xml")