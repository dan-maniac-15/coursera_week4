#!/usr/bin/python3

import emails
import reports
import os
import datetime

def create_pdf(dir):
    additional_info = ""
    result = os.listdir(dir)
    for file_from_list in result:
        with open(dir + file_from_list) as file_data:
            line = file_data.readlines()
            additional_info += 'name: ' + line[0] + '<br/>'
            additional_info += 'weight: ' + line[1] + '<br/><br/>'
    return additional_info

def main():
    filename        = "/tmp/processed.pdf"
    title           = "Processed Update on " + datetime.datetime.now().strftime('%Y-%m-%d')
    dir             = "supplier-data/descriptions/"
    additional_info = create_pdf(dir)
    reports.generate_report(filename, title, additional_info)

    sender          = "automation@example.com"
    recipient       = "<user>@example.com"
    subject         = "Upload Completed - Online Fruit Store"
    body            = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = filename
    messages = emails.generate(sender, recipient, subject, body, attachment_path)

    emails.send(messages)

if __name__ == "__main__":
    main()