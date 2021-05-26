import xml.etree.ElementTree as ET
import sys
import json
import pathlib

current_dir = pathlib.Path(__file__).parent
current_file = pathlib.Path(__file__)

FILE_PATH = current_dir / sys.argv[1]
print(FILE_PATH)

root = ET.parse(FILE_PATH).getroot()


et_string = ET.tostring(root, encoding='utf8').decode('utf8')

ns = {
    'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
    'ns': 'http://www.opentravel.org/OTA/2003/05/common/',
}


def to_json(dict):
    with open('new_parsed.json', 'w') as outfile:
        json.dump(dict, outfile, indent=4)


xml = ET.fromstring(et_string)


def xml_tags(xml):
    rowinfo_list = xml.findall('.//{http://www.opentravel.org/OTA/2003/05/common/}RowInfo', ns)
    fee_list = xml.findall('.//{http://www.opentravel.org/OTA/2003/05/common/}Fee', ns)

    dict_list = []
    dict = {
        'seat_num': '',
        'cabin_class': '',
        'availability': '',
        'seat_price': None,
           }

    count_fee = 0
    for rowinfo_tag in rowinfo_list:
        dict_copy = dict.copy()
        dict_copy['cabin_class'] = rowinfo_tag.attrib['CabinType']
        summary_list = rowinfo_tag.findall('.//{http://www.opentravel.org/OTA/2003/05/common/}Summary', ns)
        for summary_tag in summary_list:
            dict_copy = dict_copy.copy()

            dict_copy['seat_num'] = summary_tag.attrib['SeatNumber']
            dict_copy['availability'] = summary_tag.attrib['AvailableInd']

            if dict_copy['availability'] == 'true':
                dict_copy['seat_price'] = fee_list[count_fee].attrib['Amount']
                count_fee += 1
            else:
                dict_copy['seat_price'] = None

            dict_list.append(dict_copy)

    to_json(dict_list)

xml_tags(xml)
