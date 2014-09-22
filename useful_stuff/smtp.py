import smtplib

new_socket = smtplib.SMTP_SSL
server = new_socket()
server.connect()
#server.login('', '')

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

server.sendmail('from@who.com',
                ['to@who.com'],
                message)
server.quit()