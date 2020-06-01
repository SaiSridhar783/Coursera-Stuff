#!/usr/bin/env python3

import os
import reports
import datetime
import emails

if __name__ == "__main__":
  path = "/home/student-01-4cd26df1f758/supplier-data/descriptions"
  para = "<br/>"
  files = os.listdir(path)
  today = str(datetime.date.today())

  for file in files:
    i = 0
    with open(os.path.join(path,file)) as data:
      for line in data:
        if i==2:
          break
        if i==0:
          para += "name: {}".format(line.strip())+"<br/>"
          i +=1
        elif i==1:
          para += "weight: {}".format(line.strip())+"<br/>"+"<br/>"
          i +=1

  reports.generate_report("/tmp/processed.pdf", "Processed Update On "+today, para)
  print(para)
  sender = "automation@example.com"
  recipient = "student-01-4cd26df1f758@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment_path = "/tmp/processed.pdf"

  message = emails.generate_email(sender, recipient, subject, body, attachment_path)
  emails.send_email(message)