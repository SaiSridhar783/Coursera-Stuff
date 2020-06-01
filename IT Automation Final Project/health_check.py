#!/usr/bin/env python3

import shutil
import psutil
import os
import socket
import emails
import time

if __name__ == "__main__":
  cpu = psutil.cpu_percent()
  ram = (psutil.virtual_memory()[1])/1024//1024
  disk = shutil.disk_usage("/")
  host = socket.gethostbyname('localhost')

  sub = ""
  if cpu>0.8:
    sub = "Error - CPU usage is over 80%"

  elif disk[2]/disk[0]<0.2:
    sub = "Error - Available disk space is less than 20%"

  elif ram<500:
    sub = "Error - Available memory is less than 500MB"

  elif host!="127.0.0.1":
    sub = "Error - localhost cannot be resolved to 127.0.0.1"

  else:
    pass

  if sub:
    sender = "automation@example.com"
    recipient = "student-01-4cd26df1f758@example.com"
    subject = sub
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)

  else:
    pass
