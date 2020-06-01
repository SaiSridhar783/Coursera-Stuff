#!/usr/bin/env python3

import os
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
styles = getSampleStyleSheet()

def generate_report(attachment , title, paragraph):
    #today = str(date.today())
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title  , styles["h1"])
    report_body = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title,report_body])