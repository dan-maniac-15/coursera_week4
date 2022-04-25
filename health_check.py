#!/usr/bin/python3

import shutil
import psutil
import socket
import emails
import reports

cp = psutil.cpu_percent(interval=1)
du = shutil.disk_usage("/")
du = du.free / du.total
mu = psutil.virtual_memory()
mu = mu.total / 1024 **2
fl = socket.gethostbyname("localhost")

sender          = "automation@example.com"
recipient       = "<user>@example.com"
body            = "Please check your system and resolve the issue as soon as possible."
attachment_path = ""

if cp > 0.8:
    subject         = "Error - CPU usage is over 80%"
    messages = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(messages)
elif du < 0.2:
    subject         = "Error - Available disk space is less than 20%"
    messages = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(messages)
elif mu < 500:
    subject         = "Error - Available memory is less than 500MB"
    messages = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(messages)
elif fl < '127.0.0.1':
    subject         = "Error - localhost cannot be resolved to 127.0.0.1"
    messages = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(messages)