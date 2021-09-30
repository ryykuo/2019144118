# 2019144118
#coding:gb2312
#coding
import smtplib
from email.mime.text import MIMEText
msg_from='209246303@qq.com'
passwd='mkjemwjwcnybihj'
msg_to='421808206@qq.com'

subject="2019144118gujie"
cont:UTF-8ent="WaiWangIP: Date:172.68.141.84    WIFI:180.129.255.53    NeiWangIP: Date:10.116.206.124  WIFI:10.101.84.227"
msg=MIMEText(content)
msg['Subjest']=subject
msg['From']=msg_from
msg['To']=msg_to
try:
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,passwd)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("bingo")
except(s.SMTPException,e):
    print("ohh no!")
finally:
    s.quit()
