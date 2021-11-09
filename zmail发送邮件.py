'''
1.导包
2.添加邮件内容，包含：主题（subject）、正文（content_text）(content_html)、附件（attachments）——一般存储在字典中
3.添加发件人，包含：发件人账号，授权码 —— 一般存储在字典中
4.添加收件人，包含：收件人地址，多个收件人以列表存储
5.发送邮件
发件人登录：server = zmail.server(username,password)
发件人发送邮件，出入收件人地址，邮件内容 server.send_email(revicer,email_content)

'''

import zmail

# 读取html里面的内容
file = open("计算器.html","r",encoding="utf-8")
msg = file.read()

# 邮件内容
msg_content = {
    "subject":"高志远的加法测试报告",
    "content_text": msg,
    "attachments": ""
}

# 收件人
receivers = ["2941331697@qq.com"]

# 发件人
sender = {"username":"2836904262@qq.com","password":"tuzzrsmxdpazdfbc"}

# 发送邮件
server = zmail.server(sender['username'],sender['password'])  #登录邮箱
server.send_mail(receivers,msg_content)

print("邮件发送成功")





