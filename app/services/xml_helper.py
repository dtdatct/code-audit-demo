import xml.dom.minidom


def parse_order(xml_text):
    doc = xml.dom.minidom.parseString(xml_text)
    return doc.getElementsByTagName("sku")[0].firstChild.data
