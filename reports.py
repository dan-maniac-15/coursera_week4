#!/usr/bin/python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os
import requests

def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    report.build([report_title, report_info])

def get_name_weight_list(result, dir):
    dic_list = []
    for file_from_list in result:
        with open(dir + file_from_list) as file_data:
            dict_return = {
                'name': 'name',
                'weight': 'weight',
            }
            counter = 0
            for line in file_data:
                if counter == 0:
                    dict_return['name'] = line.replace( '\n' , '' )
                    counter += 1
                elif counter == 1:
                    dict_return['weight'] = line.replace( '\n' , '' )[:-3]
                    counter += 1    
        dic_list.append(dict_return)
    return dic_list

def create_body(dic_list):
    additional_info = ""
    for line in dic_list:
        additional_info += 'name: ' + line['name'] + '<br/>'
        additional_info += 'weight: ' + line['weight'] + '<br/>'
        additional_info += '<br/>'
    return additional_info
