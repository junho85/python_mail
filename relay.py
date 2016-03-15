#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.header import Header

server = "localhost"
port = 2525

from_addr = "junho85@daum.net"
to = "junho85@gmail.com"

msg = MIMEText("hello world", "text", "utf-8")
msg['Subject'] = Header(s="테스트 제목 입니다", charset="utf-8")
msg['From'] = from_addr
msg['To'] = to

smtp = smtplib.SMTP(server, port)
smtp.sendmail(from_addr, to, msg.as_string())