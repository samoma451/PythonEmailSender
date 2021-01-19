from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
import templates

def sendEmail():
    host = "smtp.gmail.com"
    port = 587
    username = "samoma451@gmail.com"
    password = "definetlyMyPassword123"
    file_path = "templates\email_message.html"

    try:
        conn = SMTP(host, port)#conn is short for connection
        conn.ehlo()
        conn.starttls()
        toList = ["email1@gmail.com","email2@gmail.com"]

        try:
            conn.login(username, password)#Need to enable "less secure app access" in google account settings to let this app login

            for i in toList:
                message = MIMEMultipart("Test message")
                message["Subject"] = "Test message"
                message["From"] = username
                message["To"] = i

                cutoff = i.index("@")#gets rid of the bit of the address after the @
                receiverName=i[0:cutoff]

                htmlTxt = templates.get_template(file_path).format(email=receiverName)
                message.attach(MIMEText(htmlTxt, "html"))

                conn.sendmail(username, i, message.as_string())  # from, to, message

        except SMTPAuthenticationError:
            print("A login error occured")

        conn.quit()
    except SMTPException:
        print("Error sending message")

sendEmail()